# coding: utf8
"""conftest module for pytest."""
# system imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import *  # noqa: I201,F4
import os
import sys

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
