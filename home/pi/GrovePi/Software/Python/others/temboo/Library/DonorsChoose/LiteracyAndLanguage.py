# -*- coding: utf-8 -*-

###############################################################################
#
# LiteracyAndLanguage
# Returns results for projects within the Literacy and Language category.
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

class LiteracyAndLanguage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LiteracyAndLanguage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LiteracyAndLanguage, self).__init__(temboo_session, '/Library/DonorsChoose/LiteracyAndLanguage')


    def new_input_set(self):
        return LiteracyAndLanguageInputSet()

    def _make_result_set(self, result, path):
        return LiteracyAndLanguageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LiteracyAndLanguageChoreographyExecution(session, exec_id, path)

class LiteracyAndLanguageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LiteracyAndLanguage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey provided by DonorsChoose.org. Defaults to the test  APIKey 'DONORSCHOOSE'.)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('APIKey', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) The number of the first row to return in the result. For example, if index=10, the results could show rows 10-59.)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('Index', value)
    def set_Max(self, value):
        """
        Set the value of the Max input for this Choreo. ((optional, integer) The max number of projects to return. Can return up to 50 rows at a time. Defaults to 10 when left empty.)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('Max', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('ResponseFormat', value)
    def set_ShowCounts(self, value):
        """
        Set the value of the ShowCounts input for this Choreo. ((optional, boolean) Set to 1 to return facet counts in the response)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('ShowCounts', value)
    def set_ShowSynopsis(self, value):
        """
        Set the value of the ShowSynopsis input for this Choreo. ((optional, boolean) Set to 1 to show the synopsis for each project listing)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('ShowSynopsis', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((optional, string) Enter a sub-category of Literacy & Language. When left empty, all Literacy & Language projects are returned.)
        """
        super(LiteracyAndLanguageInputSet, self)._set_input('Subject', value)

class LiteracyAndLanguageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LiteracyAndLanguage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DonorsChoose.org)
        """
        return self._output.get('Response', None)

class LiteracyAndLanguageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LiteracyAndLanguageResultSet(response, path)
