# -*- coding: utf-8 -*-

###############################################################################
#
# SearchJournalEntries
# Returns a keyword search of all journal entries.
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

class SearchJournalEntries(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchJournalEntries Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchJournalEntries, self).__init__(temboo_session, '/Library/Kiva/JournalEntries/SearchJournalEntries')


    def new_input_set(self):
        return SearchJournalEntriesInputSet()

    def _make_result_set(self, result, path):
        return SearchJournalEntriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchJournalEntriesChoreographyExecution(session, exec_id, path)

class SearchJournalEntriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchJournalEntries
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        super(SearchJournalEntriesInputSet, self)._set_input('AppID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        super(SearchJournalEntriesInputSet, self)._set_input('Page', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) Word or phrase used to search for in the journals' content.)
        """
        super(SearchJournalEntriesInputSet, self)._set_input('Query', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        super(SearchJournalEntriesInputSet, self)._set_input('ResponseType', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The order by which to return the results. Acceptable values: newest, oldest, recommendation_count, comment_count. Defaults to newest.)
        """
        super(SearchJournalEntriesInputSet, self)._set_input('SortBy', value)

class SearchJournalEntriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchJournalEntries Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class SearchJournalEntriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchJournalEntriesResultSet(response, path)
