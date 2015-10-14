# -*- coding: utf-8 -*-

###############################################################################
#
# Civic
# Retrieves a host of information about the district and representatives of a specified location.
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

class Civic(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Civic Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Civic, self).__init__(temboo_session, '/Library/Labs/GoodCitizen/Civic')


    def new_input_set(self):
        return CivicInputSet()

    def _make_result_set(self, result, path):
        return CivicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CivicChoreographyExecution(session, exec_id, path)

class CivicInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Civic
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((conditional, json) A JSON dictionary containing credentials for Sunlight Labs and LittleSis. If this input is set, a Sunset Labs key must be present. See Choreo notes for formatting examples.)
        """
        super(CivicInputSet, self)._set_input('APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of your location.)
        """
        super(CivicInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Set the number of records to return for the bills, votes, and relationships of each legislator. Defaults to 5.)
        """
        super(CivicInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate of your locaion.)
        """
        super(CivicInputSet, self)._set_input('Longitude', value)

class CivicResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Civic Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from the Civic Choreo.)
        """
        return self._output.get('Response', None)

class CivicChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CivicResultSet(response, path)
