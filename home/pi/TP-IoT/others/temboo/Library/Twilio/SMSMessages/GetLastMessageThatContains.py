# -*- coding: utf-8 -*-

###############################################################################
#
# GetLastMessageThatContains
# Retrieves the latest received message that contains the specified search string.
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

class GetLastMessageThatContains(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLastMessageThatContains Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLastMessageThatContains, self).__init__(temboo_session, '/Library/Twilio/SMSMessages/GetLastMessageThatContains')


    def new_input_set(self):
        return GetLastMessageThatContainsInputSet()

    def _make_result_set(self, result, path):
        return GetLastMessageThatContainsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLastMessageThatContainsChoreographyExecution(session, exec_id, path)

class GetLastMessageThatContainsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLastMessageThatContains
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('AuthToken', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((required, string) A search string to apply to the message body field.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('Filter', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page to search through. Defaults to 50.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml. This parameter is only valid when setting ResponseMode to "verbose".)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('ResponseFormat', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only the message string is returned. Verbose mode returns the full object. Defaults to "simple".)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('ResponseMode', value)
    def set_ReturnLegacyFormat(self, value):
        """
        Set the value of the ReturnLegacyFormat input for this Choreo. ((optional, boolean) If set to true, XML responses will be formatted using the deprecated /SMS/Messages resource schema. This should only be used if you have existing code that relies on the older schema.)
        """
        super(GetLastMessageThatContainsInputSet, self)._set_input('ReturnLegacyFormat', value)

class GetLastMessageThatContainsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLastMessageThatContains Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)
    def get_TotalPages(self):
        """
        Retrieve the value for the "TotalPages" output from this Choreo execution. ((integer) The total number of result pages that are available to search. If your search returns no results, you can increment the Page input to search further into the list of messages.)
        """
        return self._output.get('TotalPages', None)

class GetLastMessageThatContainsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLastMessageThatContainsResultSet(response, path)
