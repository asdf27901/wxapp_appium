# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/4/12 5:06 PM
# File: fileutils.py

import yaml
from typing import *


def get_file_object(filepath: str):
    """
    根据文件路径返回文件对象
    Args:
        filepath: 文件路径

    Returns:
        fileobject
    """
    return open(file=filepath, mode='r', encoding='utf8')


def read_small_file(fileObject):
    """
    拿到小文件对象，读取文件内容
    Args:
        fileObject: 小文件对象

    Returns: 返回文件内容
    """
    try:
        return fileObject.read()
    except Exception:
        raise Exception('something wrong')
    finally:
        fileObject.close()


def read_big_file(fileObject):
    """
    拿到大文件对象，读取文件内容
    Args:
        fileObject: 大文件对象

    Returns: 返回文件内容

    """
    try:
        return fileObject.readLines()
    except Exception:
        raise Exception('something wrong')
    finally:
        fileObject.close()


def get_yaml_data(filepath: str) -> Dict:
    """
    通过yaml文件路径，返回文件内容
    Args:
        filepath: 文件路径

    Returns:
        data: 以字典形式返回yaml文件内容

    """
    stream = get_file_object(filepath)
    data = yaml.safe_load(stream)
    stream.close()

    return data
