# -*- coding: utf-8 -*-

###############################################################################
#
# Put
# Generates a HTTP PUT request.
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

class Put(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Put Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Put, self).__init__(temboo_session, '/Library/Utilities/HTTP/Put')


    def new_input_set(self):
        return PutInputSet()

    def _make_result_set(self, result, path):
        return PutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutChoreographyExecution(session, exec_id, path)

class PutInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Put
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestBody(self, value):
        """
        Set the value of the RequestBody input for this Choreo. ((optional, multiline) The request body for the PUT request.)
        """
        super(PutInputSet, self)._set_input('RequestBody', value)
    def set_Debug(self, value):
        """
        Set the value of the Debug input for this Choreo. ((optional, boolean) When set to "true", the HTTP debug log will be returned.)
        """
        super(PutInputSet, self)._set_input('Debug', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) A valid password. This is used if the request required basic authentication.)
        """
        super(PutInputSet, self)._set_input('Password', value)
    def set_RequestHeaders(self, value):
        """
        Set the value of the RequestHeaders input for this Choreo. ((optional, json) A JSON object containing up to 10 key/value pairs that will be mapped to the HTTP request headers.)
        """
        super(PutInputSet, self)._set_input('RequestHeaders', value)
    def set_RequestParameters(self, value):
        """
        Set the value of the RequestParameters input for this Choreo. ((optional, json) A JSON object containing up to 10 key/value pairs that will be mapped to the url string as HTTP parameters.)
        """
        super(PutInputSet, self)._set_input('RequestParameters', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The base URL for the request (including http:// or https://).)
        """
        super(PutInputSet, self)._set_input('URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) A valid username. This is used if the request required basic authentication.)
        """
        super(PutInputSet, self)._set_input('Username', value)

class PutResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Put Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_HTTPLog(self):
        """
        Retrieve the value for the "HTTPLog" output from this Choreo execution. ((string) A debug log for the http request that was sent. This is only returned when Debug is set to "true".)
        """
        return self._output.get('HTTPLog', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the server.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code.)
        """
        return self._output.get('ResponseStatusCode', None)

class PutChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutResultSet(response, path)
