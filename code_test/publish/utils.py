
""" Class allow to publishTexture. """
import os
import errno
import re
import yaml
import shutil


class PublishTools:
    """Library of tools for publish."""

    def __init__(self, root_project, context, asset_name, task, extension):
        """PublishTools is a class for toolbox to publish texture file.

        :param asset_name: Asset name like "myAssetB"
        :type asset_name: str
        :param task: Task name like "surfacing"
        :type task: str
        """
        self.asset_name = asset_name
        self.task = task
        self.root_project = root_project
        self.context = context
        self.extension = extension
        self.work = "work/"
        self.publish = "publish/"
        self.assignment = "texture_assignment.yaml"
        self.publish_path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.publish)

    def get_work_file_directory_from_asset(self):
        """Methode to get the workFile directory of the asset.

        :raises FileNotFoundError: If direcotry dosn't exist raise an error.
        :return: the path of the directory
        :rtype: str
        """
        path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.work)
        if os.path.exists(path):
            return path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    def get_texture_assignement_yaml_file(self, location):
        """Methode to check if the yaml file exist in the good location.

        :param location: path of the work folder of the asset use get_work_file_directory method.
        :type location: PublishTools object
        :raises ValueError: if yaml doesn t exist raise a value error
        :return: path of the yaml file
        :rtype: str
        """
        if os.path.isfile(os.path.join(location, self.assignment)):
            return os.path.join(location, self.assignment)
        else:
            raise ValueError

    def get_use_textures_from_yaml(self, tex_assign_file):
        """Methode to get all the texture assign.

        :param tex_assign_file: yaml file for the asset
        :type tex_assign_file: yaml
        :raises FileNotFoundError: Raise error if the file doesnt exist
        :return: A dictionnary with the usefull texture
        :rtype: dict
        """
        if os.path.exists(tex_assign_file):
            with open(tex_assign_file) as file:
                return yaml.load(file, Loader=yaml.FullLoader)
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), tex_assign_file)

    def get_only_files_name(self, textures):
        """Methode to return only file texture file name.

        :param textures: textures files find inside the yaml
        :type textures: dict
        :return: only the path of the texture file
        :rtype: str
        """
        files_name = []
        for file in textures.values():
            for i in file:
                if i.startswith(os.path.join(self.context, self.asset_name, self.task, self.work)):
                    files_name.append(re.sub('^' + os.path.join(self.context, self.asset_name, self.task, self.work), '', i))
        return files_name

    def set_name_for_publish_file(self, files):
        """Set the correct publish file name for the texture file.

        :param files: Should short namefor file texture
        :type files: str
        :return: good texture name to respect nomenclatura
        :rtype: str
        """
        result = re.match(r"part[A-Z]+", files)
        if result:
            VERSION = "001"
            return "asset_{}_texture_{}_v{}.{}".format(self.asset_name, result.group(0), VERSION, self.extension)

    def move_and_rename_file(self, location, files):
        """Methode to all to move and rename file from work folder to the publish folder

        :param location: work directory of texture files
        :type location: str
        :param files: contain only the texture file name use in the scene 
        :type files: list
        """
        directory = os.listdir(location)
        for file in directory:
            if file in files:
                shutil.copy("{}{}".format(location, file), "{}{}".format(self.publish_path, file))
                dst_file = os.path.join(self.publish_path, file)
                new_dst_file_name = os.path.join(self.publish_path, self.set_name_for_publish_file(file))
                os.rename(dst_file, new_dst_file_name)



