# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFolder
# Creates a new folder.
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

class CreateFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateFolder, self).__init__(temboo_session, '/Library/Amazon/CloudDrive/Folders/CreateFolder')


    def new_input_set(self):
        return CreateFolderInputSet()

    def _make_result_set(self, result, path):
        return CreateFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFolderChoreographyExecution(session, exec_id, path)

class CreateFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(CreateFolderInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Amazon. Required unless providing a valid AccessToken.)
        """
        super(CreateFolderInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Amazon. Required unless providing a valid AccessToken.)
        """
        super(CreateFolderInputSet, self)._set_input('ClientSecret', value)
    def set_HandleRequestThrottling(self, value):
        """
        Set the value of the HandleRequestThrottling input for this Choreo. ((optional, boolean) Whether or not to perform a retry sequence if a throttling error occurs. Set to true to enable this feature. The request will be retried up-to five times when enabled.)
        """
        super(CreateFolderInputSet, self)._set_input('HandleRequestThrottling', value)
    def set_Labels(self, value):
        """
        Set the value of the Labels input for this Choreo. ((optional, json) A JSON array containing labels to apply to the folder.)
        """
        super(CreateFolderInputSet, self)._set_input('Labels', value)
    def set_LocalID(self, value):
        """
        Set the value of the LocalID input for this Choreo. ((optional, string) Globally unique client local Id for the customer.)
        """
        super(CreateFolderInputSet, self)._set_input('LocalID', value)
    def set_MetaDataURL(self, value):
        """
        Set the value of the MetaDataURL input for this Choreo. ((optional, string) The appropriate metadataUrl for your account. When not provided, the Choreo will lookup the URL using the Account.GetEndpoint Choreo.)
        """
        super(CreateFolderInputSet, self)._set_input('MetaDataURL', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the new folder.)
        """
        super(CreateFolderInputSet, self)._set_input('Name', value)
    def set_Parents(self, value):
        """
        Set the value of the Parents input for this Choreo. ((optional, json) A JSON array containing parent names associated with the new folder.)
        """
        super(CreateFolderInputSet, self)._set_input('Parents', value)
    def set_Properties(self, value):
        """
        Set the value of the Properties input for this Choreo. ((optional, json) A JSON object containing properties to be applied to the folder.)
        """
        super(CreateFolderInputSet, self)._set_input('Properties', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(CreateFolderInputSet, self)._set_input('RefreshToken', value)

class CreateFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class CreateFolderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateFolderResultSet(response, path)
