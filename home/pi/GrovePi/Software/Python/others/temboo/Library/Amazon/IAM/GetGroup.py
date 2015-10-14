# -*- coding: utf-8 -*-

###############################################################################
#
# GetGroup
# Returns a list of users that are in the specified group.
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

class GetGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetGroup, self).__init__(temboo_session, '/Library/Amazon/IAM/GetGroup')


    def new_input_set(self):
        return GetGroupInputSet()

    def _make_result_set(self, result, path):
        return GetGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetGroupChoreographyExecution(session, exec_id, path)

class GetGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetGroup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetGroupInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetGroupInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((required, string) The name of the group to return.)
        """
        super(GetGroupInputSet, self)._set_input('GroupName', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, string) Used for pagination to indicate the starting point of the results to return.)
        """
        super(GetGroupInputSet, self)._set_input('Marker', value)
    def set_MaxItems(self, value):
        """
        Set the value of the MaxItems input for this Choreo. ((optional, integer) Used for pagination to limit the number of results returned. Defaults to 100.)
        """
        super(GetGroupInputSet, self)._set_input('MaxItems', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetGroupInputSet, self)._set_input('ResponseFormat', value)

class GetGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetGroupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetGroupResultSet(response, path)
