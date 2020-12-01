"""Class allow to test methodes from PublishTools Class."""
import os

import pytest
import yaml

from code_test.config import (
    ASSET_NAME,
    ASSIGNMENT_FILE,
    CONTEXT,
    EXTENSION,
    ROOT_PROJECT,
    TASK,
    TEX_ASSIGN_FILE,
)
from code_test.publish.tools import FilesManager, YamlManager

files_manager = FilesManager(
    ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION
)
asset_work_directory = files_manager.get_file_directory_from_asset(
    files_manager.work
)
yaml_manager = YamlManager(ASSIGNMENT_FILE)
yaml_work_file = yaml_manager.get_yaml_file(asset_work_directory)


def test_get_texure_assignement_yaml_file():
    location = "/Users/christophedupin/Documents/projects/repos/testSuperprod/code_test_a_cdupin/project/Assets/myAssetB/surfacing/work/"
    publish_tools = YamlManager(ASSIGNMENT_FILE)
    file = publish_tools.get_yaml_file(location)
    assert (
        file
        == "/Users/christophedupin/Documents/projects/repos/testSuperprod/code_test_a_cdupin/project/Assets/myAssetB/surfacing/work/texture_assignment.yaml"
    )


def test_get_info_from_yaml(monkeypatch):
    def mock_yaml_load(*args, **kwargs):
        return {
            "texture_used": [
                "Assets/myAssetB/surfacing/work/partA_testA.tx",
                "Assets/myAssetB/surfacing/work/partB_003.tx",
                "Assets/myAssetB/surfacing/work/partC_001.tx",
            ]
        }

    monkeypatch.setattr(yaml, "load", mock_yaml_load)
    assert yaml_manager.get_info_from_yaml(yaml_work_file) == {
        "texture_used": [
            "Assets/myAssetB/surfacing/work/partA_testA.tx",
            "Assets/myAssetB/surfacing/work/partB_003.tx",
            "Assets/myAssetB/surfacing/work/partC_001.tx",
        ]
    }
