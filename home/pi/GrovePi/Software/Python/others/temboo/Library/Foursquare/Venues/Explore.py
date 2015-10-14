# -*- coding: utf-8 -*-

###############################################################################
#
# Explore
# Returns a list of recommended venues near the current location.
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

class Explore(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Explore Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Explore, self).__init__(temboo_session, '/Library/Foursquare/Venues/Explore')


    def new_input_set(self):
        return ExploreInputSet()

    def _make_result_set(self, result, path):
        return ExploreResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExploreChoreographyExecution(session, exec_id, path)

class ExploreInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Explore
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccuracyOfCoordinates(self, value):
        """
        Set the value of the AccuracyOfCoordinates input for this Choreo. ((optional, integer) Accuracy of latitude and longitude, in meters.)
        """
        super(ExploreInputSet, self)._set_input('AccuracyOfCoordinates', value)
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Accuracy of the user's altitude, in meters.)
        """
        super(ExploreInputSet, self)._set_input('AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters.)
        """
        super(ExploreInputSet, self)._set_input('Altitude', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(ExploreInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(ExploreInputSet, self)._set_input('ClientSecret', value)
    def set_Day(self, value):
        """
        Set the value of the Day input for this Choreo. ((optional, string) When set to "any", results for any day of the week are returned. Results that are targeted to the current day of the week are returned by default.)
        """
        super(ExploreInputSet, self)._set_input('Day', value)
    def set_FriendsVisits(self, value):
        """
        Set the value of the FriendsVisits input for this Choreo. ((optional, string) Limits results to places the acting user's friends have or haven't been. Valid values are: "visited" or "notvisited". )
        """
        super(ExploreInputSet, self)._set_input('FriendsVisits', value)
    def set_Intent(self, value):
        """
        Set the value of the Intent input for this Choreo. ((optional, string) Used in combination with the LastVenue input.  Return venues users often visit after a given venue when setting to "nextVenues" and providing a venue ID for the LastVenue input.)
        """
        super(ExploreInputSet, self)._set_input('Intent', value)
    def set_LastVenue(self, value):
        """
        Set the value of the LastVenue input for this Choreo. ((optional, string) A venue ID to use when Intent = "nextVenues", which returns venues users often visit after a given venue. See Choreo notes for more details about the use of this input.)
        """
        super(ExploreInputSet, self)._set_input('LastVenue', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) The latitude point of the user's location. Required unless the Near parameter is provided.)
        """
        super(ExploreInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 50.)
        """
        super(ExploreInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude point of the user's location. Required unless the Near parameter is provided.)
        """
        super(ExploreInputSet, self)._set_input('Longitude', value)
    def set_Near(self, value):
        """
        Set the value of the Near input for this Choreo. ((conditional, string) A string naming a place in the world. If the near string is not geocodable, returns a failed_geocode error. Required unless provided Latitude and Longitude.)
        """
        super(ExploreInputSet, self)._set_input('Near', value)
    def set_Novelty(self, value):
        """
        Set the value of the Novelty input for this Choreo. ((optional, string) Pass "new" or "old" to limit results to places the acting user hasn't been or has been, respectively. Omitting this parameter returns a mixture of both new and old.)
        """
        super(ExploreInputSet, self)._set_input('Novelty', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(ExploreInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used with the Limit input to page through results.)
        """
        super(ExploreInputSet, self)._set_input('Offset', value)
    def set_OpenNow(self, value):
        """
        Set the value of the OpenNow input for this Choreo. ((optional, boolean) Set to 1 to only include venues that are open now. Defaults to 0.)
        """
        super(ExploreInputSet, self)._set_input('OpenNow', value)
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((optional, string) A comma separated list of price points. Currently the valid range of price points are: [1,2,3,4]. See Choreo notes for more details about the use of this parameter.)
        """
        super(ExploreInputSet, self)._set_input('Price', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search term to be applied against tips, category, etc. at a venue.)
        """
        super(ExploreInputSet, self)._set_input('Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Radius to search within, in meters. If radius is not specified, a suggested radius will be used depending on the density of venues in the area.)
        """
        super(ExploreInputSet, self)._set_input('Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(ExploreInputSet, self)._set_input('ResponseFormat', value)
    def set_Saved(self, value):
        """
        Set the value of the Saved input for this Choreo. ((optional, boolean) Set to 1 to only include venues that the user has saved on their To-Do list or to another list. Defaults to 0.)
        """
        super(ExploreInputSet, self)._set_input('Saved', value)
    def set_Section(self, value):
        """
        Set the value of the Section input for this Choreo. ((optional, string) One of food, drinks, coffee, shops, arts, outdoors, sights, trending, specials, nextVenues , or topPicks. Choosing one of these limits results to venues with categories matching these terms.)
        """
        super(ExploreInputSet, self)._set_input('Section', value)
    def set_SortByDistance(self, value):
        """
        Set the value of the SortByDistance input for this Choreo. ((optional, boolean) Set to 1 to sort the results by distance instead of relevance. Default to 0.)
        """
        super(ExploreInputSet, self)._set_input('SortByDistance', value)
    def set_Specials(self, value):
        """
        Set the value of the Specials input for this Choreo. ((optional, boolean) Set to 1 to only include venues that have a special. Defaults to 0.)
        """
        super(ExploreInputSet, self)._set_input('Specials', value)
    def set_Time(self, value):
        """
        Set the value of the Time input for this Choreo. ((optional, string) When set to "any", results for any time of day are returned. Results that are targeted to the current time of day are returned by default.)
        """
        super(ExploreInputSet, self)._set_input('Time', value)
    def set_VenuePhotos(self, value):
        """
        Set the value of the VenuePhotos input for this Choreo. ((optional, boolean) Set to 1 to include a photo for each venue in response, if one is available. Default is 0 (no photos).)
        """
        super(ExploreInputSet, self)._set_input('VenuePhotos', value)

class ExploreResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Explore Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class ExploreChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ExploreResultSet(response, path)
