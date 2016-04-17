# -*- coding: utf-8 -*-

###############################################################################
#
# EventData
# Gets unique, total, or average data for a set of events over the last N days, weeks, or months.
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

class EventData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EventData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EventData, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/Events/EventData')


    def new_input_set(self):
        return EventDataInputSet()

    def _make_result_set(self, result, path):
        return EventDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EventDataChoreographyExecution(session, exec_id, path)

class EventDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EventData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(EventDataInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(EventDataInputSet, self)._set_input('APISecret', value)
    def set_EventNames(self, value):
        """
        Set the value of the EventNames input for this Choreo. ((required, json) A JSON array containing the event or events you wish to get data for.)
        """
        super(EventDataInputSet, self)._set_input('EventNames', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(EventDataInputSet, self)._set_input('Expire', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((required, integer) The time interval to return. This relates to the value provided for Unit.)
        """
        super(EventDataInputSet, self)._set_input('Interval', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and csv.)
        """
        super(EventDataInputSet, self)._set_input('ResponseFormat', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The analysis type you would like to get data for. Valid values are: general, unique, or average)
        """
        super(EventDataInputSet, self)._set_input('Type', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((required, string) The granularity of the data to return. Valid values are: minute, hour, day, week, or month.)
        """
        super(EventDataInputSet, self)._set_input('Unit', value)

class EventDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EventData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class EventDataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EventDataResultSet(response, path)
