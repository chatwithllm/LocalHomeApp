import Foundation
import Vision
import AppKit

struct BridgeResult: Codable {
    let success: Bool
    let ocr_text: String
    let error_message: String?
}

func emit(_ result: BridgeResult) {
    let encoder = JSONEncoder()
    encoder.outputFormatting = [.sortedKeys]
    if let data = try? encoder.encode(result), let text = String(data: data, encoding: .utf8) {
        FileHandle.standardOutput.write(text.data(using: .utf8)!)
        FileHandle.standardOutput.write("\n".data(using: .utf8)!)
    } else {
        fputs("{\"success\":false,\"ocr_text\":\"\",\"error_message\":\"failed to encode JSON output\"}\n", stderr)
    }
}

guard CommandLine.arguments.count >= 2 else {
    emit(BridgeResult(success: false, ocr_text: "", error_message: "missing image path argument"))
    exit(1)
}

let imagePath = CommandLine.arguments[1]
let imageUrl = URL(fileURLWithPath: imagePath)

guard FileManager.default.fileExists(atPath: imagePath) else {
    emit(BridgeResult(success: false, ocr_text: "", error_message: "source image does not exist"))
    exit(1)
}

guard let image = NSImage(contentsOf: imageUrl) else {
    emit(BridgeResult(success: false, ocr_text: "", error_message: "failed to load image"))
    exit(1)
}

guard let tiffData = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiffData),
      let cgImage = bitmap.cgImage else {
    emit(BridgeResult(success: false, ocr_text: "", error_message: "failed to create CGImage"))
    exit(1)
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["en-US"]

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])

do {
    try handler.perform([request])
    let observations = request.results ?? []
    let lines = observations.compactMap { $0.topCandidates(1).first?.string }
    emit(BridgeResult(success: true, ocr_text: lines.joined(separator: "\n"), error_message: nil))
} catch {
    emit(BridgeResult(success: false, ocr_text: "", error_message: "Vision OCR failed: \(error.localizedDescription)"))
    exit(1)
}
