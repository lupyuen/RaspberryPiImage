# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCheckin
# Allows you to create a check-in with Foursquare.
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

class CreateCheckin(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCheckin Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateCheckin, self).__init__(temboo_session, '/Library/Foursquare/Checkins/CreateCheckin')


    def new_input_set(self):
        return CreateCheckinInputSet()

    def _make_result_set(self, result, path):
        return CreateCheckinResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCheckinChoreographyExecution(session, exec_id, path)

class CreateCheckinInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCheckin
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccuracyOfCoordinates(self, value):
        """
        Set the value of the AccuracyOfCoordinates input for this Choreo. ((optional, integer) Accuracy of the user's latitude and longitude, in meters.)
        """
        super(CreateCheckinInputSet, self)._set_input('AccuracyOfCoordinates', value)
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Vertical accuracy of the user's location, in meters.)
        """
        super(CreateCheckinInputSet, self)._set_input('AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters.)
        """
        super(CreateCheckinInputSet, self)._set_input('Altitude', value)
    def set_Broadcast(self, value):
        """
        Set the value of the Broadcast input for this Choreo. ((optional, string) Who to broadcast this check-in to. Can be a comma-delimited list: private, public, facebook, twitter, or followers. Defaults to 'public'.)
        """
        super(CreateCheckinInputSet, self)._set_input('Broadcast', value)
    def set_EventID(self, value):
        """
        Set the value of the EventID input for this Choreo. ((optional, string) The event the user is checking in to. A venueId for a venue with this eventId must also be specified in the request.)
        """
        super(CreateCheckinInputSet, self)._set_input('EventID', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude point of the user's location.)
        """
        super(CreateCheckinInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) The longitude point of the user's location.)
        """
        super(CreateCheckinInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        super(CreateCheckinInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateCheckinInputSet, self)._set_input('ResponseFormat', value)
    def set_Shout(self, value):
        """
        Set the value of the Shout input for this Choreo. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        super(CreateCheckinInputSet, self)._set_input('Shout', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The venue where the user is checking in. No venueid is needed if shouting or just providing a venue name.)
        """
        super(CreateCheckinInputSet, self)._set_input('VenueID', value)
    def set_Venue(self, value):
        """
        Set the value of the Venue input for this Choreo. ((optional, string) If you are not shouting, but you don't have a venue ID or prefer a 'venueless' checkin, pass the venue name as a string using this parameter.)
        """
        super(CreateCheckinInputSet, self)._set_input('Venue', value)

class CreateCheckinResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCheckin Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateCheckinChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateCheckinResultSet(response, path)
