# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFolder
# Deletes a specified folder.
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

class DeleteFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteFolder, self).__init__(temboo_session, '/Library/Box/Folders/DeleteFolder')


    def new_input_set(self):
        return DeleteFolderInputSet()

    def _make_result_set(self, result, path):
        return DeleteFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFolderChoreographyExecution(session, exec_id, path)

class DeleteFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(DeleteFolderInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(DeleteFolderInputSet, self)._set_input('AsUser', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder that you want to delete.)
        """
        super(DeleteFolderInputSet, self)._set_input('FolderID', value)
    def set_Recursive(self, value):
        """
        Set the value of the Recursive input for this Choreo. ((optional, boolean) Whether or not to delete this folder if it has items within in. Defaults to true.)
        """
        super(DeleteFolderInputSet, self)._set_input('Recursive', value)


class DeleteFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class DeleteFolderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteFolderResultSet(response, path)
