# -*- coding: utf-8 -*-

###############################################################################
#
# AddTranslation
# Retrieves an array of all translations for a given text.
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

class AddTranslation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddTranslation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddTranslation, self).__init__(temboo_session, '/Library/Microsoft/Translator/AddTranslation')


    def new_input_set(self):
        return AddTranslationInputSet()

    def _make_result_set(self, result, path):
        return AddTranslationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTranslationChoreographyExecution(session, exec_id, path)

class AddTranslationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddTranslation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(AddTranslationInputSet, self)._set_input('AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) A string containing the category (domain) of the translation. Defaults to "general".)
        """
        super(AddTranslationInputSet, self)._set_input('Category', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(AddTranslationInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(AddTranslationInputSet, self)._set_input('ClientSecret', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) The format of the text being translated. The supported formats are "text/plain" and "text/html".)
        """
        super(AddTranslationInputSet, self)._set_input('ContentType', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) A string containing the ISO 639-1 language code of the source language. Must be one of the languages returned by the method GetLanguagesForTranslate.(e.g., en).)
        """
        super(AddTranslationInputSet, self)._set_input('From', value)
    def set_OriginalText(self, value):
        """
        Set the value of the OriginalText input for this Choreo. ((required, string) A string containing the text to translate from. The string has a maximum length of 1000 characters.)
        """
        super(AddTranslationInputSet, self)._set_input('OriginalText', value)
    def set_Rating(self, value):
        """
        Set the value of the Rating input for this Choreo. ((optional, integer) An integer representing the quality rating for this string. Value between -10 and 10. Defaults to 1.)
        """
        super(AddTranslationInputSet, self)._set_input('Rating', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(AddTranslationInputSet, self)._set_input('ResponseFormat', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) A string containing the lISO 639-1 language code of the target language. Must be one of the languages returned by the method GetLanguagesForTranslate (e.g., es).)
        """
        super(AddTranslationInputSet, self)._set_input('To', value)
    def set_TranslatedText(self, value):
        """
        Set the value of the TranslatedText input for this Choreo. ((required, string) A string containing translated text in the target language. The string has a maximum length of 2000 characters.)
        """
        super(AddTranslationInputSet, self)._set_input('TranslatedText', value)
    def set_URI(self, value):
        """
        Set the value of the URI input for this Choreo. ((optional, string) A string containing the content location of this translation.)
        """
        super(AddTranslationInputSet, self)._set_input('URI', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) A string used to track the originator of the submission.)
        """
        super(AddTranslationInputSet, self)._set_input('User', value)

class AddTranslationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddTranslation Choreo.
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

class AddTranslationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddTranslationResultSet(response, path)
