# -*- coding: utf-8 -*-

###############################################################################
#
# GetStudentStats
# Returns student statistics for a single school, city, or state. 
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

class GetStudentStats(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetStudentStats Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetStudentStats, self).__init__(temboo_session, '/Library/SchoolFinder/GetStudentStats')


    def new_input_set(self):
        return GetStudentStatsInputSet()

    def _make_result_set(self, result, path):
        return GetStudentStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStudentStatsChoreographyExecution(session, exec_id, path)

class GetStudentStatsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetStudentStats
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        super(GetStudentStatsInputSet, self)._set_input('APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The name of a city. Please note cities composed of two words should be formatted with a plus sign e.g. “san+Francisco.” City requests must also be accompanied by the corresponding state parameter.)
        """
        super(GetStudentStatsInputSet, self)._set_input('City', value)
    def set_DistrictID(self, value):
        """
        Set the value of the DistrictID input for this Choreo. ((conditional, string) The education.com district id.)
        """
        super(GetStudentStatsInputSet, self)._set_input('DistrictID', value)
    def set_DistrictLEA(self, value):
        """
        Set the value of the DistrictLEA input for this Choreo. ((conditional, string) The LEA id of the district.)
        """
        super(GetStudentStatsInputSet, self)._set_input('DistrictLEA', value)
    def set_NCES(self, value):
        """
        Set the value of the NCES input for this Choreo. ((conditional, string) The National Center for Education Statistics (NCES) id of the school.)
        """
        super(GetStudentStatsInputSet, self)._set_input('NCES', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((conditional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        super(GetStudentStatsInputSet, self)._set_input('ResponseFormat', value)
    def set_SchoolID(self, value):
        """
        Set the value of the SchoolID input for this Choreo. ((conditional, string) The Education.com id of the school you want to find.)
        """
        super(GetStudentStatsInputSet, self)._set_input('SchoolID', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        super(GetStudentStatsInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) A five digit US postal code.)
        """
        super(GetStudentStatsInputSet, self)._set_input('Zip', value)

class GetStudentStatsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetStudentStats Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class GetStudentStatsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetStudentStatsResultSet(response, path)
