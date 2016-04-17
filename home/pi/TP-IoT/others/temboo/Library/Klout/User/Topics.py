# -*- coding: utf-8 -*-

###############################################################################
#
# Topics
# Retrieves a user's topics. 
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

class Topics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Topics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Topics, self).__init__(temboo_session, '/Library/Klout/User/Topics')


    def new_input_set(self):
        return TopicsInputSet()

    def _make_result_set(self, result, path):
        return TopicsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopicsChoreographyExecution(session, exec_id, path)

class TopicsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Topics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Klout.)
        """
        super(TopicsInputSet, self)._set_input('APIKey', value)
    def set_KloutID(self, value):
        """
        Set the value of the KloutID input for this Choreo. ((required, string) The id for a Klout user to retrieve topics for.)
        """
        super(TopicsInputSet, self)._set_input('KloutID', value)

class TopicsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Topics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Klout.)
        """
        return self._output.get('Response', None)

class TopicsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopicsResultSet(response, path)
