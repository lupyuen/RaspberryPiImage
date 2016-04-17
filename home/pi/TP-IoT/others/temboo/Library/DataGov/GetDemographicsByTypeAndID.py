# -*- coding: utf-8 -*-

###############################################################################
#
# GetDemographicsByTypeAndID
# Retrieve demographic data for a specified geography type and geography ID.
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

class GetDemographicsByTypeAndID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDemographicsByTypeAndID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDemographicsByTypeAndID, self).__init__(temboo_session, '/Library/DataGov/GetDemographicsByTypeAndID')


    def new_input_set(self):
        return GetDemographicsByTypeAndIDInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsByTypeAndIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsByTypeAndIDChoreographyExecution(session, exec_id, path)

class GetDemographicsByTypeAndIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDemographicsByTypeAndID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DataVersion(self, value):
        """
        Set the value of the DataVersion input for this Choreo. ((optional, string) Specify the census data version to search. Valid values are: jun2011, dec2011, jun2012, and dec2012.)
        """
        super(GetDemographicsByTypeAndIDInputSet, self)._set_input('DataVersion', value)
    def set_GeographyIDs(self, value):
        """
        Set the value of the GeographyIDs input for this Choreo. ((conditional, integer) The geography IDs to search for. Separate multiple IDs by commas; a maximum of 10 IDs are allowed.)
        """
        super(GetDemographicsByTypeAndIDInputSet, self)._set_input('GeographyIDs', value)
    def set_GeographyType(self, value):
        """
        Set the value of the GeographyType input for this Choreo. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        super(GetDemographicsByTypeAndIDInputSet, self)._set_input('GeographyType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetDemographicsByTypeAndIDInputSet, self)._set_input('ResponseFormat', value)

class GetDemographicsByTypeAndIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDemographicsByTypeAndID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetDemographicsByTypeAndIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDemographicsByTypeAndIDResultSet(response, path)
