# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserInfo
# Updates a user's profile data.
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

class UpdateUserInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUserInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateUserInfo, self).__init__(temboo_session, '/Library/Fitbit/Profile/UpdateUserInfo')


    def new_input_set(self):
        return UpdateUserInfoInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserInfoChoreographyExecution(session, exec_id, path)

class UpdateUserInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUserInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AboutMe(self, value):
        """
        Set the value of the AboutMe input for this Choreo. ((optional, string) The user's About Me string.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('AboutMe', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('AccessToken', value)
    def set_Birthday(self, value):
        """
        Set the value of the Birthday input for this Choreo. ((optional, date) Date of Birth; in the format yyyy-MM-dd.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Birthday', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The user's city information.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('City', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('ConsumerSecret', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) The two-character code for the user's country.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Country', value)
    def set_FoodLocale(self, value):
        """
        Set the value of the FoodLocale input for this Choreo. ((optional, string) Food Database Locale; in the format "xx_XX".)
        """
        super(UpdateUserInfoInputSet, self)._set_input('FoodLocale', value)
    def set_FullName(self, value):
        """
        Set the value of the FullName input for this Choreo. ((optional, string) The user's full name.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('FullName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) The user's gender (MALE/FEMALE/NA).)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Gender', value)
    def set_GlucoseUnit(self, value):
        """
        Set the value of the GlucoseUnit input for this Choreo. ((optional, decimal) The blood glucose unit of measurement being used. Valid values are: en_US, any,  METRIC.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('GlucoseUnit', value)
    def set_HeightUnit(self, value):
        """
        Set the value of the HeightUnit input for this Choreo. ((optional, decimal) The height unit being used. Valid values are: en_US, any,  METRIC.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('HeightUnit', value)
    def set_Height(self, value):
        """
        Set the value of the Height input for this Choreo. ((optional, decimal) The user's height; in the format X.XX (inches).)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Height', value)
    def set_Locale(self, value):
        """
        Set the value of the Locale input for this Choreo. ((optional, string) Locale of website (country/language); one of the locales, currently – (en_US, fr_FR, de_DE, es_ES, en_GB, en_AU, en_NZ, ja_JP).)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Locale', value)
    def set_Nickname(self, value):
        """
        Set the value of the Nickname input for this Choreo. ((optional, string) The user's nickname.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('Nickname', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The two-character state abbreviation for the user.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('State', value)
    def set_StrideLengthRunning(self, value):
        """
        Set the value of the StrideLengthRunning input for this Choreo. ((optional, decimal) Running stride length; in the format X.XX.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('StrideLengthRunning', value)
    def set_StrideLengthWalking(self, value):
        """
        Set the value of the StrideLengthWalking input for this Choreo. ((optional, decimal) Walking stride length; in the format X.XX.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('StrideLengthWalking', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) The user's timezone; in the format "America/Los_Angeles")
        """
        super(UpdateUserInfoInputSet, self)._set_input('Timezone', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('UserID', value)
    def set_WaterUnit(self, value):
        """
        Set the value of the WaterUnit input for this Choreo. ((optional, decimal) The water unit being used. Valid values are: en_US, any,  METRIC.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('WaterUnit', value)
    def set_WeightUnit(self, value):
        """
        Set the value of the WeightUnit input for this Choreo. ((optional, string) The weight unit being used. Valid values are: en_US, any,  METRIC.)
        """
        super(UpdateUserInfoInputSet, self)._set_input('WeightUnit', value)

class UpdateUserInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUserInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class UpdateUserInfoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateUserInfoResultSet(response, path)
