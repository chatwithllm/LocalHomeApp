from local_home_app.common.runtime_errors import ConfigurationError, LocalHomeAppError


def test_configuration_error_is_application_error() -> None:
    assert issubclass(ConfigurationError, LocalHomeAppError)
