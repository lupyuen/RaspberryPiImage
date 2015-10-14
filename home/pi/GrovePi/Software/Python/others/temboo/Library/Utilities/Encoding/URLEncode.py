# -*- coding: utf-8 -*-

###############################################################################
#
# URLEncode
# Returns the specified text string in the application/x-www-form-urlencoded format.
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

class URLEncode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the URLEncode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(URLEncode, self).__init__(temboo_session, '/Library/Utilities/Encoding/URLEncode')


    def new_input_set(self):
        return URLEncodeInputSet()

    def _make_result_set(self, result, path):
        return URLEncodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return URLEncodeChoreographyExecution(session, exec_id, path)

class URLEncodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the URLEncode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be URL encoded.)
        """
        super(URLEncodeInputSet, self)._set_input('Text', value)

class URLEncodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the URLEncode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_URLEncodedText(self):
        """
        Retrieve the value for the "URLEncodedText" output from this Choreo execution. ((string) The URL encoded text.)
        """
        return self._output.get('URLEncodedText', None)

class URLEncodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return URLEncodeResultSet(response, path)
