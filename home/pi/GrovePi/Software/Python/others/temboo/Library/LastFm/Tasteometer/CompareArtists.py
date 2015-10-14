# -*- coding: utf-8 -*-

###############################################################################
#
# CompareArtists
# Retrieves a Tasteometer score from two artist inputs.
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

class CompareArtists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompareArtists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompareArtists, self).__init__(temboo_session, '/Library/LastFm/Tasteometer/CompareArtists')


    def new_input_set(self):
        return CompareArtistsInputSet()

    def _make_result_set(self, result, path):
        return CompareArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareArtistsChoreographyExecution(session, exec_id, path)

class CompareArtistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompareArtists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(CompareArtistsInputSet, self)._set_input('APIKey', value)
    def set_Artist1(self, value):
        """
        Set the value of the Artist1 input for this Choreo. ((string) The first artist to compare.)
        """
        super(CompareArtistsInputSet, self)._set_input('Artist1', value)
    def set_Artist2(self, value):
        """
        Set the value of the Artist2 input for this Choreo. ((string) The second artist to compare.)
        """
        super(CompareArtistsInputSet, self)._set_input('Artist2', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) How many shared artists to display. Defaults to 5.)
        """
        super(CompareArtistsInputSet, self)._set_input('Limit', value)

class CompareArtistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompareArtists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class CompareArtistsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompareArtistsResultSet(response, path)
