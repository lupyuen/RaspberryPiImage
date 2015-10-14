# -*- coding: utf-8 -*-

###############################################################################
#
# Share
# Allows you to share an album with one or more Last.fm users or other friends.
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

class Share(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Share Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Share, self).__init__(temboo_session, '/Library/LastFm/Album/Share')


    def new_input_set(self):
        return ShareInputSet()

    def _make_result_set(self, result, path):
        return ShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShareChoreographyExecution(session, exec_id, path)

class ShareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Share
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(ShareInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((string) Your Last.fm API Secret.)
        """
        super(ShareInputSet, self)._set_input('APISecret', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((string) The album name.)
        """
        super(ShareInputSet, self)._set_input('Album', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((string) The artist name.)
        """
        super(ShareInputSet, self)._set_input('Artist', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) An optional message to send with the recommendation. If not supplied a default message will be used.)
        """
        super(ShareInputSet, self)._set_input('Message', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((optional, boolean) Optionally show in the sharing users activity feed. Defaults to 0 (false).)
        """
        super(ShareInputSet, self)._set_input('Public', value)
    def set_Recipient(self, value):
        """
        Set the value of the Recipient input for this Choreo. ((string) A comma delimited list of email addresses or Last.fm usernames. Maximum is 10.)
        """
        super(ShareInputSet, self)._set_input('Recipient', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        super(ShareInputSet, self)._set_input('SessionKey', value)

class ShareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Share Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class ShareChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ShareResultSet(response, path)
