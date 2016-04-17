# -*- coding: utf-8 -*-

###############################################################################
#
# PropertyData
# Gets unique, total, or average data for of a single event and property over the last N days, weeks, or months.
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

class PropertyData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PropertyData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PropertyData, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/Properties/PropertyData')


    def new_input_set(self):
        return PropertyDataInputSet()

    def _make_result_set(self, result, path):
        return PropertyDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PropertyDataChoreographyExecution(session, exec_id, path)

class PropertyDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PropertyData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(PropertyDataInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(PropertyDataInputSet, self)._set_input('APISecret', value)
    def set_EventName(self, value):
        """
        Set the value of the EventName input for this Choreo. ((required, string) The name of the event that you wish to get data for.)
        """
        super(PropertyDataInputSet, self)._set_input('EventName', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(PropertyDataInputSet, self)._set_input('Expire', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((required, integer) The time interval to return. This relates to the value provided for Unit.)
        """
        super(PropertyDataInputSet, self)._set_input('Interval', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The maximum number of values to return. Defaults to 255.)
        """
        super(PropertyDataInputSet, self)._set_input('Limit', value)
    def set_PropertyName(self, value):
        """
        Set the value of the PropertyName input for this Choreo. ((required, string) The name of the property you would like to get data for.)
        """
        super(PropertyDataInputSet, self)._set_input('PropertyName', value)
    def set_PropertyValues(self, value):
        """
        Set the value of the PropertyValues input for this Choreo. ((optional, json) A JSON array containing property values that you wish to retrieve.)
        """
        super(PropertyDataInputSet, self)._set_input('PropertyValues', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and csv.)
        """
        super(PropertyDataInputSet, self)._set_input('ResponseFormat', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The analysis type you would like to get data for. Valid values are: general, unique, or average)
        """
        super(PropertyDataInputSet, self)._set_input('Type', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((required, string) The granularity of the data to return. Valid values are: minute, hour, day, week, or month.)
        """
        super(PropertyDataInputSet, self)._set_input('Unit', value)

class PropertyDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PropertyData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class PropertyDataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PropertyDataResultSet(response, path)
