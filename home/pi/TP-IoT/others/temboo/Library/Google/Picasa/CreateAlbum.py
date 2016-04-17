# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAlbum
# Creates a photo album in a Google Picasa account.
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

class CreateAlbum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAlbum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateAlbum, self).__init__(temboo_session, '/Library/Google/Picasa/CreateAlbum')


    def new_input_set(self):
        return CreateAlbumInputSet()

    def _make_result_set(self, result, path):
        return CreateAlbumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAlbumChoreographyExecution(session, exec_id, path)

class CreateAlbumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAlbum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(CreateAlbumInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateAlbumInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateAlbumInputSet, self)._set_input('ClientSecret', value)
    def set_Keywords(self, value):
        """
        Set the value of the Keywords input for this Choreo. ((optional, string) Keywords to associate with the album you are creating separated by commas.)
        """
        super(CreateAlbumInputSet, self)._set_input('Keywords', value)
    def set_PhotoAccess(self, value):
        """
        Set the value of the PhotoAccess input for this Choreo. ((optional, string) The perssion level to specify for photo access. Defaults to 'public'.)
        """
        super(CreateAlbumInputSet, self)._set_input('PhotoAccess', value)
    def set_PhotoLocation(self, value):
        """
        Set the value of the PhotoLocation input for this Choreo. ((optional, string) The location to associate with the photo (i.e. Italy).)
        """
        super(CreateAlbumInputSet, self)._set_input('PhotoLocation', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(CreateAlbumInputSet, self)._set_input('RefreshToken', value)
    def set_Summary(self, value):
        """
        Set the value of the Summary input for this Choreo. ((optional, string) The album summary.)
        """
        super(CreateAlbumInputSet, self)._set_input('Summary', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) The timestamp to associate with the photo.  Defaults to the current timestamp. Should be an epoch timestamp in milliseconds.)
        """
        super(CreateAlbumInputSet, self)._set_input('Timestamp', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the album.)
        """
        super(CreateAlbumInputSet, self)._set_input('Title', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        super(CreateAlbumInputSet, self)._set_input('UserID', value)

class CreateAlbumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAlbum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google Picasa.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class CreateAlbumChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateAlbumResultSet(response, path)
