# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserVideos
# Retrieves data about all videos watched by a specific user.
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

class GetUserVideos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserVideos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUserVideos, self).__init__(temboo_session, '/Library/KhanAcademy/Users/GetUserVideos')


    def new_input_set(self):
        return GetUserVideosInputSet()

    def _make_result_set(self, result, path):
        return GetUserVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserVideosChoreographyExecution(session, exec_id, path)

class GetUserVideosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserVideos
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Khan Academy.)
        """
        super(GetUserVideosInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The OAuth Consumer Secret provided by Khan Academy.)
        """
        super(GetUserVideosInputSet, self)._set_input('ConsumerSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address (coach or student ID) of user. If not provided, defaults to currently logged in user.)
        """
        super(GetUserVideosInputSet, self)._set_input('Email', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, string) The date/time to end searching for logs in UTC format: YYYY-mm-ddTHH:MM:SS (e.g., 2011-10-18T02:41:53).)
        """
        super(GetUserVideosInputSet, self)._set_input('EndTime', value)
    def set_OAuthTokenSecret(self, value):
        """
        Set the value of the OAuthTokenSecret input for this Choreo. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        super(GetUserVideosInputSet, self)._set_input('OAuthTokenSecret', value)
    def set_OAuthToken(self, value):
        """
        Set the value of the OAuthToken input for this Choreo. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        super(GetUserVideosInputSet, self)._set_input('OAuthToken', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, string) The date/time to start searching for logs in UTC format: YYYY-mm-ddTHH:MM:SS (e.g., 2011-10-18T02:41:53).)
        """
        super(GetUserVideosInputSet, self)._set_input('StartTime', value)

class GetUserVideosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserVideos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetUserVideosChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUserVideosResultSet(response, path)
