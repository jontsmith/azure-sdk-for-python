# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FindSimilarRequest(Model):
    """Request body for find similar operation.

    All required parameters must be populated in order to send to Azure.

    :param face_id: Required. FaceId of the query face. User needs to call
     Face - Detect first to get a valid faceId. Note that this faceId is not
     persisted and will expire 24 hours after the detection call
    :type face_id: str
    :param face_list_id: An existing user-specified unique candidate face
     list, created in Face List - Create a Face List. Face list contains a set
     of persistedFaceIds which are persisted and will never expire. Parameter
     faceListId, largeFaceListId and faceIds should not be provided at the same
     time.
    :type face_list_id: str
    :param large_face_list_id: An existing user-specified unique candidate
     large face list, created in LargeFaceList - Create. Large face list
     contains a set of persistedFaceIds which are persisted and will never
     expire. Parameter faceListId, largeFaceListId and faceIds should not be
     provided at the same time.
    :type large_face_list_id: str
    :param face_ids: An array of candidate faceIds. All of them are created by
     Face - Detect and the faceIds will expire 24 hours after the detection
     call. The number of faceIds is limited to 1000. Parameter faceListId,
     largeFaceListId and faceIds should not be provided at the same time.
    :type face_ids: list[str]
    :param max_num_of_candidates_returned: The number of top similar faces
     returned. The valid range is [1, 1000]. Default value: 20 .
    :type max_num_of_candidates_returned: int
    :param mode: Similar face searching mode. It can be "matchPerson" or
     "matchFace". Possible values include: 'matchPerson', 'matchFace'. Default
     value: "matchPerson" .
    :type mode: str or
     ~azure.cognitiveservices.vision.face.models.FindSimilarMatchMode
    """

    _validation = {
        'face_id': {'required': True},
        'face_list_id': {'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
        'large_face_list_id': {'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
        'face_ids': {'max_items': 1000},
        'max_num_of_candidates_returned': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'face_list_id': {'key': 'faceListId', 'type': 'str'},
        'large_face_list_id': {'key': 'largeFaceListId', 'type': 'str'},
        'face_ids': {'key': 'faceIds', 'type': '[str]'},
        'max_num_of_candidates_returned': {'key': 'maxNumOfCandidatesReturned', 'type': 'int'},
        'mode': {'key': 'mode', 'type': 'FindSimilarMatchMode'},
    }

    def __init__(self, **kwargs):
        super(FindSimilarRequest, self).__init__(**kwargs)
        self.face_id = kwargs.get('face_id', None)
        self.face_list_id = kwargs.get('face_list_id', None)
        self.large_face_list_id = kwargs.get('large_face_list_id', None)
        self.face_ids = kwargs.get('face_ids', None)
        self.max_num_of_candidates_returned = kwargs.get('max_num_of_candidates_returned', 20)
        self.mode = kwargs.get('mode', "matchPerson")