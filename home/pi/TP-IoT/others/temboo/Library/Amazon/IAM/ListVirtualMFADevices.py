# -*- coding: utf-8 -*-

###############################################################################
#
# ListVirtualMFADevices
# Lists the virtual MFA devices under the AWS account.
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

class ListVirtualMFADevices(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListVirtualMFADevices Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListVirtualMFADevices, self).__init__(temboo_session, '/Library/Amazon/IAM/ListVirtualMFADevices')


    def new_input_set(self):
        return ListVirtualMFADevicesInputSet()

    def _make_result_set(self, result, path):
        return ListVirtualMFADevicesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListVirtualMFADevicesChoreographyExecution(session, exec_id, path)

class ListVirtualMFADevicesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListVirtualMFADevices
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AssignmentStatus(self, value):
        """
        Set the value of the AssignmentStatus input for this Choreo. ((optional, string) Filters by the whether the device is assigned or unassigned to a specific user. Valid values: "Unassigned", "Assigned" or "Any" (default - both assigned and unassigned devices).)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('AssignmentStatus', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, string) Used for pagination to indicate the starting point of the results to return.)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('Marker', value)
    def set_MaxItems(self, value):
        """
        Set the value of the MaxItems input for this Choreo. ((optional, integer) Used for pagination to limit the number of results returned. Defaults to 100.)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('MaxItems', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListVirtualMFADevicesInputSet, self)._set_input('ResponseFormat', value)

class ListVirtualMFADevicesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListVirtualMFADevices Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ListVirtualMFADevicesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListVirtualMFADevicesResultSet(response, path)
