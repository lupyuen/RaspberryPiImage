# -*- coding: utf-8 -*-

###############################################################################
#
# ChunkedUpload
# Uploads larger files to Dropbox in multiple chunks, and offers a way to resume if an upload gets interrupted.
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

class ChunkedUpload(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChunkedUpload Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ChunkedUpload, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/ChunkedUpload')


    def new_input_set(self):
        return ChunkedUploadInputSet()

    def _make_result_set(self, result, path):
        return ChunkedUploadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChunkedUploadChoreographyExecution(session, exec_id, path)

class ChunkedUploadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChunkedUpload
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ChunkedUploadInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ChunkedUploadInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(ChunkedUploadInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(ChunkedUploadInputSet, self)._set_input('AppSecret', value)
    def set_Chunk(self, value):
        """
        Set the value of the Chunk input for this Choreo. ((conditional, string) A Base64 encoded chunk of data from the file being uploaded. If resuming and upload, the chunk should begin at the number of bytes into the file that equals the NextOffset.)
        """
        super(ChunkedUploadInputSet, self)._set_input('Chunk', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((conditional, string) The byte offset of this chunk, relative to the beginning of the full file. This is not required when uploading the first chunk of a file.)
        """
        super(ChunkedUploadInputSet, self)._set_input('Offset', value)
    def set_UploadID(self, value):
        """
        Set the value of the UploadID input for this Choreo. ((conditional, string) The ID of the upload session returned after uploading the initial file chunk. This is not required when uploading the first chunk of a file. This value is returned in the UploadSessionID output.)
        """
        super(ChunkedUploadInputSet, self)._set_input('UploadID', value)


class ChunkedUploadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChunkedUpload Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Expires(self):
        """
        Retrieve the value for the "Expires" output from this Choreo execution. ((string) The expiration time of the upload.)
        """
        return self._output.get('Expires', None)
    def get_NextOffset(self):
        """
        Retrieve the value for the "NextOffset" output from this Choreo execution. ((string) The current byte offset that the server will expect. This value can be passed to the Offset input on subsequent requests when uploading chunks repeatedly.)
        """
        return self._output.get('NextOffset', None)
    def get_UploadSessionID(self):
        """
        Retrieve the value for the "UploadSessionID" output from this Choreo execution. ((string) The upload ID returned after uploading an initial file chunk. This can be passed to the UploadID input for uploading subsequent chunks, and finally to the CommitChunkedUpload Choreo.)
        """
        return self._output.get('UploadSessionID', None)

class ChunkedUploadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ChunkedUploadResultSet(response, path)
