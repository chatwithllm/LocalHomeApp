import logging

from local_home_app.logging.logging_configuration import configure_logging


def test_configure_logging_sets_root_level() -> None:
    configure_logging("INFO")
    assert logging.getLogger().level in (logging.INFO, logging.NOTSET)
