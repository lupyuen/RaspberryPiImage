# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateNumber
# Updates the callback details for the specified number.
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

class UpdateNumber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateNumber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateNumber, self).__init__(temboo_session, '/Library/Nexmo/Account/UpdateNumber')


    def new_input_set(self):
        return UpdateNumberInputSet()

    def _make_result_set(self, result, path):
        return UpdateNumberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateNumberChoreographyExecution(session, exec_id, path)

class UpdateNumberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateNumber
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(UpdateNumberInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(UpdateNumberInputSet, self)._set_input('APISecret', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((optional, string) Mobile originated Callback URL.)
        """
        super(UpdateNumberInputSet, self)._set_input('CallbackURL', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) 2-digit country code. (e.g. CA))
        """
        super(UpdateNumberInputSet, self)._set_input('Country', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((required, string) Your inbound (MSISDN) number (e.g. 34911067000).)
        """
        super(UpdateNumberInputSet, self)._set_input('Number', value)
    def set_SMPPSystemType(self, value):
        """
        Set the value of the SMPPSystemType input for this Choreo. ((optional, string) The Mobile Orignated associated system type for SMPP client only. (e.g.: inbound))
        """
        super(UpdateNumberInputSet, self)._set_input('SMPPSystemType', value)

class UpdateNumberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateNumber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. For a successful request, an empty response body is returned.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo. A 200 is returned for a successful request.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateNumberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateNumberResultSet(response, path)
