# -*- coding: utf-8 -*-

###############################################################################
#
# GetLanguageNames
# Retrieves friendly names for languages and localized using the specified locale language.
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

class GetLanguageNames(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLanguageNames Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLanguageNames, self).__init__(temboo_session, '/Library/Microsoft/Translator/GetLanguageNames')


    def new_input_set(self):
        return GetLanguageNamesInputSet()

    def _make_result_set(self, result, path):
        return GetLanguageNamesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLanguageNamesChoreographyExecution(session, exec_id, path)

class GetLanguageNamesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLanguageNames
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('ClientSecret', value)
    def set_LanguageCodes(self, value):
        """
        Set the value of the LanguageCodes input for this Choreo. ((required, json) An array of ISO 639-1 language codes to retrieve friendly names for.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('LanguageCodes', value)
    def set_Locale(self, value):
        """
        Set the value of the Locale input for this Choreo. ((required, string) The ISO 639-1 language code associated with the language you wish to return results in.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('Locale', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLanguageNamesInputSet, self)._set_input('ResponseFormat', value)

class GetLanguageNamesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLanguageNames Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Microsoft.)
        """
        return self._output.get('Response', None)
    def get_ExpiresIn(self):
        """
        Retrieve the value for the "ExpiresIn" output from this Choreo execution. ((integer) Contains the number of seconds for which the access token is valid when ClientID and ClientSecret are provided.)
        """
        return self._output.get('ExpiresIn', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the ClientID and ClientSecret are provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetLanguageNamesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLanguageNamesResultSet(response, path)
