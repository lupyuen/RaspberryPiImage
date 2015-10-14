# -*- coding: utf-8 -*-

###############################################################################
#
# ListAccounts
# Retrieves a list of the subaccounts belonging to the main account.
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

class ListAccounts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAccounts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAccounts, self).__init__(temboo_session, '/Library/Twilio/Accounts/ListAccounts')


    def new_input_set(self):
        return ListAccountsInputSet()

    def _make_result_set(self, result, path):
        return ListAccountsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAccountsChoreographyExecution(session, exec_id, path)

class ListAccountsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAccounts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(ListAccountsInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(ListAccountsInputSet, self)._set_input('AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) Filters the results for accounts with friendly names that exactly match this value.)
        """
        super(ListAccountsInputSet, self)._set_input('FriendlyName', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        super(ListAccountsInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        super(ListAccountsInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(ListAccountsInputSet, self)._set_input('ResponseFormat', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Filters results for accounts that have a particular status. Valid values are: closed, suspended, or active.)
        """
        super(ListAccountsInputSet, self)._set_input('Status', value)

class ListAccountsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAccounts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListAccountsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAccountsResultSet(response, path)
