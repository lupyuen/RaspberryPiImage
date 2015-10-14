# -*- coding: utf-8 -*-

###############################################################################
#
# Request
# Use this method to request funds from a source user, originating from the user associated with the authorized access token.
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

class Request(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Request Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Request, self).__init__(temboo_session, '/Library/Dwolla/Transactions/Request')


    def new_input_set(self):
        return RequestInputSet()

    def _make_result_set(self, result, path):
        return RequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RequestChoreographyExecution(session, exec_id, path)

class RequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Request
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        super(RequestInputSet, self)._set_input('AccessToken', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, decimal) Amount of funds to request from the source user.)
        """
        super(RequestInputSet, self)._set_input('Amount', value)
    def set_FacillitatorAmount(self, value):
        """
        Set the value of the FacillitatorAmount input for this Choreo. ((optional, decimal) Amount of the facilitator fee to override. Only applicable if the facilitator fee feature is enabled. If set to 0, facilitator fee is disabled for transaction. Cannot exceed 25% of the 'amount'.)
        """
        super(RequestInputSet, self)._set_input('FacillitatorAmount', value)
    def set_Notes(self, value):
        """
        Set the value of the Notes input for this Choreo. ((optional, multiline) Note to attach to the transaction. Limited to 250 characters.)
        """
        super(RequestInputSet, self)._set_input('Notes', value)
    def set_Pin(self, value):
        """
        Set the value of the Pin input for this Choreo. ((required, integer) User's PIN associated with their account.)
        """
        super(RequestInputSet, self)._set_input('Pin', value)
    def set_SourceID(self, value):
        """
        Set the value of the SourceID input for this Choreo. ((required, string) Identification of the user to request funds from. Must be the Dwolla identifier, Facebook identifier, Twitter screename, phone number, or email address.)
        """
        super(RequestInputSet, self)._set_input('SourceID', value)
    def set_SourceType(self, value):
        """
        Set the value of the SourceType input for this Choreo. ((optional, string) Type of destination user. Defaults to Dwolla. Can be Dwolla, Facebook, Twitter, Email, or Phone.)
        """
        super(RequestInputSet, self)._set_input('SourceType', value)

class RequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Request Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class RequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RequestResultSet(response, path)
