# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveLatestActivity
# Returns the latest activity from a user's fitness activity history.
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

class RetrieveLatestActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveLatestActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveLatestActivity, self).__init__(temboo_session, '/Library/RunKeeper/FitnessActivities/RetrieveLatestActivity')


    def new_input_set(self):
        return RetrieveLatestActivityInputSet()

    def _make_result_set(self, result, path):
        return RetrieveLatestActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveLatestActivityChoreographyExecution(session, exec_id, path)

class RetrieveLatestActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveLatestActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(RetrieveLatestActivityInputSet, self)._set_input('AccessToken', value)

class RetrieveLatestActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveLatestActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)
    def get_BeginTime(self):
        """
        Retrieve the value for the "BeginTime" output from this Choreo execution. ((date) The start time of the latest activity.)
        """
        return self._output.get('BeginTime', None)
    def get_Climb(self):
        """
        Retrieve the value for the "Climb" output from this Choreo execution. ((decimal) The total elevation climbed over the course of the activity, in meters.)
        """
        return self._output.get('Climb', None)
    def get_Duration(self):
        """
        Retrieve the value for the "Duration" output from this Choreo execution. ((integer) The duration of the activity, in seconds.)
        """
        return self._output.get('Duration', None)
    def get_Equipment(self):
        """
        Retrieve the value for the "Equipment" output from this Choreo execution. ((string) The equipment used to complete this activity.)
        """
        return self._output.get('Equipment', None)
    def get_Notes(self):
        """
        Retrieve the value for the "Notes" output from this Choreo execution. ((string) Any notes that the user has associated with the activity.)
        """
        return self._output.get('Notes', None)
    def get_TotalCalories(self):
        """
        Retrieve the value for the "TotalCalories" output from this Choreo execution. ((integer) The total calories burned (omitted if not available).)
        """
        return self._output.get('TotalCalories', None)
    def get_TotalDistance(self):
        """
        Retrieve the value for the "TotalDistance" output from this Choreo execution. ((decimal) The total distance traveled, in meters.)
        """
        return self._output.get('TotalDistance', None)
    def get_Type(self):
        """
        Retrieve the value for the "Type" output from this Choreo execution. ((string) The type of activity.)
        """
        return self._output.get('Type', None)
    def get_URI(self):
        """
        Retrieve the value for the "URI" output from this Choreo execution. ((string) The URI of the activity.)
        """
        return self._output.get('URI', None)

class RetrieveLatestActivityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveLatestActivityResultSet(response, path)
