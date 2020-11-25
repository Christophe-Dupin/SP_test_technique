# coding: utf8
"""The code_test main module."""
# system imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import *  # noqa: I201,F4


from code_test import LOG


def publish_texture(asset_name, task, tex_assign_file):
    """Publish the textures defined by the tex_assign_file.

    :param asset_name: Asset name like "myAssetB"
    :type asset_name: str
    :param task: Task name like "surfacing"
    :type task: str
    :param tex_assign_file: Path to the texture_assignment.yaml file
    :type tex_assign_file: str
    :return: A resume of the publish, like {"published": [], "already-published": [], "failed": []}
    :rtype: dict
    """
    # Init result
    result = {"published": [], "already-published": [], "failed": []}

    LOG.info("result : {}".format(result))

    return result
