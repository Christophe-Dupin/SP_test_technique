
""" Class allow to publishTexture. """
import os
import errno 
import re
import yaml


class PublishTools:
    """Library of tools for publish."""

    def __init__(self, root_project, context, asset_name, task):
        """[summary]

        :param asset_name: Asset name like "myAssetB"
        :type asset_name: str
        :param task: Task name like "surfacing"
        :type task: str
        """
        self.asset_name = asset_name
        self.task = task
        self.root_project = root_project
        self.context = context
        self.work = "work/"
        self.publish = "publish/"
        self.assignment = "texture_assignment.yaml"
        self.work_path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.work)

    def get_work_file_directory_from_asset(self):
        """Methode to get the workFile directory of the asset.

        :raises FileNotFoundError: If direcotry dosn't exist raise an error.
        :return: the path of the directory
        :rtype: str
        """
        path = os.path.join(self.work_path)
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    def get_texture_assignement_yaml_file(self):
        """[summary]

        :raises ValueError: [description]
        :return: [description]
        :rtype: [type]
        """
        if os.path.isfile(os.path.join(self.work_path, self.assignment)):
            return os.path.join(self.work_path, self.assignment)
        else:
            raise ValueError
  
    def get_use_textures_from_yaml(self, tex_assign_file):
        files_name = []
        for file in tex_assign_file.values():
            for name in file:
                if name.startswith(os.path.join(self.context, self.asset_name, self.task, self.work)):
                    files_name.append(re.sub('^' + os.path.join(self.context, self.asset_name, self.task, self.work), '', name))
                else:
                    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), name)
        return files_name

    def get_files_name_part(self, files):
        pass

    def get_name_for_publish_texture_file(self):
        pass

    def generate_yaml_for_publish_file(self, task):
        pass

