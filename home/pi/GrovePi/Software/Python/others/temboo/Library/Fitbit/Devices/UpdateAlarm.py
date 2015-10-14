# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAlarm
# Updates an existing alarm entry for a given device.
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

class UpdateAlarm(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAlarm Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateAlarm, self).__init__(temboo_session, '/Library/Fitbit/Devices/UpdateAlarm')


    def new_input_set(self):
        return UpdateAlarmInputSet()

    def _make_result_set(self, result, path):
        return UpdateAlarmResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAlarmChoreographyExecution(session, exec_id, path)

class UpdateAlarmInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAlarm
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(UpdateAlarmInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(UpdateAlarmInputSet, self)._set_input('AccessToken', value)
    def set_AlarmID(self, value):
        """
        Set the value of the AlarmID input for this Choreo. ((required, string) The ID of the alarm to update.)
        """
        super(UpdateAlarmInputSet, self)._set_input('AlarmID', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(UpdateAlarmInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(UpdateAlarmInputSet, self)._set_input('ConsumerSecret', value)
    def set_DeviceID(self, value):
        """
        Set the value of the DeviceID input for this Choreo. ((required, string) The id of the device you would like to manage the alarm on.)
        """
        super(UpdateAlarmInputSet, self)._set_input('DeviceID', value)
    def set_Enabled(self, value):
        """
        Set the value of the Enabled input for this Choreo. ((required, boolean) Indicates whether or not the alarm is enabled. Valid values are: true and false.)
        """
        super(UpdateAlarmInputSet, self)._set_input('Enabled', value)
    def set_Label(self, value):
        """
        Set the value of the Label input for this Choreo. ((optional, string) A label for the alarm.)
        """
        super(UpdateAlarmInputSet, self)._set_input('Label', value)
    def set_Recurring(self, value):
        """
        Set the value of the Recurring input for this Choreo. ((required, boolean) Specifies if this is a one-time or recurring alarm. Valid values are: true or false. When adding a recurring alarm, the WeekDays input is required.)
        """
        super(UpdateAlarmInputSet, self)._set_input('Recurring', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(UpdateAlarmInputSet, self)._set_input('ResponseFormat', value)
    def set_SnoozeCount(self, value):
        """
        Set the value of the SnoozeCount input for this Choreo. ((required, integer) The maximum snooze count.)
        """
        super(UpdateAlarmInputSet, self)._set_input('SnoozeCount', value)
    def set_SnoozeLength(self, value):
        """
        Set the value of the SnoozeLength input for this Choreo. ((required, integer) The number of minutes in between alarms when using the snooze option.)
        """
        super(UpdateAlarmInputSet, self)._set_input('SnoozeLength', value)
    def set_Time(self, value):
        """
        Set the value of the Time input for this Choreo. ((required, string) The time of the alarm in the format XX:XX+XX:XX (the hour, minute, and time offset from UTC). This will be converted to the timezone of the user's profile.)
        """
        super(UpdateAlarmInputSet, self)._set_input('Time', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(UpdateAlarmInputSet, self)._set_input('UserID', value)
    def set_Vibe(self, value):
        """
        Set the value of the Vibe input for this Choreo. ((optional, string) The vibe pattern. Currently this only has one accepted value: DEFAULT.)
        """
        super(UpdateAlarmInputSet, self)._set_input('Vibe', value)
    def set_WeekDays(self, value):
        """
        Set the value of the WeekDays input for this Choreo. ((required, string) Specifies the days of the week that the alarm is active. Required when specifying a "recurring" alarm. Multiple days can be specified in a comma-separated list (e.g., MONDAY,TUESDAY,WEDNESDAY).)
        """
        super(UpdateAlarmInputSet, self)._set_input('WeekDays', value)

class UpdateAlarmResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAlarm Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class UpdateAlarmChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateAlarmResultSet(response, path)
