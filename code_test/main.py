# coding: utf8
"""The code_test main module."""
# system imports

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *  # noqa: I201,F

from code_test.config import (
    ASSET_NAME,
    ASSIGNMENT_FILE,
    CONTEXT,
    EXTENSION,
    ROOT_PROJECT,
    TASK,
)
from code_test.publish.tools import FilesManager, YamlManager
import os
import re


class PublishTools:
    def publish_texture(self):
        """Publish the textures defined by the tex_assign_file."""

        # Instanciate FilesManager class
        files_manager = FilesManager(
            ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION
        )
        # Instanciate YamlManager class
        yaml_manager = YamlManager(ASSIGNMENT_FILE)
        # Get work directory for a specific asset
        asset_work_directory = files_manager.get_file_directory_from_asset(
            files_manager.work
        )
        # Get publish directory for a specific asset
        asset_publish_directory = files_manager.get_file_directory_from_asset(
            files_manager.publish
        )
        # Get path of of the work texture assignement yaml file
        yaml_work_file = yaml_manager.get_yaml_file(asset_work_directory)
        # Get path of of the publish texture assignement yaml file
        yaml_publish_file = yaml_manager.get_yaml_file(asset_publish_directory)
        # Get used textures in the work yaml file
        info_from_yaml_work_file = yaml_manager.get_info_from_yaml(
            yaml_work_file
        )
        # Keep only short name of the textures files
        only_files_name = files_manager.get_only_files_name(
            info_from_yaml_work_file
        )
        # Get texture which are already publish
        info_from_yaml_publish_file = yaml_manager.get_info_from_yaml(
            yaml_publish_file
        )
        # Copy selected textures files from work directory to publish directory and rename with publish nomenclatura
        publish = files_manager.move_and_rename_file(
            asset_work_directory, only_files_name, info_from_yaml_publish_file
        )
        # Update yaml with the published texture
        yaml_manager.update_yaml(yaml_publish_file, only_files_name)

        return publish


if __name__ == "__main__":

    publish_tools = PublishTools()
    publish_tools.publish_texture()
