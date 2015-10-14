# -*- coding: utf-8 -*-

###############################################################################
#
# UploadFile
# Uploads a file to your Dropbox account.
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
        super(UploadFile, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/UploadFile')


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
        Set the value of the FileContents input for this Choreo. ((conditional, string) The Base64-encoded contents of the file you want to upload. Required UNLESS uploading a file from a URL using the FileContentsFromURL input variable.)
        """
        super(UploadFileInputSet, self)._set_input('FileContents', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(UploadFileInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(UploadFileInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(UploadFileInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(UploadFileInputSet, self)._set_input('AppSecret', value)
    def set_FileContentsFromURL(self, value):
        """
        Set the value of the FileContentsFromURL input for this Choreo. ((conditional, string) URL for file you want to upload. Alternative to uploading Base64Encoded data. If specifiying URL, leave FileContents blank. Valid URLs: http(s) requests only.)
        """
        super(UploadFileInputSet, self)._set_input('FileContentsFromURL', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file you are uploading to Dropbox.)
        """
        super(UploadFileInputSet, self)._set_input('FileName', value)
    def set_Folder(self, value):
        """
        Set the value of the Folder input for this Choreo. ((optional, string) The name of the folder that that you want to upload a file to. A path to a sub-folder is also valid (i.e. /RootFolder/SubFolder).)
        """
        super(UploadFileInputSet, self)._set_input('Folder', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UploadFileInputSet, self)._set_input('ResponseFormat', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((optional, string) Defaults to "auto" which automatically determines the root folder using your app's permission level. Other options are "sandbox" (App Folder) and "dropbox" (Full Dropbox).)
        """
        super(UploadFileInputSet, self)._set_input('Root', value)


class UploadFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class UploadFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadFileResultSet(response, path)
