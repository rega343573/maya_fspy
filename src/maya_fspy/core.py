"""
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
"""

import json
import sys

import maya.cmds as cmds


def create_camera_and_plane(json_path, image_path):
    """
    Create a camera and image plane given a json with data generated from fSpy.
    :param str json_path: full path to the json.
    :param str image_path: full or relative path to the image to use.
    :return: A dictionary containing the newly created nodes in the following format:
            {'camera': (camera_transform, camera_shape),
            'image_plane': (image_transform, image_shape),
            'root': group}
    :rtype: dict
    """
    # Python 2/3 compatible file reading
    if sys.version_info[0] >= 3:
        with open(json_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        with open(json_path) as json_file:
            data = json.load(json_file)

    # Group for all the created items.
    group = cmds.group(empty=True, name='projected_camera_grp_001')

    # Applying the matrix transformations onto a camera
    matrix_rows = [['in00', 'in10', 'in20', 'in30'],
                   ['in01', 'in11', 'in21', 'in31'],
                   ['in02', 'in12', 'in22', 'in32'],
                   ['in03', 'in13', 'in23', 'in33']]

    # Creating a camera, 4x4 matrix and decompose-matrix, then setting up the connections.
    camera_transform = cmds.camera()[0]
    camera_shape = cmds.listRelatives(camera_transform, shapes=True)[0]
    cmds.parent(camera_transform, group)
    matrix = cmds.createNode('fourByFourMatrix', name='cameraTransform_fourByFourMatrix')
    decompose_matrix = cmds.createNode('decomposeMatrix', name='cameraTransform_decomposeMatrix')
    cmds.connectAttr('{0}.output'.format(matrix), '{0}.inputMatrix'.format(decompose_matrix))
    cmds.connectAttr('{0}.outputTranslate'.format(decompose_matrix), '{0}.translate'.format(camera_transform))
    cmds.connectAttr('{0}.outputRotate'.format(decompose_matrix), '{0}.rotate'.format(camera_transform))

    # Setting the matrix attrs onto the 4x4 matrix.
    for i, matrix_list in enumerate(data['cameraTransform']['rows']):
        for value, attr in zip(matrix_list, matrix_rows[i]):
            cmds.setAttr('{0}.{1}'.format(matrix, attr), value)

    # creating an image plane for the camera
    image_plane_result = cmds.imagePlane(camera=camera_shape)
    image_transform = image_plane_result[0]
    image_shape = image_plane_result[1]
    cmds.setAttr('{0}.imageName'.format(image_shape), image_path, type='string')

    # Cleanup
    cmds.delete([matrix, decompose_matrix])
    for attr in ['translate', 'rotate', 'scale']:
        for ax in ['X', 'Y', 'Z']:
            cmds.setAttr('{0}.{1}{2}'.format(camera_transform, attr, ax), lock=True)
            cmds.setAttr('{0}.{1}{2}'.format(image_transform, attr, ax), lock=True)

    # Returning all the newly created items in case someone wants to grab and use them later.
    return {'camera': (camera_transform, camera_shape),
            'image_plane': (image_transform, image_shape),
            'root': group}
