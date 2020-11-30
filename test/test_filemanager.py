from code_test.publish.tools import FilesManager

from code_test.config import ASSET_NAME, ASSIGNMENT_FILE, CONTEXT, EXTENSION, ROOT_PROJECT, TASK
files_manager = FilesManager(ROOT_PROJECT, CONTEXT, ASSET_NAME, TASK, EXTENSION)

def get_file_directory_from_asset(step):
    step = 