# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateEntry
# Updates a calendar event or milestone in a project you specify. 
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

class UpdateEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateEntry, self).__init__(temboo_session, '/Library/Basecamp/UpdateEntry')


    def new_input_set(self):
        return UpdateEntryInputSet()

    def _make_result_set(self, result, path):
        return UpdateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateEntryChoreographyExecution(session, exec_id, path)

class UpdateEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(UpdateEntryInputSet, self)._set_input('AccountName', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The new end date for the updated entry, in the format YYYY-MM-DD.)
        """
        super(UpdateEntryInputSet, self)._set_input('EndDate', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, integer) The ID for the calendar entry to update.)
        """
        super(UpdateEntryInputSet, self)._set_input('EntryID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(UpdateEntryInputSet, self)._set_input('Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID of the project with the calendar entry to update.)
        """
        super(UpdateEntryInputSet, self)._set_input('ProjectID', value)
    def set_ResponsibleParty(self, value):
        """
        Set the value of the ResponsibleParty input for this Choreo. ((optional, any) The user ID or company ID (preceded by a “c”, as in "c1234") to reassign the entry to. Applies only to "Milestone" entry types.)
        """
        super(UpdateEntryInputSet, self)._set_input('ResponsibleParty', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) The new start date for the updated entry, in the format YYYY-MM-DD.)
        """
        super(UpdateEntryInputSet, self)._set_input('StartDate', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The new title for the updated entry.)
        """
        super(UpdateEntryInputSet, self)._set_input('Title', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The new type for the updated entry, either "CalendarEvent" (the default) or "Milestone".)
        """
        super(UpdateEntryInputSet, self)._set_input('Type', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(UpdateEntryInputSet, self)._set_input('Username', value)

class UpdateEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)
    def get_TemplateOutput(self):
        """
        Retrieve the value for the "TemplateOutput" output from this Choreo execution. (The request created from the input template.)
        """
        return self._output.get('TemplateOutput', None)

class UpdateEntryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateEntryResultSet(response, path)
