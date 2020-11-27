# coding: utf8
"""The code_test main module."""
# system imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import *  # noqa: I201,F4
import yaml
import re
import os
import shutil
import errno
from code_test import LOG
from  code_test.publish.utils import PublishTools
from code_test.config import TEX_ASSIGN_FILE, ASSET_NAME, TASK, EXTENSION, ROOT_PROJECT, WORK_PATH, PUBLISH_PATH, CONTEXT


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
    # Init result
    publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)
    get_work_file_directory = publish_tools.get_work_file_directory_from_asset()
    get_texture_assignement_yaml = publish_tools.get_texture_assignement_yaml_file(get_work_file_directory)
    get_use_textures_from_yaml = publish_tools.get_use_textures_from_yaml(get_texture_assignement_yaml)
    get_only_files_name = publish_tools.get_only_files_name(get_use_textures_from_yaml)
    publish_tools.move_and_rename_file(get_work_file_directory, get_only_files_name)


    #result = {"published": [], "already-published": [], "failed": []}

    #LOG.info("result : {}".format(result))

    #return result


if __name__ == "__main__":
    publish_texture()

