
""" Class allow to publishTexture. """
import errno
import os
import re
import shutil

import yaml

from code_test import LOG


class YamlManager:
    """Library of tools for publish."""

    def __init__(self, assignment):
        """PublishTools is a class for toolbox to publish texture file.

        :param asset_name: Asset name like "myAssetB"
        :type asset_name: str
        :param task: Task name like "surfacing"
        :type task: str
        """
        self.assignment = assignment

    def get_yaml_file(self, location):
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
            LOG.error("yaml file doesnt exist please contact your td pipeline")

    def get_info_from_yaml(self, file):
        """Methode to get all the texture assign.

        :param tex_assign_file: yaml file for the asset
        :type tex_assign_file: yaml
        :raises FileNotFoundError: Raise error if the file doesnt exist
        :return: A dictionnary with the usefull texture
        :rtype: dict
        """
        with open(file) as files:
            return yaml.load(files, Loader=yaml.FullLoader)
    
    def update_yaml(self, file_path, data):
        with open(file_path, 'w') as file:
            return yaml.dump(data, file)


class FilesManager:

    def __init__(self, root_project, context, asset_name, task, extension):
        """PublishTools is a class for toolbox to publish texture file.

        :param asset_name: Asset name like "myAssetB"
        :type asset_name: str
        :param task: Task name like "surfacing"
        :type task: str
        """
        self.context = context
        self.root_project = root_project
        self.asset_name = asset_name
        self.task = task
        self.extension = extension
        self.work = "work/"
        self.publish = "publish/"
        self.publish_path = os.path.join(self.root_project, self.context, self.asset_name, self.task, self.publish)

    def get_file_directory_from_asset(self, step):
        """Methode to get the workFile directory of the asset.

        :raises FileNotFoundError: If direcotry dosn't exist raise an error.
        :return: the path of the directory
        :rtype: str
        """
        path = os.path.join(self.root_project, self.context, self.asset_name, self.task, step)
        if not os.path.exists(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
        LOG.info("Asset working directory : {}".format(path))
        return path

    def get_only_files_name(self, textures):
        """Methode to return only file texture file name.

        :param textures: textures files find inside the yaml
        :type textures: dict
        :return: only the name of the texture file without the full path
        :rtype: str
        """
        files_name = []
        for file in textures.values():
            for i in file:
                LOG.info("Use texture for the asset: {}".format(i))
                if i.startswith(os.path.join(self.context, self.asset_name, self.task, self.work)):
                    files_name.append(re.sub('^' + os.path.join(self.context, self.asset_name, self.task, self.work), '', i))
        return {"texture_publish": files_name}

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
        else:
            LOG.error("Work File doesnt match the nomenclatura please check in the wiki")
    
    def move_and_rename_file(self, location, files, publish):
        """Methode to all to move and rename file from work folder to the publish folder

        :param location: work directory of texture files
        :type location: str
        :param files: contain only the texture file name use in the scene
        :type files: list
        """
        result = {"published": [], "already-published": [], "failed": []}
        for x in files["texture_publish"]:
            if publish["texture_publish"] is None:
                shutil.copy("{}{}".format(location, x), "{}{}".format(self.publish_path, x))
                dst_file = os.path.join(self.publish_path, x)
                new_dst_file_name = os.path.join(self.publish_path, self.set_name_for_publish_file(x))
                os.rename(dst_file, new_dst_file_name)
                result["published"].append(x)
            elif x in publish["texture_publish"]:
                result["already-published"].append(x)
            else:
                result["failed"].append(x)
        LOG.info("result : {}".format(result))
        return result