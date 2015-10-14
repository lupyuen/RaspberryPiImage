# -*- coding: utf-8 -*-

###############################################################################
#
# TextSearch
# Search for places based on a text query and optional location.
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

class TextSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TextSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TextSearch, self).__init__(temboo_session, '/Library/Google/Places/TextSearch')


    def new_input_set(self):
        return TextSearchInputSet()

    def _make_result_set(self, result, path):
        return TextSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TextSearchChoreographyExecution(session, exec_id, path)

class TextSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TextSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The API Key provided by Google.)
        """
        super(TextSearchInputSet, self)._set_input('Key', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language code, indicating in which language the results should be returned, if possible. See Choreo notes for a list of supported languages and their codes.)
        """
        super(TextSearchInputSet, self)._set_input('Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, string) Specify a latitude point around which Places results will be retrieved (e.g., 38.898717). When specifying a latitude, both longitude and radius must also be supplied.)
        """
        super(TextSearchInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, string) Specify a longitude point around which Places results will be retrieved (e.g., -77.035974). When specifying a longitude, both latitude and radius must also be supplied.)
        """
        super(TextSearchInputSet, self)._set_input('Longitude', value)
    def set_MaxPrice(self, value):
        """
        Set the value of the MaxPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(TextSearchInputSet, self)._set_input('MaxPrice', value)
    def set_MinPrice(self, value):
        """
        Set the value of the MinPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(TextSearchInputSet, self)._set_input('MinPrice', value)
    def set_OpenNow(self, value):
        """
        Set the value of the OpenNow input for this Choreo. ((optional, boolean) Returns only those Places that are open for business at the time the query is sent. Places that do not specify opening hours in the Google Places database will not be returned.)
        """
        super(TextSearchInputSet, self)._set_input('OpenNow', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "NextPageToken" returned in the choreo output from a previous run. Used to page through large result sets. When the PageToken is specified, all other inputs are ignored.)
        """
        super(TextSearchInputSet, self)._set_input('PageToken', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) The text string on which to search, for example: "restaurant". The Place service will return candidate matches based on this string and order the results based on their perceived relevance.)
        """
        super(TextSearchInputSet, self)._set_input('Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Specify the radius in meters for which Places results will be returned. Maximum radius is limited to 50,000 meters. When specifying a radius, both latitude and longitude must also be supplied.)
        """
        super(TextSearchInputSet, self)._set_input('Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(TextSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(TextSearchInputSet, self)._set_input('Sensor', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Filter results by types, such as: bar, dentist.  Multiple types must be separated by the pipe ("|") symbol: bar|dentist|airport.)
        """
        super(TextSearchInputSet, self)._set_input('Types', value)

class TextSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TextSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class TextSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TextSearchResultSet(response, path)
