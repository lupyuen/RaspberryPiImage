# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateWaterGoal
# Create or updates a user's water goal.
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

class UpdateWaterGoal(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateWaterGoal Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateWaterGoal, self).__init__(temboo_session, '/Library/Fitbit/Foods/UpdateWaterGoal')


    def new_input_set(self):
        return UpdateWaterGoalInputSet()

    def _make_result_set(self, result, path):
        return UpdateWaterGoalResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWaterGoalChoreographyExecution(session, exec_id, path)

class UpdateWaterGoalInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateWaterGoal
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('ConsumerSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('ResponseFormat', value)
    def set_Target(self, value):
        """
        Set the value of the Target input for this Choreo. ((conditional, decimal) The target water goal. Note that a water goal is created in units based on locale (fl. oz. for US and milliliters elsewhere).)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('Target', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(UpdateWaterGoalInputSet, self)._set_input('UserID', value)

class UpdateWaterGoalResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateWaterGoal Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class UpdateWaterGoalChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateWaterGoalResultSet(response, path)
