# -*- coding: utf-8 -*-

###############################################################################
#
# Phrases
# Returns a list of the top phrases in the Congressional Record, which are searchable by day, month, state, or legislator.
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

class Phrases(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Phrases Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Phrases, self).__init__(temboo_session, '/Library/SunlightLabs/CapitolWords/Phrases')


    def new_input_set(self):
        return PhrasesInputSet()

    def _make_result_set(self, result, path):
        return PhrasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhrasesChoreographyExecution(session, exec_id, path)

class PhrasesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Phrases
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(PhrasesInputSet, self)._set_input('APIKey', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        super(PhrasesInputSet, self)._set_input('Chamber', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        super(PhrasesInputSet, self)._set_input('Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        super(PhrasesInputSet, self)._set_input('EndDate', value)
    def set_EntityType(self, value):
        """
        Set the value of the EntityType input for this Choreo. ((required, string) The entity type to get top phrases for. Acceptable values: date, month, state, legislator.)
        """
        super(PhrasesInputSet, self)._set_input('EntityType', value)
    def set_EntityValue(self, value):
        """
        Set the value of the EntityValue input for this Choreo. ((required, string) The value of the entity to get top phrases for. Acceptable formats as follows for each EntityType: (date) 2011-11-09, (month) 201111, (state) NY. For the legislator EntityType, enter Bioguide ID here.)
        """
        super(PhrasesInputSet, self)._set_input('EntityValue', value)
    def set_Length(self, value):
        """
        Set the value of the Length input for this Choreo. ((optional, integer) The length of the phrase, in words, to search for (up to 5).)
        """
        super(PhrasesInputSet, self)._set_input('Length', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to show. 100 results are shown at a time. To see more results use the page parameter.)
        """
        super(PhrasesInputSet, self)._set_input('Page', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        super(PhrasesInputSet, self)._set_input('Party', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        super(PhrasesInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) The metric and direction to sort by. Acceptable values: tfidf asc (default), tfidf desc, count asc, count desc.)
        """
        super(PhrasesInputSet, self)._set_input('Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        super(PhrasesInputSet, self)._set_input('StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        super(PhrasesInputSet, self)._set_input('State', value)

class PhrasesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Phrases Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CapitolWords.)
        """
        return self._output.get('Response', None)

class PhrasesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PhrasesResultSet(response, path)
