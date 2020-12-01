from code_test.publish.tools import FilesManager

from code_test.config import ASSET_NAME, CONTEXT, EXTENSION, ROOT_PROJECT, TASK
files_manager = FilesManager(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)


def test_get_file_directory_from_asset():
    step = ["work/", "publish/"]
    path = files_manager.get_file_directory_from_asset(step)
    assert path == "/Users/christophedupin/Documents/projects/repos/testSuperprod/code_test_a_cdupin/project/Assets/myAssetB/surfacing/work/"


def test_get_only_files_name():
    texture = {'texture_used': ['Assets/myAssetB/surfacing/work/partA_testA.tx', 'Assets/myAssetB/surfacing/work/partB_003.tx', 'Assets/myAssetB/surfacing/work/partC_001.tx']}
    files_names = files_manager.get_only_files_name(texture)
    assert type(files_names) == dict
    assert files_names.keys() == ['texture_publish']
