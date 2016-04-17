# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEntry
# Creates a new calendar entry in a specified project.
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

class CreateEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateEntry, self).__init__(temboo_session, '/Library/Basecamp/CreateEntry')


    def new_input_set(self):
        return CreateEntryInputSet()

    def _make_result_set(self, result, path):
        return CreateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEntryChoreographyExecution(session, exec_id, path)

class CreateEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(CreateEntryInputSet, self)._set_input('AccountName', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The date the entry ends, in YYYY-MM-DD format. This is the same as StartDate for one-day entries.)
        """
        super(CreateEntryInputSet, self)._set_input('EndDate', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(CreateEntryInputSet, self)._set_input('Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project in which to create the new entry.)
        """
        super(CreateEntryInputSet, self)._set_input('ProjectID', value)
    def set_ResponsibleParty(self, value):
        """
        Set the value of the ResponsibleParty input for this Choreo. ((optional, any) The user ID or company ID (preceded by a “c”, as in "c1234") to assign the entry to. Applies only to "Milestone" entry types.)
        """
        super(CreateEntryInputSet, self)._set_input('ResponsibleParty', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The date the entry starts, in YYYY-MM-DD format.)
        """
        super(CreateEntryInputSet, self)._set_input('StartDate', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title for the calendar entry to create.)
        """
        super(CreateEntryInputSet, self)._set_input('Title', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The type of calendar entry to create, either "Milestone" or "CalendarEvent" (the default).)
        """
        super(CreateEntryInputSet, self)._set_input('Type', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(CreateEntryInputSet, self)._set_input('Username', value)

class CreateEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class CreateEntryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateEntryResultSet(response, path)
