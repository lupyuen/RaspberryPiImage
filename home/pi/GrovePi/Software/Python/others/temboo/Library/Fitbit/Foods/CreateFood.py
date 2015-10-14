# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFood
# Create new private food for a user.
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

class CreateFood(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFood Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateFood, self).__init__(temboo_session, '/Library/Fitbit/Foods/CreateFood')


    def new_input_set(self):
        return CreateFoodInputSet()

    def _make_result_set(self, result, path):
        return CreateFoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFoodChoreographyExecution(session, exec_id, path)

class CreateFoodInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFood
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CreateFoodInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateFoodInputSet, self)._set_input('AccessToken', value)
    def set_Calories(self, value):
        """
        Set the value of the Calories input for this Choreo. ((required, integer) The number of calories per serving size.)
        """
        super(CreateFoodInputSet, self)._set_input('Calories', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(CreateFoodInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(CreateFoodInputSet, self)._set_input('ConsumerSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the food entry.)
        """
        super(CreateFoodInputSet, self)._set_input('Description', value)
    def set_FormType(self, value):
        """
        Set the value of the FormType input for this Choreo. ((optional, string) Form type; (LIQUID or DRY).)
        """
        super(CreateFoodInputSet, self)._set_input('FormType', value)
    def set_MeasurementUnitID(self, value):
        """
        Set the value of the MeasurementUnitID input for this Choreo. ((required, integer) The default measurement unit.)
        """
        super(CreateFoodInputSet, self)._set_input('MeasurementUnitID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the food.)
        """
        super(CreateFoodInputSet, self)._set_input('Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(CreateFoodInputSet, self)._set_input('ResponseFormat', value)
    def set_ServingSize(self, value):
        """
        Set the value of the ServingSize input for this Choreo. ((required, integer) The default serving size.)
        """
        super(CreateFoodInputSet, self)._set_input('ServingSize', value)

class CreateFoodResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFood Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class CreateFoodChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateFoodResultSet(response, path)
