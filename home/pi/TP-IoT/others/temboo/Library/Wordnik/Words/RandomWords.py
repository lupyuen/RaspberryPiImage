# -*- coding: utf-8 -*-

###############################################################################
#
# RandomWords
# Retrieves a list of random words.
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

class RandomWords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RandomWords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RandomWords, self).__init__(temboo_session, '/Library/Wordnik/Words/RandomWords')


    def new_input_set(self):
        return RandomWordsInputSet()

    def _make_result_set(self, result, path):
        return RandomWordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RandomWordsChoreographyExecution(session, exec_id, path)

class RandomWordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RandomWords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(RandomWordsInputSet, self)._set_input('APIKey', value)
    def set_ExcludePartOfSpeech(self, value):
        """
        Set the value of the ExcludePartOfSpeech input for this Choreo. ((optional, string) Excludes the specified comma-delimited parts of speech from the results returned. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        super(RandomWordsInputSet, self)._set_input('ExcludePartOfSpeech', value)
    def set_HasDefinition(self, value):
        """
        Set the value of the HasDefinition input for this Choreo. ((optional, string) Only returns words that have dictionary definitions when true. Otherwise false. Defaults to true.)
        """
        super(RandomWordsInputSet, self)._set_input('HasDefinition', value)
    def set_IncludePartOfSpeech(self, value):
        """
        Set the value of the IncludePartOfSpeech input for this Choreo. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        super(RandomWordsInputSet, self)._set_input('IncludePartOfSpeech', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 10.)
        """
        super(RandomWordsInputSet, self)._set_input('Limit', value)
    def set_MaxCorpus(self, value):
        """
        Set the value of the MaxCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count below the given number.)
        """
        super(RandomWordsInputSet, self)._set_input('MaxCorpus', value)
    def set_MaxDictionaries(self, value):
        """
        Set the value of the MaxDictionaries input for this Choreo. ((optional, integer) Maximum number of dictionaries in which the words appear.)
        """
        super(RandomWordsInputSet, self)._set_input('MaxDictionaries', value)
    def set_MaxLength(self, value):
        """
        Set the value of the MaxLength input for this Choreo. ((optional, integer) Maximum word length.)
        """
        super(RandomWordsInputSet, self)._set_input('MaxLength', value)
    def set_MinCorpus(self, value):
        """
        Set the value of the MinCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count above the given number.)
        """
        super(RandomWordsInputSet, self)._set_input('MinCorpus', value)
    def set_MinDictionaries(self, value):
        """
        Set the value of the MinDictionaries input for this Choreo. ((optional, integer) Minimum number of dictionaries in which the words appear.)
        """
        super(RandomWordsInputSet, self)._set_input('MinDictionaries', value)
    def set_MinLength(self, value):
        """
        Set the value of the MinLength input for this Choreo. ((optional, integer) ‪Minimum word length.)
        """
        super(RandomWordsInputSet, self)._set_input('MinLength', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(RandomWordsInputSet, self)._set_input('ResponseType', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Results can be sorted by: alpha, count, or length.)
        """
        super(RandomWordsInputSet, self)._set_input('SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Indicate the order to sort, either asc (ascending) or desc (descending).)
        """
        super(RandomWordsInputSet, self)._set_input('SortOrder', value)

class RandomWordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RandomWords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class RandomWordsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RandomWordsResultSet(response, path)
