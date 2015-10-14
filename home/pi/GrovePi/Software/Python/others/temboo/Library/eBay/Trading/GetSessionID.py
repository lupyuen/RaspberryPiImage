# -*- coding: utf-8 -*-

###############################################################################
#
# GetSessionID
# Generates an authorization URL that an application can use to complete the first step in the authentication process.
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

class GetSessionID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSessionID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSessionID, self).__init__(temboo_session, '/Library/eBay/Trading/GetSessionID')


    def new_input_set(self):
        return GetSessionIDInputSet()

    def _make_result_set(self, result, path):
        return GetSessionIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSessionIDChoreographyExecution(session, exec_id, path)

class GetSessionIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSessionID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(GetSessionIDInputSet, self)._set_input('AppID', value)
    def set_CertID(self, value):
        """
        Set the value of the CertID input for this Choreo. ((required, string) The certificate that authenticates the application when making API calls.)
        """
        super(GetSessionIDInputSet, self)._set_input('CertID', value)
    def set_DevID(self, value):
        """
        Set the value of the DevID input for this Choreo. ((required, string) The unique identifier for the developer's account.)
        """
        super(GetSessionIDInputSet, self)._set_input('DevID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetSessionIDInputSet, self)._set_input('ResponseFormat', value)
    def set_RuName(self, value):
        """
        Set the value of the RuName input for this Choreo. ((required, string) Your application's RuName which identifies your application to eBay.)
        """
        super(GetSessionIDInputSet, self)._set_input('RuName', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetSessionIDInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetSessionIDInputSet, self)._set_input('SiteID', value)

class GetSessionIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSessionID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)
    def get_AuthorizationURL(self):
        """
        Retrieve the value for the "AuthorizationURL" output from this Choreo execution. ((string) The URL that you can send the user to so that they can sign-in and approve the user consent form.)
        """
        return self._output.get('AuthorizationURL', None)
    def get_SessionID(self):
        """
        Retrieve the value for the "SessionID" output from this Choreo execution. ((string) The SessionID returned from eBay. This gets passed to the FetchToken Choreo after the user authorizes the request.)
        """
        return self._output.get('SessionID', None)

class GetSessionIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSessionIDResultSet(response, path)
