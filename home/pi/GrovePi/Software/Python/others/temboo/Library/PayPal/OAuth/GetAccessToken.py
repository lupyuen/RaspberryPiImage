# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccessToken
# Retrieves an Access Token from PayPal.
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

class GetAccessToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccessToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAccessToken, self).__init__(temboo_session, '/Library/PayPal/OAuth/GetAccessToken')


    def new_input_set(self):
        return GetAccessTokenInputSet()

    def _make_result_set(self, result, path):
        return GetAccessTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccessTokenChoreographyExecution(session, exec_id, path)

class GetAccessTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccessToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by PayPal.)
        """
        super(GetAccessTokenInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by PayPal.)
        """
        super(GetAccessTokenInputSet, self)._set_input('ClientSecret', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) A space delimited list of resource URL endpoints that the token should have access for (i.e. https://api.paypal.com/v1/payments/.*).)
        """
        super(GetAccessTokenInputSet, self)._set_input('Scope', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Defaults to 0.)
        """
        super(GetAccessTokenInputSet, self)._set_input('UseSandbox', value)

class GetAccessTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccessToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((string) The access token retrieved from PayPal.)
        """
        return self._output.get('AccessToken', None)
    def get_Expires(self):
        """
        Retrieve the value for the "Expires" output from this Choreo execution. ((integer) The expiration time of the access token retrieved.)
        """
        return self._output.get('Expires', None)

class GetAccessTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAccessTokenResultSet(response, path)
