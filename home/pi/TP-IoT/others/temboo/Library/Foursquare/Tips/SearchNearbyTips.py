# -*- coding: utf-8 -*-

###############################################################################
#
# SearchNearbyTips
# Get a list of tips near the specified area.
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

class SearchNearbyTips(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchNearbyTips Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchNearbyTips, self).__init__(temboo_session, '/Library/Foursquare/Tips/SearchNearbyTips')


    def new_input_set(self):
        return SearchNearbyTipsInputSet()

    def _make_result_set(self, result, path):
        return SearchNearbyTipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchNearbyTipsChoreographyExecution(session, exec_id, path)

class SearchNearbyTipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchNearbyTips
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Filter results.  If set to 'friends', the choreo returns tips from friends.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Filter', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point of the user's location.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to be returned by the search, up to 500.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of the user's location.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Use to page through the list of results.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) Only find tips matching the given term. Cannot be used in conjunction with 'friends' filter.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(SearchNearbyTipsInputSet, self)._set_input('ResponseFormat', value)

class SearchNearbyTipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchNearbyTips Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class SearchNearbyTipsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchNearbyTipsResultSet(response, path)
