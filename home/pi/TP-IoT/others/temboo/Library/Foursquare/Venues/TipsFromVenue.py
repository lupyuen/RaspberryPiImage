# -*- coding: utf-8 -*-

###############################################################################
#
# TipsFromVenue
# This choreo returns tips for a particular venue written by other Foursquare users.
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

class TipsFromVenue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TipsFromVenue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TipsFromVenue, self).__init__(temboo_session, '/Library/Foursquare/Venues/TipsFromVenue')


    def new_input_set(self):
        return TipsFromVenueInputSet()

    def _make_result_set(self, result, path):
        return TipsFromVenueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TipsFromVenueChoreographyExecution(session, exec_id, path)

class TipsFromVenueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TipsFromVenue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(TipsFromVenueInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(TipsFromVenueInputSet, self)._set_input('ClientSecret', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to retun, up to 50.)
        """
        super(TipsFromVenueInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(TipsFromVenueInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        super(TipsFromVenueInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(TipsFromVenueInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Enter: recent or popular.)
        """
        super(TipsFromVenueInputSet, self)._set_input('Sort', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The venue you want tips for.)
        """
        super(TipsFromVenueInputSet, self)._set_input('VenueID', value)

class TipsFromVenueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TipsFromVenue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class TipsFromVenueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TipsFromVenueResultSet(response, path)
