# -*- coding: utf-8 -*-

###############################################################################
#
# SearchContactsByEmail
# Allows you to search Constant Contact by email to retrieve a contact's information.
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

class SearchContactsByEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchContactsByEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchContactsByEmail, self).__init__(temboo_session, '/Library/ConstantContact/SearchContactsByEmail')


    def new_input_set(self):
        return SearchContactsByEmailInputSet()

    def _make_result_set(self, result, path):
        return SearchContactsByEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchContactsByEmailChoreographyExecution(session, exec_id, path)

class SearchContactsByEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchContactsByEmail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        super(SearchContactsByEmailInputSet, self)._set_input('APIKey', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address to use in your search.)
        """
        super(SearchContactsByEmailInputSet, self)._set_input('EmailAddress', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        super(SearchContactsByEmailInputSet, self)._set_input('Password', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        super(SearchContactsByEmailInputSet, self)._set_input('UserName', value)

class SearchContactsByEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchContactsByEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class SearchContactsByEmailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchContactsByEmailResultSet(response, path)
