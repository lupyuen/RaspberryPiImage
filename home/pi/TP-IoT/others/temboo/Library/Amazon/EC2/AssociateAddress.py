# -*- coding: utf-8 -*-

###############################################################################
#
# AssociateAddress
# Associates an Elastic IP address with an instance or a network interface.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AssociateAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AssociateAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AssociateAddress, self).__init__(temboo_session, '/Library/Amazon/EC2/AssociateAddress')


    def new_input_set(self):
        return AssociateAddressInputSet()

    def _make_result_set(self, result, path):
        return AssociateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssociateAddressChoreographyExecution(session, exec_id, path)

class AssociateAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AssociateAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(AssociateAddressInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(AssociateAddressInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AllocationId(self, value):
        """
        Set the value of the AllocationId input for this Choreo. ((optional, string) [EC2-VPC] The allocation ID.  Required for a VPC.)
        """
        super(AssociateAddressInputSet, self)._set_input('AllocationId', value)
    def set_AllowReassociation(self, value):
        """
        Set the value of the AllowReassociation input for this Choreo. ((optional, string) [EC2-VPC] Allows an Elastic IP address that is already associated with an instance or network interface to be re-associated with the specified instance or network interface. False if not specified.)
        """
        super(AssociateAddressInputSet, self)._set_input('AllowReassociation', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((conditional, string) The ID of the instance.  Required for EC2-Classic. For a VPC, you can specify either an instance ID or a network interface ID, but not both.)
        """
        super(AssociateAddressInputSet, self)._set_input('InstanceId', value)
    def set_NetworkInterfaceId(self, value):
        """
        Set the value of the NetworkInterfaceId input for this Choreo. ((optional, string) [EC2-VPC] The ID of the network interface. Association fails when specifying an instance ID unless exactly one interface is attached.)
        """
        super(AssociateAddressInputSet, self)._set_input('NetworkInterfaceId', value)
    def set_PrivateIpAddress(self, value):
        """
        Set the value of the PrivateIpAddress input for this Choreo. ((optional, string) [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If nothing is specified, the Elastic IP address is associated with the primary private IP address.)
        """
        super(AssociateAddressInputSet, self)._set_input('PrivateIpAddress', value)
    def set_PublicIp(self, value):
        """
        Set the value of the PublicIp input for this Choreo. ((conditional, string) The Elastic IP address.)
        """
        super(AssociateAddressInputSet, self)._set_input('PublicIp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(AssociateAddressInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(AssociateAddressInputSet, self)._set_input('UserRegion', value)

class AssociateAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AssociateAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AssociateAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AssociateAddressResultSet(response, path)
