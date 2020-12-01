# coding: utf8
"""Module."""
# system imports
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *  # noqa: I201,F4

import pytest

from code_test import LOG
from code_test.main import PublishTools


def test_publish_texture():
    """Simple test for the publish_texture.

    This test show you, how we basically test the publish texture function.
    Of course we don't compare the result in this test in order not to influence the code test.
    """
    publish_tools = PublishTools()
    LOG.info(
        "Test : asset_name={asset_name}, task={task}, tex_assign_file={tex_assign_file}".format(
            asset_name=pytest.ASSET_NAME,
            task=pytest.TASK,
            tex_assign_file=pytest.TEX_ASSIGN_FILE,
        )
    )
    publish_tools.publish_texture()
