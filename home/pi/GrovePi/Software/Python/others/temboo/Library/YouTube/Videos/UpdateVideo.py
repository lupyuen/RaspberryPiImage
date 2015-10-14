# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateVideo
# Updates a video's metadata.
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

class UpdateVideo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateVideo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateVideo, self).__init__(temboo_session, '/Library/YouTube/Videos/UpdateVideo')


    def new_input_set(self):
        return UpdateVideoInputSet()

    def _make_result_set(self, result, path):
        return UpdateVideoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateVideoChoreographyExecution(session, exec_id, path)

class UpdateVideoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateVideo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_VideoMetadata(self, value):
        """
        Set the value of the VideoMetadata input for this Choreo. ((required, json) A JSON representation of the video resource containing fields to update. The id key for the video is required for updates. See documentation for examples.)
        """
        super(UpdateVideoInputSet, self)._set_input('VideoMetadata', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(UpdateVideoInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(UpdateVideoInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(UpdateVideoInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(UpdateVideoInputSet, self)._set_input('Fields', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields that are being set and that will be returned in the response (i.e. snippet,status).)
        """
        super(UpdateVideoInputSet, self)._set_input('Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(UpdateVideoInputSet, self)._set_input('RefreshToken', value)

class UpdateVideoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateVideo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class UpdateVideoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateVideoResultSet(response, path)
