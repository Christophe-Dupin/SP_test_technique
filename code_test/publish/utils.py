
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
        self.work_path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.work)
        self.publish_path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.publish)

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
        """Methode allow to check if the assignment file exist.

        :raises ValueError: Raise error if the file doesnt exist.
        :return: return the path of the assignement file.
        :rtype: str
        """
        if os.path.isfile(os.path.join(self.work_path, self.assignment)):
            return os.path.join(self.work_path, self.assignment)
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

    def get_files_name(self, files):
        """Methode to keep only the file name of the texture file.

        :param files: Yaml file fo the assignement texture.
        :type files: yaml
        :raises FileNotFoundError: Raise an error if the file doesn t exist
        :return: list of the texture file name
        :rtype: list
        """
        files_name = []
        for file in files.values():
            for i in file:
                if i.startswith(os.path.join(self.work_path)):
                    files_name.append(re.sub('^' + os.path.join(self.work_path), '', i))
                else:
                    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), i)
        return files_name
   
    def get_files_name_part(self, files):
        """[summary]

        :param files: [description]
        :type files: [type]
        :return: [description]
        :rtype: [type]
        """
        result = re.match(r"part[A-Z]+", files)
        if result:
            VERSION = "001"
            return "asset_{}_texture_{}_v{}.{}".format(self.asset_name, result.group(0), VERSION, self.extension)

    def get_name_for_publish_texture_file(self):
        pass

    def move_and_rename_file(self, files):
        directory = os.listdir(self.work_path)
        for file in directory:
            if file in files:
                shutil.copy("{}{}".format(self.work_path, file), "{}{}".format(self.publish_path, file))
                dst_file = os.path.join(self.publish_path, file)
                new_dst_file_name = os.path.join(self.publish_path, files(file))
                os.rename(dst_file, new_dst_file_name)



