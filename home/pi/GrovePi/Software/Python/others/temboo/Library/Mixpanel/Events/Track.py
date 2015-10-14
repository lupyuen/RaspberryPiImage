# -*- coding: utf-8 -*-

###############################################################################
#
# Track
# Records an event in Mixpanel.
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

class Track(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Track Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Track, self).__init__(temboo_session, '/Library/Mixpanel/Events/Track')


    def new_input_set(self):
        return TrackInputSet()

    def _make_result_set(self, result, path):
        return TrackResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackChoreographyExecution(session, exec_id, path)

class TrackInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Track
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DistinctID(self, value):
        """
        Set the value of the DistinctID input for this Choreo. ((optional, string) Used to uniquely identify a user associated with your event. When provided, you can track a given user through funnels and distinguish unique users for retention analyses.)
        """
        super(TrackInputSet, self)._set_input('DistinctID', value)
    def set_EventName(self, value):
        """
        Set the value of the EventName input for this Choreo. ((required, string) A name for the event (e.g., Signed Up, Uploaded Photo, etc).)
        """
        super(TrackInputSet, self)._set_input('EventName', value)
    def set_EventProperties(self, value):
        """
        Set the value of the EventProperties input for this Choreo. ((optional, json) Additional properties associated with the event formatted as name/value pairs in a JSON object. These properties can be used for segmentation and funnels.)
        """
        super(TrackInputSet, self)._set_input('EventProperties', value)
    def set_IP(self, value):
        """
        Set the value of the IP input for this Choreo. ((optional, string) An IP address string associated with the event (e.g., 127.0.0.1). When set to 0 (the default) Mixpanel will ignore IP information.)
        """
        super(TrackInputSet, self)._set_input('IP', value)
    def set_Time(self, value):
        """
        Set the value of the Time input for this Choreo. ((optional, date) A unix timestamp representing the time the event occurred. If not provided, Mixpanel will use the time the event arrives at the server.)
        """
        super(TrackInputSet, self)._set_input('Time', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The token provided by Mixpanel. You can find your Mixpanel token in the project settings dialog in the Mixpanel app.)
        """
        super(TrackInputSet, self)._set_input('Token', value)
    def set_Verbose(self, value):
        """
        Set the value of the Verbose input for this Choreo. ((optional, boolean) When set to 1, the response will contain more information describing the success or failure of the tracking call.)
        """
        super(TrackInputSet, self)._set_input('Verbose', value)

class TrackResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Track Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class TrackChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TrackResultSet(response, path)
