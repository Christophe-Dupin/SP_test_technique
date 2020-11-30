    """All constants for the publish tools class."""
    
import os

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
ROOT_REPOSITORY = os.path.dirname(CURRENT_FOLDER)
ROOT_PROJECT = os.path.join(ROOT_REPOSITORY, "project")
ASSET_NAME = "myAssetB"
TASK = "surfacing"
CONTEXT = "Assets"
EXTENSION = "tx"
ASSIGNMENT_FILE = "texture_assignment.yaml" 
TEX_ASSIGN_FILE = os.path.join(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, "work", "texture_assignment.yaml")
TEX_PUBLISH_ASSIGN_FILE = os.path.join(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, "publish", "texture_assignment.yaml")
WORK_PATH = os.path.join(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, "work/")
PUBLISH_PATH = os.path.join(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, "publish/")
