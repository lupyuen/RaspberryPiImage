# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadFile
# Retrieves the contents of a specified file.
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

class DownloadFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DownloadFile, self).__init__(temboo_session, '/Library/Box/Files/DownloadFile')


    def new_input_set(self):
        return DownloadFileInputSet()

    def _make_result_set(self, result, path):
        return DownloadFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadFileChoreographyExecution(session, exec_id, path)

class DownloadFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(DownloadFileInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(DownloadFileInputSet, self)._set_input('AsUser', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The id of the file to download.)
        """
        super(DownloadFileInputSet, self)._set_input('FileID', value)


class DownloadFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The Base64 encoded contents of the downloaded file.)
        """
        return self._output.get('Response', None)

class DownloadFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadFileResultSet(response, path)
