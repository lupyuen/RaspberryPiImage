# -*- coding: utf-8 -*-

###############################################################################
#
# Translate
# Translates a text string from one language to another.
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

class Translate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Translate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Translate, self).__init__(temboo_session, '/Library/Microsoft/Translator/Translate')


    def new_input_set(self):
        return TranslateInputSet()

    def _make_result_set(self, result, path):
        return TranslateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TranslateChoreographyExecution(session, exec_id, path)

class TranslateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Translate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(TranslateInputSet, self)._set_input('AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) A string containing the category (domain) of the translation. Defaults to "general".)
        """
        super(TranslateInputSet, self)._set_input('Category', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(TranslateInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(TranslateInputSet, self)._set_input('ClientSecret', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) The format of the text being translated. The supported formats are "text/plain" (the default) and "text/html".)
        """
        super(TranslateInputSet, self)._set_input('ContentType', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) A string representing the ISO 639-1 language code of the translation text (e.g., en).)
        """
        super(TranslateInputSet, self)._set_input('From', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) A string representing the text to translate. The size of the text must not exceed 10000 characters.)
        """
        super(TranslateInputSet, self)._set_input('Text', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) A string representing the ISO 639-1 language codee to translate the text into (e.g., es).)
        """
        super(TranslateInputSet, self)._set_input('To', value)

class TranslateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Translate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

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
    def get_TranslatedText(self):
        """
        Retrieve the value for the "TranslatedText" output from this Choreo execution. ((string) The translated text parsed from the Microsoft response.)
        """
        return self._output.get('TranslatedText', None)

class TranslateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TranslateResultSet(response, path)
