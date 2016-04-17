# -*- coding: utf-8 -*-

###############################################################################
#
# GetBadges
# Retrieves a list of all badges, and if a user is logged in, retrieves additional information about the badges that user has earned.
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

class GetBadges(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBadges Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBadges, self).__init__(temboo_session, '/Library/KhanAcademy/Badges/GetBadges')


    def new_input_set(self):
        return GetBadgesInputSet()

    def _make_result_set(self, result, path):
        return GetBadgesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBadgesChoreographyExecution(session, exec_id, path)

class GetBadgesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBadges
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((optional, string) The Consumer Key provided by Khan Academy.)
        """
        super(GetBadgesInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((optional, string) The OAuth Consumer Secret provided by Khan Academy.)
        """
        super(GetBadgesInputSet, self)._set_input('ConsumerSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address (coach or student ID) of user. If not provided, defaults to currently logged in user in the case when authentication credentials are provided.)
        """
        super(GetBadgesInputSet, self)._set_input('Email', value)
    def set_OAuthTokenSecret(self, value):
        """
        Set the value of the OAuthTokenSecret input for this Choreo. ((optional, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        super(GetBadgesInputSet, self)._set_input('OAuthTokenSecret', value)
    def set_OAuthToken(self, value):
        """
        Set the value of the OAuthToken input for this Choreo. ((optional, string) The OAuth Token retrieved during the OAuth process.)
        """
        super(GetBadgesInputSet, self)._set_input('OAuthToken', value)

class GetBadgesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBadges Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetBadgesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBadgesResultSet(response, path)
