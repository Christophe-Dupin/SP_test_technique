"""The code_test package."""
import logging

# Initialize the LOG for the entire module
FORMAT = "%(asctime)s|%(name)s|%(filename)s|l.%(lineno)s|%(levelname)8s| %(message)s"
file_formatter = logging.Formatter(FORMAT)
handler = logging.StreamHandler()
handler.setFormatter(file_formatter)
LOG = logging.getLogger("code_test_a")
LOG.addHandler(handler)
LOG.setLevel(logging.INFO)
