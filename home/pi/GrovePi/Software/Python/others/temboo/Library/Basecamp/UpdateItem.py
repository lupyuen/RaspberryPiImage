# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateItem
# Creates a new item for a specified To-do list.
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

class UpdateItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateItem, self).__init__(temboo_session, '/Library/Basecamp/UpdateItem')


    def new_input_set(self):
        return UpdateItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateItemChoreographyExecution(session, exec_id, path)

class UpdateItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(UpdateItemInputSet, self)._set_input('AccountName', value)
    def set_Content(self, value):
        """
        Set the value of the Content input for this Choreo. ((required, string) The text of the updated item.)
        """
        super(UpdateItemInputSet, self)._set_input('Content', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, integer) The ID for the item to update.)
        """
        super(UpdateItemInputSet, self)._set_input('ItemID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(UpdateItemInputSet, self)._set_input('Password', value)
    def set_ResponsibleParty(self, value):
        """
        Set the value of the ResponsibleParty input for this Choreo. ((optional, integer) The user ID or company ID  (preceded by a “c”, as in "c1234") to re-assign the item to when updated. Defaults to unassigned If left blank.)
        """
        super(UpdateItemInputSet, self)._set_input('ResponsibleParty', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(UpdateItemInputSet, self)._set_input('Username', value)

class UpdateItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No structured response is returned from Basecamp for new item requests.)
        """
        return self._output.get('Response', None)

class UpdateItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateItemResultSet(response, path)
