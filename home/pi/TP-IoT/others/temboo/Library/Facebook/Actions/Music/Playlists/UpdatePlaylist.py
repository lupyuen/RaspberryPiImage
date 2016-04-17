# -*- coding: utf-8 -*-

###############################################################################
#
# UpdatePlaylist
# Updates an existing playlist action.
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

class UpdatePlaylist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdatePlaylist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdatePlaylist, self).__init__(temboo_session, '/Library/Facebook/Actions/Music/Playlists/UpdatePlaylist')


    def new_input_set(self):
        return UpdatePlaylistInputSet()

    def _make_result_set(self, result, path):
        return UpdatePlaylistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdatePlaylistChoreographyExecution(session, exec_id, path)

class UpdatePlaylistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdatePlaylist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('ActionID', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(UpdatePlaylistInputSet, self)._set_input('EndTime', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this fitness action. Setting this parameter requires enabling of message capabilities.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('Message', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('Place', value)
    def set_PlayList(self, value):
        """
        Set the value of the PlayList input for this Choreo. ((optional, string) An object representing a playlist)
        """
        super(UpdatePlaylistInputSet, self)._set_input('PlayList', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('ResponseFormat', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        super(UpdatePlaylistInputSet, self)._set_input('Tags', value)

class UpdatePlaylistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdatePlaylist Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UpdatePlaylistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdatePlaylistResultSet(response, path)
