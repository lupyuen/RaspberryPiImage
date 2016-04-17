# -*- coding: utf-8 -*-

###############################################################################
#
# Speak
# Returns a Base64 encoded wave or mp3 file of the passed-in text being spoken in the desired language.
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

class Speak(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Speak Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Speak, self).__init__(temboo_session, '/Library/Microsoft/Translator/Speak')


    def new_input_set(self):
        return SpeakInputSet()

    def _make_result_set(self, result, path):
        return SpeakResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SpeakChoreographyExecution(session, exec_id, path)

class SpeakInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Speak
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(SpeakInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(SpeakInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(SpeakInputSet, self)._set_input('ClientSecret', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) A string specifying the content-type. Currently, "audio/wav" and "audio/mp3" are available. The default value is "audio/wav".)
        """
        super(SpeakInputSet, self)._set_input('Format', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((required, string) A string representing the supported ISO 639-1 language code to speak the text in (e.g., es). The code must be present in the list of codes returned from the method GetLanguagesForSpeak.)
        """
        super(SpeakInputSet, self)._set_input('Language', value)
    def set_Options(self, value):
        """
        Set the value of the Options input for this Choreo. ((optional, string) A string specifying the quality of the audio signals. Valid values are: MaxQuality or MinQuality (the default).)
        """
        super(SpeakInputSet, self)._set_input('Options', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) A string representing the text to translate. The size of the text must not exceed 10000 characters.)
        """
        super(SpeakInputSet, self)._set_input('Text', value)

class SpeakResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Speak Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AudioFile(self):
        """
        Retrieve the value for the "AudioFile" output from this Choreo execution. ((string) The Base64 encoded audio file in mp3 or wav format.)
        """
        return self._output.get('AudioFile', None)
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

class SpeakChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SpeakResultSet(response, path)
