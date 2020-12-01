# coding: utf8
"""conftest module for pytest."""
# system imports
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os
import sys
from builtins import *  # noqa: I201,F4

import pytest


def pytest_configure():
    """Register our custom variables & decorators required to perform the tests."""
    current_folder = os.path.dirname(os.path.abspath(__file__))
    root_repository = os.path.dirname(current_folder)

    # Add code_test to PYTHONPATH
    sys.path.append(root_repository)
    # Define var
    pytest.ROOT_PROJECT = os.path.join(root_repository, "project")
    pytest.ASSET_NAME = "myAssetB"
    pytest.TASK = "surfacing"
    pytest.TEX_ASSIGN_FILE = os.path.join(
        pytest.ROOT_PROJECT,
        "Assets",
        pytest.ASSET_NAME,
        pytest.TASK,
        "work",
        "texture_assignment.yaml",
    )
