# -*- coding: utf-8 -*-

###############################################################################
#
# GetFile
# Gets the content and metadata for a specified file.
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

class GetFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetFile, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/GetFile')


    def new_input_set(self):
        return GetFileInputSet()

    def _make_result_set(self, result, path):
        return GetFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFileChoreographyExecution(session, exec_id, path)

class GetFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetFileInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetFileInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(GetFileInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(GetFileInputSet, self)._set_input('AppSecret', value)
    def set_EncodeFileContent(self, value):
        """
        Set the value of the EncodeFileContent input for this Choreo. ((optional, boolean) File content is returned as Base64 encoded data by default. Text files can be returned as Base64 decoded by setting this input to "false". Note that binary files should always be Base64 encoded.)
        """
        super(GetFileInputSet, self)._set_input('EncodeFileContent', value)
    def set_IncludeMetadata(self, value):
        """
        Set the value of the IncludeMetadata input for this Choreo. ((optional, boolean) If set to true, metadata about the file is returned. Defaults to false, indicating that only the file content is returned.)
        """
        super(GetFileInputSet, self)._set_input('IncludeMetadata', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to file you want to retrieve (i.e. RootFolder/SubFolder/MyFile.txt). Only the file name is necessary when the file is at the root level.)
        """
        super(GetFileInputSet, self)._set_input('Path', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((optional, string) Defaults to "auto" which automatically determines the root folder using your app's permission level. Other options are "sandbox" (App Folder) and "dropbox" (Full Dropbox).)
        """
        super(GetFileInputSet, self)._set_input('Root', value)

class GetFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_FileMetadata(self):
        """
        Retrieve the value for the "FileMetadata" output from this Choreo execution. ((json) The metadata for the file. This only returned when IncludeMetadata is set to true.)
        """
        return self._output.get('FileMetadata', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from Dropbox. The response will contain the contents of the file you are retrieving as Base64 encoded data.)
        """
        return self._output.get('Response', None)

class GetFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetFileResultSet(response, path)
