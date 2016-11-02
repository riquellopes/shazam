import logging
import pytest


@pytest.fixture(scope="session", autouse=True)
def resource_a_setup():
    logging.disable(logging.CRITICAL)
