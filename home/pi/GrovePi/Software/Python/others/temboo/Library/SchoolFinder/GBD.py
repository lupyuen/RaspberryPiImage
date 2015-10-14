# -*- coding: utf-8 -*-

###############################################################################
#
# GBD
# Returns contextual and branding links to Education.com. 
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

class GBD(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GBD Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GBD, self).__init__(temboo_session, '/Library/SchoolFinder/GBD')


    def new_input_set(self):
        return GBDInputSet()

    def _make_result_set(self, result, path):
        return GBDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GBDChoreographyExecution(session, exec_id, path)

class GBDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GBD
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        super(GBDInputSet, self)._set_input('APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The name of a city. Must also be accompanied by the corresponding state parameter.)
        """
        super(GBDInputSet, self)._set_input('City', value)
    def set_DistrictID(self, value):
        """
        Set the value of the DistrictID input for this Choreo. ((conditional, string) The internal Education.com id of a school district.)
        """
        super(GBDInputSet, self)._set_input('DistrictID', value)
    def set_NCES(self, value):
        """
        Set the value of the NCES input for this Choreo. ((conditional, string) The nces id of the school.)
        """
        super(GBDInputSet, self)._set_input('NCES', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        super(GBDInputSet, self)._set_input('ResponseFormat', value)
    def set_SchoolID(self, value):
        """
        Set the value of the SchoolID input for this Choreo. ((conditional, string) The id of the school.)
        """
        super(GBDInputSet, self)._set_input('SchoolID', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        super(GBDInputSet, self)._set_input('State', value)

class GBDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GBD Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class GBDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GBDResultSet(response, path)
