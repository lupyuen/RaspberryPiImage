# -*- coding: utf-8 -*-

###############################################################################
#
# GetBodyMetrics
# Retrieves body metrics for the specified user.
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

class GetBodyMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBodyMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBodyMetrics, self).__init__(temboo_session, '/Library/Withings/Measure/GetBodyMetrics')


    def new_input_set(self):
        return GetBodyMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetBodyMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBodyMetricsChoreographyExecution(session, exec_id, path)

class GetBodyMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBodyMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, integer) Set to 2 to retrieve objectives or to 1 to retrieve actual measurements.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('Category', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Withings.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Withings.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('ConsumerSecret', value)
    def set_DeviceType(self, value):
        """
        Set the value of the DeviceType input for this Choreo. ((optional, integer) Retrieves data for a particular device type. Specifying 1 will retrieve all body scale related measures and 0 will retrieve all user personal data entered at user creation time.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('DeviceType', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Retrieves results dated before the specified EPOCH formatted date.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('EndDate', value)
    def set_LastUpdated(self, value):
        """
        Set the value of the LastUpdated input for this Choreo. ((optional, date) Retrieves results added or modified since the specified EPOCH formatted date.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('LastUpdated', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of measure groups returned in the result.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('Limit', value)
    def set_MeasurementType(self, value):
        """
        Set the value of the MeasurementType input for this Choreo. ((optional, integer) Filters by the measurement type. Set to 1 to filter by weight or 4 to filter by height.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('MeasurementType', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used in combination with the Limit parameter to page through results.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('Offset', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Retrieves results dated after the specified EPOCH formatted date.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('StartDate', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to retrieve body metrics for.)
        """
        super(GetBodyMetricsInputSet, self)._set_input('UserID', value)

class GetBodyMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBodyMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class GetBodyMetricsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBodyMetricsResultSet(response, path)
