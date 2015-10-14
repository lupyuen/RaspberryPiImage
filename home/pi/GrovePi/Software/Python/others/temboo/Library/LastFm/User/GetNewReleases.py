# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewReleases
# Retrieves a list of forthcoming releases based on a user's musical taste. 
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

class GetNewReleases(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNewReleases Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNewReleases, self).__init__(temboo_session, '/Library/LastFm/User/GetNewReleases')


    def new_input_set(self):
        return GetNewReleasesInputSet()

    def _make_result_set(self, result, path):
        return GetNewReleasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewReleasesChoreographyExecution(session, exec_id, path)

class GetNewReleasesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNewReleases
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(GetNewReleasesInputSet, self)._set_input('APIKey', value)
    def set_UserRecommendations(self, value):
        """
        Set the value of the UserRecommendations input for this Choreo. ((optional, boolean) If 1, the feed contains new releases based on Last.fm's artist recommendations for this user. Otherwise, it is based on their library.)
        """
        super(GetNewReleasesInputSet, self)._set_input('UserRecommendations', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The Last.fm username.)
        """
        super(GetNewReleasesInputSet, self)._set_input('User', value)

class GetNewReleasesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNewReleases Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetNewReleasesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNewReleasesResultSet(response, path)
