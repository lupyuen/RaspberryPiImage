# -*- coding: utf-8 -*-

###############################################################################
#
# GetLatestActivity
# Gets a user's latest activity.
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

class GetLatestActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLatestActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLatestActivity, self).__init__(temboo_session, '/Library/Fitbit/Activities/GetLatestActivity')


    def new_input_set(self):
        return GetLatestActivityInputSet()

    def _make_result_set(self, result, path):
        return GetLatestActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLatestActivityChoreographyExecution(session, exec_id, path)

class GetLatestActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLatestActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetLatestActivityInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetLatestActivityInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(GetLatestActivityInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(GetLatestActivityInputSet, self)._set_input('ConsumerSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(GetLatestActivityInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(GetLatestActivityInputSet, self)._set_input('UserID', value)

class GetLatestActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLatestActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)
    def get_ActivityID(self):
        """
        Retrieve the value for the "ActivityID" output from this Choreo execution. ((string) The ID of the activity.)
        """
        return self._output.get('ActivityID', None)
    def get_Calories(self):
        """
        Retrieve the value for the "Calories" output from this Choreo execution. ((integer) Calories burned during this activity.)
        """
        return self._output.get('Calories', None)
    def get_Description(self):
        """
        Retrieve the value for the "Description" output from this Choreo execution. ((string) The description of the activity.)
        """
        return self._output.get('Description', None)
    def get_Distance(self):
        """
        Retrieve the value for the "Distance" output from this Choreo execution. ((decimal) The distance traveled during the activity.)
        """
        return self._output.get('Distance', None)
    def get_Duration(self):
        """
        Retrieve the value for the "Duration" output from this Choreo execution. ((integer) The duration of the activity (in milliseconds).)
        """
        return self._output.get('Duration', None)
    def get_Name(self):
        """
        Retrieve the value for the "Name" output from this Choreo execution. ((string) The name of the activity.)
        """
        return self._output.get('Name', None)

class GetLatestActivityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLatestActivityResultSet(response, path)
