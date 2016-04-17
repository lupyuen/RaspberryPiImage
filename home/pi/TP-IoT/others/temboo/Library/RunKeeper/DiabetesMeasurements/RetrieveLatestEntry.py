# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveLatestEntry
# Returns the latest entry from a user's diabetes measurements history.
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

class RetrieveLatestEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveLatestEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveLatestEntry, self).__init__(temboo_session, '/Library/RunKeeper/DiabetesMeasurements/RetrieveLatestEntry')


    def new_input_set(self):
        return RetrieveLatestEntryInputSet()

    def _make_result_set(self, result, path):
        return RetrieveLatestEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveLatestEntryChoreographyExecution(session, exec_id, path)

class RetrieveLatestEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveLatestEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(RetrieveLatestEntryInputSet, self)._set_input('AccessToken', value)

class RetrieveLatestEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveLatestEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)
    def get_Insulin(self):
        """
        Retrieve the value for the "Insulin" output from this Choreo execution. ((decimal) The value of the measured quantity in U (omitted if not available).)
        """
        return self._output.get('Insulin', None)
    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) The timestamp of the entry.)
        """
        return self._output.get('Timestamp', None)
    def get_URI(self):
        """
        Retrieve the value for the "URI" output from this Choreo execution. ((string) The URI of the entry.)
        """
        return self._output.get('URI', None)

class RetrieveLatestEntryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveLatestEntryResultSet(response, path)
