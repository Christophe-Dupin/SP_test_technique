"""Class allow to test methodes from PublishTools Class."""
import os

import yaml

from code_test.config import (ASSET_NAME, CONTEXT, EXTENSION, ROOT_PROJECT,
                              TASK, TEX_ASSIGN_FILE)
from code_test.publish.utils import PublishTools


class TestPublishTools:

    def test_get_work_file_directory_from_asset(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)
        path = publish_tools.get_work_file_directory_from_asset()
        assert path == "/Users/christophedupin/Documents/projects/repos/testSuperprod/code_test_a_cdupin/project/Assets/myAssetB/surfacing/work/"
    
    def test_get_texure_assignement_yaml_file(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)
        file = publish_tools.get_texture_assignement_yaml_file()
        assert file

    def test_get_use_textures_from_yam(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)
        file = publish_tools.get_use_textures_from_yaml(TEX_ASSIGN_FILE)
        assert isinstance(file, dict)
