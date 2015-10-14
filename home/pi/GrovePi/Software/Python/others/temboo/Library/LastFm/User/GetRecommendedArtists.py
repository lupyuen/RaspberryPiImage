# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecommendedArtists
# Retrieves Last.fm artist recommendations for a user.
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

class GetRecommendedArtists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecommendedArtists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecommendedArtists, self).__init__(temboo_session, '/Library/LastFm/User/GetRecommendedArtists')


    def new_input_set(self):
        return GetRecommendedArtistsInputSet()

    def _make_result_set(self, result, path):
        return GetRecommendedArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecommendedArtistsChoreographyExecution(session, exec_id, path)

class GetRecommendedArtistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecommendedArtists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(GetRecommendedArtistsInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((string) Your Last.fm API Secret.)
        """
        super(GetRecommendedArtistsInputSet, self)._set_input('APISecret', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        super(GetRecommendedArtistsInputSet, self)._set_input('Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to first page.)
        """
        super(GetRecommendedArtistsInputSet, self)._set_input('Page', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        super(GetRecommendedArtistsInputSet, self)._set_input('SessionKey', value)

class GetRecommendedArtistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecommendedArtists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetRecommendedArtistsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecommendedArtistsResultSet(response, path)
