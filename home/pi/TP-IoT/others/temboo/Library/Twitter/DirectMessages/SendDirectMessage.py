# -*- coding: utf-8 -*-

###############################################################################
#
# SendDirectMessage
# Sends a new direct message to the specified user from the authenticating user.
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

class SendDirectMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendDirectMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendDirectMessage, self).__init__(temboo_session, '/Library/Twitter/DirectMessages/SendDirectMessage')


    def new_input_set(self):
        return SendDirectMessageInputSet()

    def _make_result_set(self, result, path):
        return SendDirectMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendDirectMessageChoreographyExecution(session, exec_id, path)

class SendDirectMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendDirectMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(SendDirectMessageInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(SendDirectMessageInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(SendDirectMessageInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(SendDirectMessageInputSet, self)._set_input('ConsumerSecret', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name of the user who should receive the direct message. Required unless specifying the UserId.)
        """
        super(SendDirectMessageInputSet, self)._set_input('ScreenName', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text for the direct message. Max characters is 140.)
        """
        super(SendDirectMessageInputSet, self)._set_input('Text', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The ID of the user who should receive the direct message. Required unless specifying the ScreenName.)
        """
        super(SendDirectMessageInputSet, self)._set_input('UserID', value)

class SendDirectMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendDirectMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class SendDirectMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendDirectMessageResultSet(response, path)
