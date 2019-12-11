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

from .feature_support_request_py3 import FeatureSupportRequest


class AzureVMResourceFeatureSupportRequest(FeatureSupportRequest):
    """AzureResource(IaaS VM) Specific feature support request.

    All required parameters must be populated in order to send to Azure.

    :param feature_type: Required. Constant filled by server.
    :type feature_type: str
    :param vm_size: Size of the resource: VM size(A/D series etc) in case of
     IaasVM
    :type vm_size: str
    :param vm_sku: SKUs (Premium/Managed etc) in case of IaasVM
    :type vm_sku: str
    """

    _validation = {
        'feature_type': {'required': True},
    }

    _attribute_map = {
        'feature_type': {'key': 'featureType', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'vm_sku': {'key': 'vmSku', 'type': 'str'},
    }

    def __init__(self, *, vm_size: str=None, vm_sku: str=None, **kwargs) -> None:
        super(AzureVMResourceFeatureSupportRequest, self).__init__(**kwargs)
        self.vm_size = vm_size
        self.vm_sku = vm_sku
        self.feature_type = 'AzureVMResourceBackup'