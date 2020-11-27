# coding: utf8
"""The code_test main module."""
# system imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from builtins import *  # noqa: I201,F

from code_test.config import ASSET_NAME, CONTEXT, EXTENSION, ROOT_PROJECT, TASK
from code_test.publish.utils import PublishTools


def publish_texture():
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
    # Instanciate PublishTools Class
    publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)
    # Get work directory of the texturefile for a specific asset
    get_work_file_directory = publish_tools.get_work_file_directory_from_asset()
    # Get path of of the texture assignement yaml file
    get_texture_assignement_yaml = publish_tools.get_texture_assignement_yaml_file(get_work_file_directory)
    # Get use textures in the yaml file
    get_use_textures_from_yaml = publish_tools.get_use_textures_from_yaml(get_texture_assignement_yaml)
    # Keep only shot name of the textures files
    get_only_files_name = publish_tools.get_only_files_name(get_use_textures_from_yaml)
    # Copy selected textures files from work directory to publish directory and rename with publish nomenclatura
    publish_tools.move_and_rename_file(get_work_file_directory, get_only_files_name)

    # result = {"published": [], "already-published": [], "failed": []}

    # LOG.info("result : {}".format(result))

    # return result


if __name__ == "__main__":
    a = publish_texture()
