# -*- coding: utf-8 -*-

###############################################################################
#
# Delete
# Removes a revision.
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

class Delete(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Delete Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Delete, self).__init__(temboo_session, '/Library/Google/Drive/Revisions/Delete')


    def new_input_set(self):
        return DeleteInputSet()

    def _make_result_set(self, result, path):
        return DeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteChoreographyExecution(session, exec_id, path)

class DeleteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Delete
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(DeleteInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteInputSet, self)._set_input('ClientSecret', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The ID of the file.)
        """
        super(DeleteInputSet, self)._set_input('FileID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(DeleteInputSet, self)._set_input('RefreshToken', value)
    def set_RevisionID(self, value):
        """
        Set the value of the RevisionID input for this Choreo. ((required, string) The ID of the revision.)
        """
        super(DeleteInputSet, self)._set_input('RevisionID', value)

class DeleteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Delete Choreo.
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

class DeleteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteResultSet(response, path)
