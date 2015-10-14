# -*- coding: utf-8 -*-

###############################################################################
#
# SchoolSearch
# Returns a list of school district profiles and related school information for a zip code, city, state, or other criteria in the search parameters.
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

class SchoolSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SchoolSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SchoolSearch, self).__init__(temboo_session, '/Library/SchoolFinder/SchoolSearch')


    def new_input_set(self):
        return SchoolSearchInputSet()

    def _make_result_set(self, result, path):
        return SchoolSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SchoolSearchChoreographyExecution(session, exec_id, path)

class SchoolSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SchoolSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        super(SchoolSearchInputSet, self)._set_input('APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The name of a city. Must also be accompanied by the corresponding state parameter.)
        """
        super(SchoolSearchInputSet, self)._set_input('City', value)
    def set_County(self, value):
        """
        Set the value of the County input for this Choreo. ((conditional, string) The name of a county.)
        """
        super(SchoolSearchInputSet, self)._set_input('County', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((conditional, decimal) A distance in miles from a specific latitude/longitude. The suggested value is around 1.5 miles. Please note that distance is required when using latitude and longitude parameters.)
        """
        super(SchoolSearchInputSet, self)._set_input('Distance', value)
    def set_DistrictID(self, value):
        """
        Set the value of the DistrictID input for this Choreo. ((optional, string) The internal Education.com id of a school district.)
        """
        super(SchoolSearchInputSet, self)._set_input('DistrictID', value)
    def set_DistrictLEA(self, value):
        """
        Set the value of the DistrictLEA input for this Choreo. ((optional, string) The NCES Local Education Agency (LEA) id of a school district.)
        """
        super(SchoolSearchInputSet, self)._set_input('DistrictLEA', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) A latitude which serves as the center for distance searches. Please note that distance is required when using latitude and longitude parameters.)
        """
        super(SchoolSearchInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) A longitude which serves as the center for distance searches. Please note that distance is required when using latitude and longitude parameters.)
        """
        super(SchoolSearchInputSet, self)._set_input('Longitude', value)
    def set_MinResult(self, value):
        """
        Set the value of the MinResult input for this Choreo. ((optional, decimal) Minimum number of search results to return. The search will be expanded in increments of 0.5 miles until the minresult is reached. minResult is only valid for zip code and latitude/longitude requests.)
        """
        super(SchoolSearchInputSet, self)._set_input('MinResult', value)
    def set_NCES(self, value):
        """
        Set the value of the NCES input for this Choreo. ((optional, string) The National Center for Education Statistics (NCES) id of the school you want to find.)
        """
        super(SchoolSearchInputSet, self)._set_input('NCES', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        super(SchoolSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_SchoolID(self, value):
        """
        Set the value of the SchoolID input for this Choreo. ((optional, string) The Education.com id of the school you want to find.)
        """
        super(SchoolSearchInputSet, self)._set_input('SchoolID', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        super(SchoolSearchInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((conditional, integer) A five digit US postal code.)
        """
        super(SchoolSearchInputSet, self)._set_input('Zip', value)

class SchoolSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SchoolSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class SchoolSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SchoolSearchResultSet(response, path)
