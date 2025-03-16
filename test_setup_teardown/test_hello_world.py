import logging
import pytest


class TestHelloWorld:

    @classmethod
    def setup_class(cls):
        logging.info("Inside method 'setup_class'")
        pass

    @classmethod
    def teardown_class(cls):
        logging.info("Inside method 'teardown_class'")
        pass

    def setup_method(self):
        logging.info("Inside method 'setup_method'")

    def teardown_method(self):
        logging.info("Inside method 'teardown_method'")

    def test_sample_1(self) -> None:
        logging.info("Inside sample_1 test method")

    def test_sample_2(self) -> None:
        logging.info("Inside sample_2 test method")

