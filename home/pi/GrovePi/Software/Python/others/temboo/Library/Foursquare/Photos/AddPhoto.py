# -*- coding: utf-8 -*-

###############################################################################
#
# AddPhoto
# Allows a user to add a new photo to a check-in, tip, or a venue.
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

class AddPhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddPhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddPhoto, self).__init__(temboo_session, '/Library/Foursquare/Photos/AddPhoto')


    def new_input_set(self):
        return AddPhotoInputSet()

    def _make_result_set(self, result, path):
        return AddPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPhotoChoreographyExecution(session, exec_id, path)

class AddPhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddPhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Vertical accuracy of the user's location, in meters.)
        """
        super(AddPhotoInputSet, self)._set_input('AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters.)
        """
        super(AddPhotoInputSet, self)._set_input('Altitude', value)
    def set_Broadcast(self, value):
        """
        Set the value of the Broadcast input for this Choreo. ((optional, string) Whether to broadcast this photo. Set to "twitter" if you want to send to twitter, "facebook "if you want to send to facebook, or "twitter,facebook" if you want to send to both.)
        """
        super(AddPhotoInputSet, self)._set_input('Broadcast', value)
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((conditional, any) The ID of the checkin to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        super(AddPhotoInputSet, self)._set_input('CheckinID', value)
    def set_ImageFile(self, value):
        """
        Set the value of the ImageFile input for this Choreo. ((conditional, string) The base64 encoded image contents. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        super(AddPhotoInputSet, self)._set_input('ImageFile', value)
    def set_LLAccuracy(self, value):
        """
        Set the value of the LLAccuracy input for this Choreo. ((optional, integer) Accuracy of the user's latitude and longitude, in meters.)
        """
        super(AddPhotoInputSet, self)._set_input('LLAccuracy', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Laitude of the user's location.)
        """
        super(AddPhotoInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Longitude of the user's location.)
        """
        super(AddPhotoInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(AddPhotoInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(AddPhotoInputSet, self)._set_input('ResponseFormat', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((conditional, string) The ID of the tip to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        super(AddPhotoInputSet, self)._set_input('TipID', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((conditional, string) The ID of the venue to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        super(AddPhotoInputSet, self)._set_input('VenueID', value)


class AddPhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddPhoto Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class AddPhotoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddPhotoResultSet(response, path)
