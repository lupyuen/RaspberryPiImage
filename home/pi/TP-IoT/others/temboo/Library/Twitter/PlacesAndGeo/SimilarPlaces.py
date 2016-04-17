# -*- coding: utf-8 -*-

###############################################################################
#
# SimilarPlaces
# Locates places near the given coordinates which have a similar name.
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

class SimilarPlaces(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SimilarPlaces Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SimilarPlaces, self).__init__(temboo_session, '/Library/Twitter/PlacesAndGeo/SimilarPlaces')


    def new_input_set(self):
        return SimilarPlacesInputSet()

    def _make_result_set(self, result, path):
        return SimilarPlacesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SimilarPlacesChoreographyExecution(session, exec_id, path)

class SimilarPlacesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SimilarPlaces
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(SimilarPlacesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(SimilarPlacesInputSet, self)._set_input('AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) If supplied, the response will use the JSONP format with a callback of the given name.)
        """
        super(SimilarPlacesInputSet, self)._set_input('Callback', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(SimilarPlacesInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(SimilarPlacesInputSet, self)._set_input('ConsumerSecret', value)
    def set_ContainedWithin(self, value):
        """
        Set the value of the ContainedWithin input for this Choreo. ((optional, string) This is the place_id which you would like to restrict the search results to. This id can be retrieved with the GetPlaceInformation Choreo.)
        """
        super(SimilarPlacesInputSet, self)._set_input('ContainedWithin', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude to search around.)
        """
        super(SimilarPlacesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude to search around.)
        """
        super(SimilarPlacesInputSet, self)._set_input('Longitude', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(SimilarPlacesInputSet, self)._set_input('MaxResults', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the place.)
        """
        super(SimilarPlacesInputSet, self)._set_input('Name', value)

class SimilarPlacesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SimilarPlaces Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class SimilarPlacesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SimilarPlacesResultSet(response, path)
