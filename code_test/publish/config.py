import os

current_folder = os.path.dirname(os.path.abspath(__file__))
root_repository = os.path.dirname(current_folder)
ROOT_PROJECT = os.path.join(root_repository, "project")
ASSET_NAME = "myAssetB"
TASK = "surfacing"
EXTENSION = "tx"
TEX_ASSIGN_FILE = os.path.join(ROOT_PROJECT, "Assets", ASSET_NAME, TASK, "work", "texture_assignment.yaml")
WORK_PATH = os.path.join(ROOT_PROJECT, "Assets", ASSET_NAME, TASK, "work/")
PUBLISH_PATH = os.path.join(ROOT_PROJECT, "Assets", ASSET_NAME, TASK, "publish/")
