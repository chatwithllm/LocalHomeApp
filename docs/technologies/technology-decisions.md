# Technology Decisions

## Initial Decisions

### Python 3.11+
- **Why**: strong ecosystem, typing support, maintainable backend implementation.
- **Where used**: all core runtime and CLI tooling.
- **Alternatives considered**: Node.js, Go.
- **Portability implications**: strong cross-platform portability.
- **Privacy implications**: neutral.

### Telegram Bot API
- **Why**: primary V1 intake and communication channel.
- **Where used**: main chat, workers chat, alerts chat.
- **Alternatives considered**: email, web upload.
- **Portability implications**: token/config driven.
- **Privacy implications**: intake trust boundary must be documented.

### SQLite
- **Why**: local-first, simple, reliable for single-household V1.
- **Where used**: structured receipt/purchase history and metadata.
- **Alternatives considered**: PostgreSQL.
- **Portability implications**: excellent single-file migration story.
- **Privacy implications**: strong local control.

### OCR Strategy (dual local OCR)
Two local OCR implementations will be designed and evaluated:

#### Apple-oriented OCR
- **Intent**: optimize for Mac mini M4 / Apple Silicon.
- **Candidate direction**: Apple Vision / native macOS-friendly OCR path.
- **Why**: potentially better performance and platform optimization on Apple hardware.
- **Portability implications**: lower portability; must be isolated behind an interface.

#### Portable OCR
- **Intent**: provide reliable local OCR across multiple machine types.
- **Candidate direction**: Tesseract as the initial portable baseline.
- **Why**: broad support, mature local deployment model.
- **Portability implications**: strong.

A dedicated OCR decision record must document the final selected implementations, tradeoffs, and fallback behavior.
