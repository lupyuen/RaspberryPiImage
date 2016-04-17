# -*- coding: utf-8 -*-

###############################################################################
#
# Uppercase
# Returns the contents of the specified string converted to uppercase.
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

class Uppercase(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Uppercase Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Uppercase, self).__init__(temboo_session, '/Library/Utilities/Text/Uppercase')


    def new_input_set(self):
        return UppercaseInputSet()

    def _make_result_set(self, result, path):
        return UppercaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UppercaseChoreographyExecution(session, exec_id, path)

class UppercaseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Uppercase
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, multiline) The text that should be converted to uppercase.)
        """
        super(UppercaseInputSet, self)._set_input('Text', value)

class UppercaseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Uppercase Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The converted uppercase text.)
        """
        return self._output.get('Response', None)

class UppercaseChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UppercaseResultSet(response, path)
