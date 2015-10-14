# -*- coding: utf-8 -*-

###############################################################################
#
# CopyFolder
# Creates a copy of a folder in another folder.
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

class CopyFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CopyFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CopyFolder, self).__init__(temboo_session, '/Library/Box/Folders/CopyFolder')


    def new_input_set(self):
        return CopyFolderInputSet()

    def _make_result_set(self, result, path):
        return CopyFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyFolderChoreographyExecution(session, exec_id, path)

class CopyFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CopyFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(CopyFolderInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(CopyFolderInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(CopyFolderInputSet, self)._set_input('Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder to copy.)
        """
        super(CopyFolderInputSet, self)._set_input('FolderID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) An optional new name for the folder.)
        """
        super(CopyFolderInputSet, self)._set_input('Name', value)
    def set_ParentID(self, value):
        """
        Set the value of the ParentID input for this Choreo. ((required, string) The ID of the destination folder to copy the folder to.)
        """
        super(CopyFolderInputSet, self)._set_input('ParentID', value)

class CopyFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CopyFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class CopyFolderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CopyFolderResultSet(response, path)
