# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForBusinessesWithDeals
# Only returns information for businesses with deals.
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

class SearchForBusinessesWithDeals(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchForBusinessesWithDeals Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchForBusinessesWithDeals, self).__init__(temboo_session, '/Library/Yelp/SearchForBusinessesWithDeals')


    def new_input_set(self):
        return SearchForBusinessesWithDealsInputSet()

    def _make_result_set(self, result, path):
        return SearchForBusinessesWithDealsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBusinessesWithDealsChoreographyExecution(session, exec_id, path)

class SearchForBusinessesWithDealsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchForBusinessesWithDeals
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) Narrow or widen the search range in relation to the coordinates, such as "2" for state or "8" for street address.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Accuracy', value)
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "wine" or "restaurants". Leave blank to search for all business types.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('BusinessType', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) The category to filter search results with. This can be a list of comma delimited categories. For example, "bars,french". See Choreo description for a list of categories.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Category', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Yelp.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Yelp.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of business results to return. The maxiumum is 20.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Count', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) The ISO 3166-1 2-digit country code to use when parsing the location field. United States = US, Canada = CA, United Kingdom = GB.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('CountryCode', value)
    def set_LanguageCode(self, value):
        """
        Set the value of the LanguageCode input for this Choreo. ((optional, string) The ISO 639 language code. Default to "en". Reviews and snippets written in the specified language will be returned.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('LanguageCode', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) The latitude to search near, such as "37.788022". Searching with either Location or Coordinates is required.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Latitude', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((conditional, string) An address, neighborhood, city, state, or ZIP code in which to search for the category. Searching with either Location or Coordinates is required.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Location', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude to search near, such as "-122.399797". Searching with either Location or Coordinates is required.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Longitude', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offsets the list of returned business results by this amount.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Offset', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((optional, integer) Narrow or expand a search by specifying a range in either feet, meters, miles, or kilometers, depending on the value of the Units input. Defaults to 200 feet. Maximum is 25 miles (40000 meters).)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Range', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, integer) The sort mode: 0 = Best matched, 1 = Distance (default), 2 = Highest Rated.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Sort', value)
    def set_TokenSecret(self, value):
        """
        Set the value of the TokenSecret input for this Choreo. ((required, string) The Token Secret provided by Yelp.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('TokenSecret', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The Token provided by Yelp.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Token', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Specify "feet" (the default), "meters", "miles", or "kilometers". Units apply to the Range input value.)
        """
        super(SearchForBusinessesWithDealsInputSet, self)._set_input('Units', value)

class SearchForBusinessesWithDealsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchForBusinessesWithDeals Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchForBusinessesWithDealsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchForBusinessesWithDealsResultSet(response, path)
