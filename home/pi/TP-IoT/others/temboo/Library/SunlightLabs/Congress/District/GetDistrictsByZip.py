# -*- coding: utf-8 -*-

###############################################################################
#
# GetDistrictsByZip
# Returns all districts that overlap the area for a given zip code.
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

class GetDistrictsByZip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDistrictsByZip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDistrictsByZip, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/District/GetDistrictsByZip')


    def new_input_set(self):
        return GetDistrictsByZipInputSet()

    def _make_result_set(self, result, path):
        return GetDistrictsByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDistrictsByZipChoreographyExecution(session, exec_id, path)

class GetDistrictsByZipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDistrictsByZip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetDistrictsByZipInputSet, self)._set_input('APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetDistrictsByZipInputSet, self)._set_input('ResponseFormat', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) The zip code for the districts to return.)
        """
        super(GetDistrictsByZipInputSet, self)._set_input('Zip', value)

class GetDistrictsByZipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDistrictsByZip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetDistrictsByZipChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDistrictsByZipResultSet(response, path)
