# -*- coding: utf-8 -*-

###############################################################################
#
# CompleteItem
# Marks a single, specified item in a To-do list as complete.
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

class CompleteItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompleteItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompleteItem, self).__init__(temboo_session, '/Library/Basecamp/CompleteItem')


    def new_input_set(self):
        return CompleteItemInputSet()

    def _make_result_set(self, result, path):
        return CompleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompleteItemChoreographyExecution(session, exec_id, path)

class CompleteItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompleteItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(CompleteItemInputSet, self)._set_input('AccountName', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, integer) The ID of the item to mark as complete.)
        """
        super(CompleteItemInputSet, self)._set_input('ItemID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(CompleteItemInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(CompleteItemInputSet, self)._set_input('Username', value)

class CompleteItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompleteItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (There is no structrued response from complete item requests.)
        """
        return self._output.get('Response', None)

class CompleteItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompleteItemResultSet(response, path)
