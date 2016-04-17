# -*- coding: utf-8 -*-

###############################################################################
#
# GetFile
# Retrieves a file from the CloudMine server with a given key.
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
        super(GetFile, self).__init__(temboo_session, '/Library/CloudMine/FileStorage/GetFile')


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
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        super(GetFileInputSet, self)._set_input('APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        super(GetFileInputSet, self)._set_input('ApplicationIdentifier', value)
    def set_EncodeFileContent(self, value):
        """
        Set the value of the EncodeFileContent input for this Choreo. ((optional, boolean) Returns the file content as Base64 encoded data when set to "true". This should be set to "true" when returning binary files. Defaults to "false".)
        """
        super(GetFileInputSet, self)._set_input('EncodeFileContent', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The key whose value you want.)
        """
        super(GetFileInputSet, self)._set_input('Key', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        super(GetFileInputSet, self)._set_input('SessionToken', value)


class GetFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CloudMine.)
        """
        return self._output.get('Response', None)

class GetFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetFileResultSet(response, path)
