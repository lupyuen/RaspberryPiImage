# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateWithMedia
# Allows you to update your Twitter status and attach an image.
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

class UpdateWithMedia(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateWithMedia Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateWithMedia, self).__init__(temboo_session, '/Library/Twitter/Tweets/UpdateWithMedia')


    def new_input_set(self):
        return UpdateWithMediaInputSet()

    def _make_result_set(self, result, path):
        return UpdateWithMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWithMediaChoreographyExecution(session, exec_id, path)

class UpdateWithMediaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateWithMedia
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_MediaContent(self, value):
        """
        Set the value of the MediaContent input for this Choreo. ((required, string) The Base64 encoded image content to post to Twitter.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('MediaContent', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('ConsumerSecret', value)
    def set_DisplayCoordinates(self, value):
        """
        Set the value of the DisplayCoordinates input for this Choreo. ((optional, boolean) Whether or not to put a pin on the exact coordinates a tweet has been sent from.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('DisplayCoordinates', value)
    def set_InReplyTo(self, value):
        """
        Set the value of the InReplyTo input for this Choreo. ((optional, string) The ID of an existing status that the update is in reply to.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('InReplyTo', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude of the location this tweet refers to e.g., 40.71863.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) The longitude of the location this tweet refers to e.g., -74.005584.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('Longitude', value)
    def set_PlaceID(self, value):
        """
        Set the value of the PlaceID input for this Choreo. ((optional, string) The ID associated with a place in the world. These IDs can be retrieved from the PlacesAndGeo.ReverseGeocode Choreo.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('PlaceID', value)
    def set_PossiblySensitive(self, value):
        """
        Set the value of the PossiblySensitive input for this Choreo. ((optional, boolean) Set to true for content which may not be suitable for every audience.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('PossiblySensitive', value)
    def set_StatusUpdate(self, value):
        """
        Set the value of the StatusUpdate input for this Choreo. ((required, string) The text for your status update. 140-character limit.)
        """
        super(UpdateWithMediaInputSet, self)._set_input('StatusUpdate', value)


class UpdateWithMediaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateWithMedia Choreo.
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

class UpdateWithMediaChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateWithMediaResultSet(response, path)
