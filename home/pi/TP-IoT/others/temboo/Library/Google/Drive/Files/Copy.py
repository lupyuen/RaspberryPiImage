# -*- coding: utf-8 -*-

###############################################################################
#
# Copy
# Creates a copy of the specified file.
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

class Copy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Copy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Copy, self).__init__(temboo_session, '/Library/Google/Drive/Files/Copy')


    def new_input_set(self):
        return CopyInputSet()

    def _make_result_set(self, result, path):
        return CopyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyChoreographyExecution(session, exec_id, path)

class CopyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Copy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestBody(self, value):
        """
        Set the value of the RequestBody input for this Choreo. ((optional, json) A JSON representation of fields in a file resource. File metadata information (such as the title) can be set using this input. See documentation for formatting examples.)
        """
        super(CopyInputSet, self)._set_input('RequestBody', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(CopyInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CopyInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CopyInputSet, self)._set_input('ClientSecret', value)
    def set_Convert(self, value):
        """
        Set the value of the Convert input for this Choreo. ((optional, boolean) Whether to convert this file to the corresponding Google Docs format. (Default: false).)
        """
        super(CopyInputSet, self)._set_input('Convert', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        super(CopyInputSet, self)._set_input('Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The ID of the file to copy.)
        """
        super(CopyInputSet, self)._set_input('FileID', value)
    def set_OCR(self, value):
        """
        Set the value of the OCR input for this Choreo. ((optional, boolean) Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. (Default: false))
        """
        super(CopyInputSet, self)._set_input('OCR', value)
    def set_OcrLanguage(self, value):
        """
        Set the value of the OcrLanguage input for this Choreo. ((optional, string) If ocr is true, hints at the language to use. Valid values are ISO 639-1 codes.)
        """
        super(CopyInputSet, self)._set_input('OcrLanguage', value)
    def set_Pinned(self, value):
        """
        Set the value of the Pinned input for this Choreo. ((optional, boolean) Whether to pin the head revision of the uploaded file. (Default: false).)
        """
        super(CopyInputSet, self)._set_input('Pinned', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(CopyInputSet, self)._set_input('RefreshToken', value)
    def set_SourceLanguage(self, value):
        """
        Set the value of the SourceLanguage input for this Choreo. ((optional, string) The language of the original file to be translated.)
        """
        super(CopyInputSet, self)._set_input('SourceLanguage', value)
    def set_TargetLanguage(self, value):
        """
        Set the value of the TargetLanguage input for this Choreo. ((optional, string) Target language to translate the file to. If no sourceLanguage is provided, the API will attempt to detect the language.)
        """
        super(CopyInputSet, self)._set_input('TargetLanguage', value)
    def set_TimedTextLanguage(self, value):
        """
        Set the value of the TimedTextLanguage input for this Choreo. ((optional, string) The language of the timed text.)
        """
        super(CopyInputSet, self)._set_input('TimedTextLanguage', value)
    def set_TimedTextTrackName(self, value):
        """
        Set the value of the TimedTextTrackName input for this Choreo. ((optional, string) The timed text track name.)
        """
        super(CopyInputSet, self)._set_input('TimedTextTrackName', value)

class CopyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Copy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class CopyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CopyResultSet(response, path)
