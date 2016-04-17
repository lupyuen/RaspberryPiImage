# -*- coding: utf-8 -*-

###############################################################################
#
# UploadFile
# Uploads a new file to a user's account. This can also be used when updating the contents of an existing file.
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

class UploadFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UploadFile, self).__init__(temboo_session, '/Library/Box/Files/UploadFile')


    def new_input_set(self):
        return UploadFileInputSet()

    def _make_result_set(self, result, path):
        return UploadFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadFileChoreographyExecution(session, exec_id, path)

class UploadFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((conditional, string) The Base64 encoded contents of the file you want to upload.)
        """
        super(UploadFileInputSet, self)._set_input('FileContents', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(UploadFileInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(UploadFileInputSet, self)._set_input('AsUser', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((optional, string) When providing the id of an existing file, the content of the file will be updated.)
        """
        super(UploadFileInputSet, self)._set_input('FileID', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((conditional, string) The name of the new file to upload. Note that when providing the FileID in order to perform an update to a file, it is not necessary to provide the FileName.)
        """
        super(UploadFileInputSet, self)._set_input('FileName', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((optional, string) The ID of the target folder to upload the file to. Defaults to 0 indicating the root folder.)
        """
        super(UploadFileInputSet, self)._set_input('FolderID', value)


class UploadFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UploadFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadFileResultSet(response, path)
