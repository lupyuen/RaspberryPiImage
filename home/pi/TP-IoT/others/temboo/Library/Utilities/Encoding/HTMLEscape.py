# -*- coding: utf-8 -*-

###############################################################################
#
# HTMLEscape
# Replaces HTML markup characters in the specified text with equivalent character entity names. 
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

class HTMLEscape(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HTMLEscape Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(HTMLEscape, self).__init__(temboo_session, '/Library/Utilities/Encoding/HTMLEscape')


    def new_input_set(self):
        return HTMLEscapeInputSet()

    def _make_result_set(self, result, path):
        return HTMLEscapeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HTMLEscapeChoreographyExecution(session, exec_id, path)

class HTMLEscapeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HTMLEscape
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UnescapedHTML(self, value):
        """
        Set the value of the UnescapedHTML input for this Choreo. ((required, string) The HTML that needs to be escaped.)
        """
        super(HTMLEscapeInputSet, self)._set_input('UnescapedHTML', value)

class HTMLEscapeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HTMLEscape Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_EscapedHTML(self):
        """
        Retrieve the value for the "EscapedHTML" output from this Choreo execution. ((string) The escaped HTML.)
        """
        return self._output.get('EscapedHTML', None)

class HTMLEscapeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return HTMLEscapeResultSet(response, path)
