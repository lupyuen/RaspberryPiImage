# -*- coding: utf-8 -*-

###############################################################################
#
# GetEncodersCount
# Returns the count of users who have shortened a specified Bitly link.
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

class GetEncodersCount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEncodersCount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetEncodersCount, self).__init__(temboo_session, '/Library/Bitly/LinkMetrics/GetEncodersCount')


    def new_input_set(self):
        return GetEncodersCountInputSet()

    def _make_result_set(self, result, path):
        return GetEncodersCountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEncodersCountChoreographyExecution(session, exec_id, path)

class GetEncodersCountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEncodersCount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The OAuth access token provided by Bitly.)
        """
        super(GetEncodersCountInputSet, self)._set_input('AccessToken', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((required, string) A Bitly link.)
        """
        super(GetEncodersCountInputSet, self)._set_input('Link', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(GetEncodersCountInputSet, self)._set_input('ResponseFormat', value)

class GetEncodersCountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEncodersCount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetEncodersCountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetEncodersCountResultSet(response, path)
