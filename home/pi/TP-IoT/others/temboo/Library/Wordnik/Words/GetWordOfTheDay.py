# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordOfTheDay
# Retrieves the word of the day for specified dates.
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

class GetWordOfTheDay(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWordOfTheDay Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetWordOfTheDay, self).__init__(temboo_session, '/Library/Wordnik/Words/GetWordOfTheDay')


    def new_input_set(self):
        return GetWordOfTheDayInputSet()

    def _make_result_set(self, result, path):
        return GetWordOfTheDayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordOfTheDayChoreographyExecution(session, exec_id, path)

class GetWordOfTheDayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWordOfTheDay
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(GetWordOfTheDayInputSet, self)._set_input('APIKey', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, string) The date of the Word of the Day to retrieve, in yyyy-MM-dd format.)
        """
        super(GetWordOfTheDayInputSet, self)._set_input('Date', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(GetWordOfTheDayInputSet, self)._set_input('ResponseType', value)

class GetWordOfTheDayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWordOfTheDay Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetWordOfTheDayChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetWordOfTheDayResultSet(response, path)
