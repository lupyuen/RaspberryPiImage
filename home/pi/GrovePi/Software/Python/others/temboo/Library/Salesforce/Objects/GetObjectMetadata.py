# -*- coding: utf-8 -*-

###############################################################################
#
# GetObjectMetadata
# Retrieves the individual metadata for the specified object type such as a Contact, Lead, or Account object.
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

class GetObjectMetadata(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetObjectMetadata Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetObjectMetadata, self).__init__(temboo_session, '/Library/Salesforce/Objects/GetObjectMetadata')


    def new_input_set(self):
        return GetObjectMetadataInputSet()

    def _make_result_set(self, result, path):
        return GetObjectMetadataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetObjectMetadataChoreographyExecution(session, exec_id, path)

class GetObjectMetadataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetObjectMetadata
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(GetObjectMetadataInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        super(GetObjectMetadataInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Salesforce. Required unless providing a valid AccessToken.)
        """
        super(GetObjectMetadataInputSet, self)._set_input('ClientSecret', value)
    def set_InstanceName(self, value):
        """
        Set the value of the InstanceName input for this Choreo. ((required, string) The server url prefix that indicates which instance your Salesforce account is on (e.g. na1, na2, na3, etc).)
        """
        super(GetObjectMetadataInputSet, self)._set_input('InstanceName', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetObjectMetadataInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetObjectMetadataInputSet, self)._set_input('ResponseFormat', value)
    def set_SObjectName(self, value):
        """
        Set the value of the SObjectName input for this Choreo. ((required, string) The name of the SObject to retrieve (e.g. Contact, Lead, Account, etc).)
        """
        super(GetObjectMetadataInputSet, self)._set_input('SObjectName', value)

class GetObjectMetadataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetObjectMetadata Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Salesforce.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetObjectMetadataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetObjectMetadataResultSet(response, path)
