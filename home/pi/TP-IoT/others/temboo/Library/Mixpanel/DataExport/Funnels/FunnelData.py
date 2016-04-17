# -*- coding: utf-8 -*-

###############################################################################
#
# FunnelData
# Gets data for a specified funnel.
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

class FunnelData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FunnelData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FunnelData, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/Funnels/FunnelData')


    def new_input_set(self):
        return FunnelDataInputSet()

    def _make_result_set(self, result, path):
        return FunnelDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FunnelDataChoreographyExecution(session, exec_id, path)

class FunnelDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FunnelData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(FunnelDataInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(FunnelDataInputSet, self)._set_input('APISecret', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(FunnelDataInputSet, self)._set_input('Expire', value)
    def set_FromDate(self, value):
        """
        Set the value of the FromDate input for this Choreo. ((optional, date) The first date in yyyy-mm-dd format from which a user can begin the first step in the funnel. This date is inclusive.)
        """
        super(FunnelDataInputSet, self)._set_input('FromDate', value)
    def set_FunnelID(self, value):
        """
        Set the value of the FunnelID input for this Choreo. ((required, string) The ID of the funnel to get data for.)
        """
        super(FunnelDataInputSet, self)._set_input('FunnelID', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((optional, integer) The number of days you want your results bucketed into.The default value is 1.)
        """
        super(FunnelDataInputSet, self)._set_input('Interval', value)
    def set_Length(self, value):
        """
        Set the value of the Length input for this Choreo. ((optional, integer) The number of days each user has to complete the funnel, starting from the time they triggered the first step in the funnel. May not be greater than 60 days. Defaults to 14.)
        """
        super(FunnelDataInputSet, self)._set_input('Length', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Return the top limit property values. This parameter is ignored if the On input is not specified.)
        """
        super(FunnelDataInputSet, self)._set_input('Limit', value)
    def set_On(self, value):
        """
        Set the value of the On input for this Choreo. ((optional, string) The property expression to segment the event on (e.g., properties["Referred By"] == "Friend"). See Choreo description for examples.)
        """
        super(FunnelDataInputSet, self)._set_input('On', value)
    def set_ToDate(self, value):
        """
        Set the value of the ToDate input for this Choreo. ((optional, date) The last date in yyyy-mm-dd format from which a user can begin the first step in the funnel. This date is inclusive. The date range may not be more than 60 days.)
        """
        super(FunnelDataInputSet, self)._set_input('ToDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) This is an alternate way of specifying interval and can set to be 'day' or 'week'.)
        """
        super(FunnelDataInputSet, self)._set_input('Unit', value)
    def set_Where(self, value):
        """
        Set the value of the Where input for this Choreo. ((optional, string) An expression to filter events by  (e.g., properties["Signed Up"]). See Choreo description for examples.)
        """
        super(FunnelDataInputSet, self)._set_input('Where', value)

class FunnelDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FunnelData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class FunnelDataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FunnelDataResultSet(response, path)
