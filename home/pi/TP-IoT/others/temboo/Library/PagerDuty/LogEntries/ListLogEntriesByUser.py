# -*- coding: utf-8 -*-

###############################################################################
#
# ListLogEntriesByUser
# Lists all incident log entries associated with a specific user.
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

class ListLogEntriesByUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListLogEntriesByUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListLogEntriesByUser, self).__init__(temboo_session, '/Library/PagerDuty/LogEntries/ListLogEntriesByUser')


    def new_input_set(self):
        return ListLogEntriesByUserInputSet()

    def _make_result_set(self, result, path):
        return ListLogEntriesByUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListLogEntriesByUserChoreographyExecution(session, exec_id, path)

class ListLogEntriesByUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListLogEntriesByUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by PagerDuty.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('APIKey', value)
    def set_Include(self, value):
        """
        Set the value of the Include input for this Choreo. ((optional, string) A list of additional details to include in the response. Valid values are: channel, incident, and service.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('Include', value)
    def set_IsOverview(self, value):
        """
        Set the value of the IsOverview input for this Choreo. ((optional, boolean) If set to true, only log entries of type trigger, acknowledge, or resolve are returned. Defaults to false.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('IsOverview', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of log events returned. Default (and max limit) is 100.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The offset of the first log event record returned. Default is 0.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('Offset', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) The start of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('Since', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((required, string) The subdomain of your PagerDuty site address.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('SubDomain', value)
    def set_TimeZone(self, value):
        """
        Set the value of the TimeZone input for this Choreo. ((optional, string) The time zone in which dates in the result will be rendered. Defaults to account time zone.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('TimeZone', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) The end of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('Until', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user associated with the log entries to retrieve.)
        """
        super(ListLogEntriesByUserInputSet, self)._set_input('UserID', value)

class ListLogEntriesByUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListLogEntriesByUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class ListLogEntriesByUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListLogEntriesByUserResultSet(response, path)
