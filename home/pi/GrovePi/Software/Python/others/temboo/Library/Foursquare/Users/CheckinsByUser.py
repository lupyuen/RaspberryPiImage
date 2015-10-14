# -*- coding: utf-8 -*-

###############################################################################
#
# CheckinsByUser
# Retrieve a list of check-ins for an authenticated user.
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

class CheckinsByUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CheckinsByUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CheckinsByUser, self).__init__(temboo_session, '/Library/Foursquare/Users/CheckinsByUser')


    def new_input_set(self):
        return CheckinsByUserInputSet()

    def _make_result_set(self, result, path):
        return CheckinsByUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckinsByUserChoreographyExecution(session, exec_id, path)

class CheckinsByUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CheckinsByUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimeStamp(self, value):
        """
        Set the value of the AfterTimeStamp input for this Choreo. ((optional, date) Retrieve the first results after the seconds entered since epoch time.)
        """
        super(CheckinsByUserInputSet, self)._set_input('AfterTimeStamp', value)
    def set_BeforeTimeStamp(self, value):
        """
        Set the value of the BeforeTimeStamp input for this Choreo. ((optional, date) Retrieve the first results prior to the seconds specified. Useful for paging backward in time.)
        """
        super(CheckinsByUserInputSet, self)._set_input('BeforeTimeStamp', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The total number of results to be returned, up to 250.)
        """
        super(CheckinsByUserInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(CheckinsByUserInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The number of results to skip. Used to page through results.)
        """
        super(CheckinsByUserInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CheckinsByUserInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Only 'self' is supported at this moment by the Foursquare API. Defaults to: self.)
        """
        super(CheckinsByUserInputSet, self)._set_input('UserID', value)

class CheckinsByUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CheckinsByUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CheckinsByUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CheckinsByUserResultSet(response, path)
