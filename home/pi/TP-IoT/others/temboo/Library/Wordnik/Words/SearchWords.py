# -*- coding: utf-8 -*-

###############################################################################
#
# SearchWords
# Searches words.
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

class SearchWords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchWords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchWords, self).__init__(temboo_session, '/Library/Wordnik/Words/SearchWords')


    def new_input_set(self):
        return SearchWordsInputSet()

    def _make_result_set(self, result, path):
        return SearchWordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchWordsChoreographyExecution(session, exec_id, path)

class SearchWordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchWords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(SearchWordsInputSet, self)._set_input('APIKey', value)
    def set_CaseSensitive(self, value):
        """
        Set the value of the CaseSensitive input for this Choreo. ((optional, string) Makes the query case-insensitive when false. Defaults to true, so queries are case-sensitive.)
        """
        super(SearchWordsInputSet, self)._set_input('CaseSensitive', value)
    def set_ExcludePartOfSpeech(self, value):
        """
        Set the value of the ExcludePartOfSpeech input for this Choreo. ((optional, string) Excludes the specified comma-delimited parts of speech from the results returned. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        super(SearchWordsInputSet, self)._set_input('ExcludePartOfSpeech', value)
    def set_IncludePartOfSpeech(self, value):
        """
        Set the value of the IncludePartOfSpeech input for this Choreo. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        super(SearchWordsInputSet, self)._set_input('IncludePartOfSpeech', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 10.)
        """
        super(SearchWordsInputSet, self)._set_input('Limit', value)
    def set_MaxCorpus(self, value):
        """
        Set the value of the MaxCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count below the given number.)
        """
        super(SearchWordsInputSet, self)._set_input('MaxCorpus', value)
    def set_MaxEntries(self, value):
        """
        Set the value of the MaxEntries input for this Choreo. ((optional, integer) Limits the results to words that have fewer than the given numner of dictionary entries.)
        """
        super(SearchWordsInputSet, self)._set_input('MaxEntries', value)
    def set_MaxLength(self, value):
        """
        Set the value of the MaxLength input for this Choreo. ((optional, integer) Maximum word length.)
        """
        super(SearchWordsInputSet, self)._set_input('MaxLength', value)
    def set_MinCorpus(self, value):
        """
        Set the value of the MinCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count above the given number.)
        """
        super(SearchWordsInputSet, self)._set_input('MinCorpus', value)
    def set_MinEntries(self, value):
        """
        Set the value of the MinEntries input for this Choreo. ((optional, integer) Limits the results to words that have more than the given numner of dictionary entries.)
        """
        super(SearchWordsInputSet, self)._set_input('MinEntries', value)
    def set_MinLength(self, value):
        """
        Set the value of the MinLength input for this Choreo. ((optional, integer) ‪Minimum word length.)
        """
        super(SearchWordsInputSet, self)._set_input('MinLength', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Word or fragment to query for in Wordnik.)
        """
        super(SearchWordsInputSet, self)._set_input('Query', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(SearchWordsInputSet, self)._set_input('ResponseType', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Number of results to skip.)
        """
        super(SearchWordsInputSet, self)._set_input('Skip', value)

class SearchWordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchWords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class SearchWordsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchWordsResultSet(response, path)
