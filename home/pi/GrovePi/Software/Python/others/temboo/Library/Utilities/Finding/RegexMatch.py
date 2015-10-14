# -*- coding: utf-8 -*-

###############################################################################
#
# RegexMatch
# Returns the first substring that matches the specified regular expression pattern in the specified string.
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

class RegexMatch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegexMatch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RegexMatch, self).__init__(temboo_session, '/Library/Utilities/Finding/RegexMatch')


    def new_input_set(self):
        return RegexMatchInputSet()

    def _make_result_set(self, result, path):
        return RegexMatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegexMatchChoreographyExecution(session, exec_id, path)

class RegexMatchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegexMatch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Pattern(self, value):
        """
        Set the value of the Pattern input for this Choreo. ((conditional, string) A regular expression.)
        """
        super(RegexMatchInputSet, self)._set_input('Pattern', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) The text on which to perform a regex match.)
        """
        super(RegexMatchInputSet, self)._set_input('Text', value)

class RegexMatchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegexMatch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. ((string) The result of the match.)
        """
        return self._output.get('Result', None)

class RegexMatchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RegexMatchResultSet(response, path)
