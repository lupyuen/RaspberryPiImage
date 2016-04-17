# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveProfile
# Returns a user's profile information including the user’s identity, geographical location, and fitness goals.
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

class RetrieveProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveProfile, self).__init__(temboo_session, '/Library/RunKeeper/Profile/RetrieveProfile')


    def new_input_set(self):
        return RetrieveProfileInputSet()

    def _make_result_set(self, result, path):
        return RetrieveProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveProfileChoreographyExecution(session, exec_id, path)

class RetrieveProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(RetrieveProfileInputSet, self)._set_input('AccessToken', value)

class RetrieveProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveProfileResultSet(response, path)
