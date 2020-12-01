
""" Class allow to publishTexture. """
import errno
import os
import re
import shutil

import yaml

from code_test import LOG


class YamlManager:
    """Library for managing yaml file."""

    def __init__(self, assignment):
        """Allow to mange yaml file.

        :param assignment: name of the yaml file
        :type assignment: str
        """
        self.assignment = assignment

    def get_yaml_file(self, location):
        """Get the yaml file directory.

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
        """Get info from any yaml file

        :param file: path of the yaml file
        :type file: str
        :return: Python dict of yaml content
        :rtype: dict
        """
        with open(file) as files:
            return yaml.load(files, Loader=yaml.FullLoader)
    
    def update_yaml(self, file_path, data):
        """Update data in yaml file

        :param file_path: file path of the yaml file
        :type file_path: str
        :param data: Dictionnairy of the data to update
        :type data: dict
        :return: new yaml file
        :rtype: yaml
        """
        with open(file_path, 'w') as file:
            return yaml.dump(data, file)


class FilesManager:

    def __init__(self, root_project, context, asset_name, task, extension):
        """Allow to acces to several tools to manage Files.

        :param root_project: Define the path of the root project define in the config module
        :type root_project: str
        :param context: Define the context of the asset asset or shot for example
        :type context: str
        :param asset_name: Name of the asset for example myAssetB
        :type asset_name: str
        :param task: Define the task ofthe asset for example surfacing
        :type task: str
        :param extension: Define the extension of the textexture file here its tx
        :type extension: str
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
        """Get the file directory of any asset.

        :param step: You can choose work or publish directory
        :type step: str
        :raises FileNotFoundError: If the path diesnt exist raise an error
        :return: return the path of the asset
        :rtype: str
        """
        path = os.path.join(self.root_project, self.context, self.asset_name, self.task, step)
        if not os.path.exists(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
        LOG.info("Asset working directory : {}".format(path))
        return path

    def get_only_files_name(self, textures):
        """Get only the file name of any files, remove all the absolute path.

        :param textures: It's all the full path of a file 
        :type textures: str
        :return: dictionary of the file name
        :rtype: dict
        """
        files_name = []
        for file in textures.values():
            for i in file:
                LOG.info("Use texture for the asset: {}".format(i))
                if i.startswith(os.path.join(self.context, self.asset_name, self.task, self.work)):
                    files_name.append(re.sub('^' + os.path.join(self.context, self.asset_name, self.task, self.work), '', i))
        return {"texture_publish": files_name}

    def set_name_for_publish_file(self, files):
        """Set publish file name for the texture file.

        :param files: Should short name for file texture
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
        """Move and rename file.

        :param location: work directory is the source directory
        :type location: YamlManager
        :param files: shortt name of the files to move
        :type files: FilesManager
        :param publish: Get the already publish texture
        :type publish: YamlManager
        :return: Summary of what append in the method
        :rtype: dict
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