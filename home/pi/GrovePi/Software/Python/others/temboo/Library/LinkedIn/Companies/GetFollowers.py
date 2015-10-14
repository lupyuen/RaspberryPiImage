# -*- coding: utf-8 -*-

###############################################################################
#
# GetFollowers
# Returns a company's followers, by segment.
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

class GetFollowers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFollowers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetFollowers, self).__init__(temboo_session, '/Library/LinkedIn/Companies/GetFollowers')


    def new_input_set(self):
        return GetFollowersInputSet()

    def _make_result_set(self, result, path):
        return GetFollowersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFollowersChoreographyExecution(session, exec_id, path)

class GetFollowersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFollowers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the Client ID).)
        """
        super(GetFollowersInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process (AKA the OAuth User Secret).)
        """
        super(GetFollowersInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process (AKA the OAuth User Token).)
        """
        super(GetFollowersInputSet, self)._set_input('AccessToken', value)
    def set_CompanyID(self, value):
        """
        Set the value of the CompanyID input for this Choreo. ((required, integer) A LinkedIn assigned ID associated with the company.)
        """
        super(GetFollowersInputSet, self)._set_input('CompanyID', value)
    def set_CompanySizes(self, value):
        """
        Set the value of the CompanySizes input for this Choreo. ((optional, string) Used to segment by a particular company size targeting code. See Choreo notes for more details.)
        """
        super(GetFollowersInputSet, self)._set_input('CompanySizes', value)
    def set_GeographicArea(self, value):
        """
        Set the value of the GeographicArea input for this Choreo. ((optional, string) Used to segment by a particular geographic area. See Choreo notes for more details.)
        """
        super(GetFollowersInputSet, self)._set_input('GeographicArea', value)
    def set_Industries(self, value):
        """
        Set the value of the Industries input for this Choreo. ((optional, string) Used to segment by member industry. See Choreo notes for more details.)
        """
        super(GetFollowersInputSet, self)._set_input('Industries', value)
    def set_JobFunction(self, value):
        """
        Set the value of the JobFunction input for this Choreo. ((optional, string) Used to segment by member job function targeting code. See Choreo notes for more details.)
        """
        super(GetFollowersInputSet, self)._set_input('JobFunction', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetFollowersInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the Client Secret).)
        """
        super(GetFollowersInputSet, self)._set_input('SecretKey', value)
    def set_SeniorityLevel(self, value):
        """
        Set the value of the SeniorityLevel input for this Choreo. ((optional, string) Used to segment by member seniority level targeting code. See Choreo notes for more details.)
        """
        super(GetFollowersInputSet, self)._set_input('SeniorityLevel', value)

class GetFollowersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFollowers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetFollowersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetFollowersResultSet(response, path)
