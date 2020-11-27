
""" Class allow to publishTexture. """
import yaml


class PublishTools:
    """Library of tools for publish."""
    
    def __init__(self,asset_name,task):
        """[summary]

        :param asset_name: Asset name like "myAssetB"
        :type asset_name: str
        :param task: Task name like "surfacing"
        :type task: str
        """
        self.asset_name = asset_name
        self.task = task
    
    def get_work_file_directory_from_asset(self):
        pass

    def get_texture_assignement_yaml_file(self):
        pass

    def get_use_textures_from_yaml(self,tex_assign_file):
        pass
            
    def get_files_name_part(self,files):
        pass

    def get_name_for_publish_texture_file(self):
        pass

    def generate_yaml_for_publish_file(self,task):
        pass

