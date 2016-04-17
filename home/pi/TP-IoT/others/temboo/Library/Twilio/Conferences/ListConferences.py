# -*- coding: utf-8 -*-

###############################################################################
#
# ListConferences
# Returns a list of conferences within an account.
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

class ListConferences(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListConferences Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListConferences, self).__init__(temboo_session, '/Library/Twilio/Conferences/ListConferences')


    def new_input_set(self):
        return ListConferencesInputSet()

    def _make_result_set(self, result, path):
        return ListConferencesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListConferencesChoreographyExecution(session, exec_id, path)

class ListConferencesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListConferences
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(ListConferencesInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(ListConferencesInputSet, self)._set_input('AuthToken', value)
    def set_DateCreated(self, value):
        """
        Set the value of the DateCreated input for this Choreo. ((optional, string) Only show conferences that started on this date, given as YYYY-MM-DD. You can also specify operators such as <=YYYY-MM-DD.)
        """
        super(ListConferencesInputSet, self)._set_input('DateCreated', value)
    def set_DateUpdated(self, value):
        """
        Set the value of the DateUpdated input for this Choreo. ((optional, string) Only returns conferences that were last updated on this date, given as YYYY-MM-DD. You can also specify operators such as <=YYYY-MM-DD.)
        """
        super(ListConferencesInputSet, self)._set_input('DateUpdated', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) Returns conferences who's FriendlyName is the exact match of this string.)
        """
        super(ListConferencesInputSet, self)._set_input('FriendlyName', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        super(ListConferencesInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(ListConferencesInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListConferencesInputSet, self)._set_input('ResponseFormat', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Only returns conferences currently in with this status. May be init, in-progress, or completed.)
        """
        super(ListConferencesInputSet, self)._set_input('Status', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the list of conferences. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(ListConferencesInputSet, self)._set_input('SubAccountSID', value)

class ListConferencesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListConferences Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListConferencesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListConferencesResultSet(response, path)
