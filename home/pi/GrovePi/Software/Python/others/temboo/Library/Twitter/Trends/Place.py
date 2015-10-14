# -*- coding: utf-8 -*-

###############################################################################
#
# Place
# Retrieves the top 10 trending topics for a specific WOEID.
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

class Place(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Place Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Place, self).__init__(temboo_session, '/Library/Twitter/Trends/Place')


    def new_input_set(self):
        return PlaceInputSet()

    def _make_result_set(self, result, path):
        return PlaceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceChoreographyExecution(session, exec_id, path)

class PlaceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Place
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(PlaceInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(PlaceInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(PlaceInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(PlaceInputSet, self)._set_input('ConsumerSecret', value)
    def set_Exclude(self, value):
        """
        Set the value of the Exclude input for this Choreo. ((optional, boolean) If set to "hashtags", all hashtags from the trends list will be removed.)
        """
        super(PlaceInputSet, self)._set_input('Exclude', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The (WOEID) Yahoo! Where On Earth ID of the location to return trending information for. Global information is available by setting this parameter to 1.)
        """
        super(PlaceInputSet, self)._set_input('ID', value)

class PlaceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Place Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class PlaceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PlaceResultSet(response, path)
