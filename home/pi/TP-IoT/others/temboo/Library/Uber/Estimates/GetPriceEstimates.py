# -*- coding: utf-8 -*-

###############################################################################
#
# GetPriceEstimates
# Returns an estimated price range for each product offered at a given location.
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

class GetPriceEstimates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPriceEstimates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPriceEstimates, self).__init__(temboo_session, '/Library/Uber/Estimates/GetPriceEstimates')


    def new_input_set(self):
        return GetPriceEstimatesInputSet()

    def _make_result_set(self, result, path):
        return GetPriceEstimatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPriceEstimatesChoreographyExecution(session, exec_id, path)

class GetPriceEstimatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPriceEstimates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EndLatitude(self, value):
        """
        Set the value of the EndLatitude input for this Choreo. ((required, decimal) The latitude coordinate for the destination e.g., 40.650729.)
        """
        super(GetPriceEstimatesInputSet, self)._set_input('EndLatitude', value)
    def set_EndLongitude(self, value):
        """
        Set the value of the EndLongitude input for this Choreo. ((required, decimal) The longitude coordinate for the destination e.g., -74.009536.)
        """
        super(GetPriceEstimatesInputSet, self)._set_input('EndLongitude', value)
    def set_ServerToken(self, value):
        """
        Set the value of the ServerToken input for this Choreo. ((required, string) The Sever Token provided by Uber.)
        """
        super(GetPriceEstimatesInputSet, self)._set_input('ServerToken', value)
    def set_StartLatitude(self, value):
        """
        Set the value of the StartLatitude input for this Choreo. ((required, decimal) The latitude coordinate for the starting location e.g., 40.71863.)
        """
        super(GetPriceEstimatesInputSet, self)._set_input('StartLatitude', value)
    def set_StartLongitude(self, value):
        """
        Set the value of the StartLongitude input for this Choreo. ((required, decimal) The longitude coordinate for the starting location e.g., -74.005584.)
        """
        super(GetPriceEstimatesInputSet, self)._set_input('StartLongitude', value)

class GetPriceEstimatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPriceEstimates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Uber.)
        """
        return self._output.get('Response', None)

class GetPriceEstimatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPriceEstimatesResultSet(response, path)
