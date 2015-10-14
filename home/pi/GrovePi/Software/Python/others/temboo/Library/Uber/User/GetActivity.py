# -*- coding: utf-8 -*-

###############################################################################
#
# GetActivity
# Returns information about a user's activity with Uber including pickup locations and times, dropoff locations and times, the distance of past requests, and information about which products were requested.
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

class GetActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetActivity, self).__init__(temboo_session, '/Library/Uber/User/GetActivity')


    def new_input_set(self):
        return GetActivityInputSet()

    def _make_result_set(self, result, path):
        return GetActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetActivityChoreographyExecution(session, exec_id, path)

class GetActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid Access Token retrieved during the OAuth process.)
        """
        super(GetActivityInputSet, self)._set_input('AccessToken', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of records returned in the response.)
        """
        super(GetActivityInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Returns results starting from the specified number.)
        """
        super(GetActivityInputSet, self)._set_input('Offset', value)

class GetActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Uber.)
        """
        return self._output.get('Response', None)

class GetActivityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetActivityResultSet(response, path)
