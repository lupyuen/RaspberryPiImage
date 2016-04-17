# -*- coding: utf-8 -*-

###############################################################################
#
# SearchVenues
# Obtain a list of venues near the current location. 
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

class SearchVenues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchVenues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchVenues, self).__init__(temboo_session, '/Library/Foursquare/Venues/SearchVenues')


    def new_input_set(self):
        return SearchVenuesInputSet()

    def _make_result_set(self, result, path):
        return SearchVenuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchVenuesChoreographyExecution(session, exec_id, path)

class SearchVenuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchVenues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccuracyOfCoordinates(self, value):
        """
        Set the value of the AccuracyOfCoordinates input for this Choreo. ((optional, integer) Accuracy of latitude and longitude, in meters. Currently, this parameter   does not affect search results.)
        """
        super(SearchVenuesInputSet, self)._set_input('AccuracyOfCoordinates', value)
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Accuracy of the user's altitude, in meters. Currently, this parameter does not affect search results.)
        """
        super(SearchVenuesInputSet, self)._set_input('AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters. Currently, this parameter does not affect search results.)
        """
        super(SearchVenuesInputSet, self)._set_input('Altitude', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(SearchVenuesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(SearchVenuesInputSet, self)._set_input('ClientSecret', value)
    def set_Intent(self, value):
        """
        Set the value of the Intent input for this Choreo. ((optional, string) Indicates your intent when performing the search.  Enter: checkin (default), match (requires Query and Latitude/Longitude to be provided).)
        """
        super(SearchVenuesInputSet, self)._set_input('Intent', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point of the user's location.)
        """
        super(SearchVenuesInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to retun, up to 50.)
        """
        super(SearchVenuesInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of the user's location.)
        """
        super(SearchVenuesInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(SearchVenuesInputSet, self)._set_input('OauthToken', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) Your search string.)
        """
        super(SearchVenuesInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(SearchVenuesInputSet, self)._set_input('ResponseFormat', value)

class SearchVenuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchVenues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class SearchVenuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchVenuesResultSet(response, path)
