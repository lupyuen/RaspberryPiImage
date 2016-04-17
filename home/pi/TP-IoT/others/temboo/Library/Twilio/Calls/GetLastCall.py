# -*- coding: utf-8 -*-

###############################################################################
#
# GetLastCall
# Retrieves the latest phone call made to or from the specified account.
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

class GetLastCall(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLastCall Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLastCall, self).__init__(temboo_session, '/Library/Twilio/Calls/GetLastCall')


    def new_input_set(self):
        return GetLastCallInputSet()

    def _make_result_set(self, result, path):
        return GetLastCallResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLastCallChoreographyExecution(session, exec_id, path)

class GetLastCallInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLastCall
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetLastCallInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetLastCallInputSet, self)._set_input('AuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLastCallInputSet, self)._set_input('ResponseFormat', value)

class GetLastCallResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLastCall Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetLastCallChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLastCallResultSet(response, path)
