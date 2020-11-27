"""Class allow to test methodes from PublishTools Class."""
import os 

from code_test.publish.utils import PublishTools
from code_test.config import ASSET_NAME, TASK, ROOT_PROJECT, CONTEXT,TEX_ASSIGN_FILE


class TestPublishTools:

    def test_get_work_file_directory_from_asset(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK)
        path = publish_tools.get_work_file_directory_from_asset()
        assert path == "/Users/christophedupin/Documents/projects/repos/testSuperprod/code_test_a_cdupin/project/Assets/myAssetB/surfacing/work/"
    
    def test_get_texure_assignement_yaml_file(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK)
        file = publish_tools.get_texture_assignement_yaml_file()
        assert file

    def test_use_texture_from_yaml(self):
        publish_tools = PublishTools(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK)
        yaml = publish.get_texture_assignement_yaml_file(TEX_ASSIGN_FILE)