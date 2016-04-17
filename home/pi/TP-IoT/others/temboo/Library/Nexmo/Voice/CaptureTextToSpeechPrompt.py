# -*- coding: utf-8 -*-

###############################################################################
#
# CaptureTextToSpeechPrompt
# Sends a Text-to-Speech message to the specifed Number and captures keypad entries from the receiver.
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

class CaptureTextToSpeechPrompt(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CaptureTextToSpeechPrompt Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CaptureTextToSpeechPrompt, self).__init__(temboo_session, '/Library/Nexmo/Voice/CaptureTextToSpeechPrompt')


    def new_input_set(self):
        return CaptureTextToSpeechPromptInputSet()

    def _make_result_set(self, result, path):
        return CaptureTextToSpeechPromptResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CaptureTextToSpeechPromptChoreographyExecution(session, exec_id, path)

class CaptureTextToSpeechPromptInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CaptureTextToSpeechPrompt
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('APISecret', value)
    def set_ByeText(self, value):
        """
        Set the value of the ByeText input for this Choreo. ((required, string) Body of the text message played after digits are entered.  (with a maximum length of 500 characters).)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('ByeText', value)
    def set_CallbackMethod(self, value):
        """
        Set the value of the CallbackMethod input for this Choreo. ((optional, string) The HTTP method for your callback. Valid values are: GET (default) or POST.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('CallbackMethod', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((optional, string) A CallbackURL that Nexmo will request when the call ends to notify your application.  If left empty, the Choreo will handle the callback for you and return the results in CallbackData.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('CallbackURL', value)
    def set_DropIfMachine(self, value):
        """
        Set the value of the DropIfMachine input for this Choreo. ((optional, integer) Deprecated (retained for backward compatibility only).)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('DropIfMachine', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((optional, string) A voice enabled inbound number associated with your Nexmo account.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('From', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language used to play back your message.  The default is "en-us" which corresponds to United States english.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('Language', value)
    def set_MachineDetection(self, value):
        """
        Set the value of the MachineDetection input for this Choreo. ((optional, string) If set to "hangup", the call will hang up immediately if a machine is detected, and the status in the CallbackData output will be set to "machine".)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('MachineDetection', value)
    def set_MachineTimeout(self, value):
        """
        Set the value of the MachineTimeout input for this Choreo. ((optional, integer) Time allocated to analyze if the call has been answered by a machine. The default value is 15000 (milliseconds).)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('MachineTimeout', value)
    def set_MaxDigits(self, value):
        """
        Set the value of the MaxDigits input for this Choreo. ((conditional, integer) Number of digits entered by the end user. Valid values are 1-9. Defaults to 1.)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('MaxDigits', value)
    def set_Repeat(self, value):
        """
        Set the value of the Repeat input for this Choreo. ((optional, integer) Define how many times you want to repeat the text message (default is 1 , maximum is 10).)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('Repeat', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Body of the text message. (with a maximum length of 1000 characters).)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('Text', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) Phone number in international format and one recipient per request. (e.g. 447525856424 when sending to UK))
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('To', value)
    def set_Voice(self, value):
        """
        Set the value of the Voice input for this Choreo. ((optional, string) The voice to be used female (default) or male)
        """
        super(CaptureTextToSpeechPromptInputSet, self)._set_input('Voice', value)

class CaptureTextToSpeechPromptResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CaptureTextToSpeechPrompt Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)
    def get_CallbackData(self):
        """
        Retrieve the value for the "CallbackData" output from this Choreo execution. (The Nexmo callback data retrieved after a user has entered a pin code. Note that this will only be returned when the CallbackURL input  is not provided.)
        """
        return self._output.get('CallbackData', None)
    def get_Digits(self):
        """
        Retrieve the value for the "Digits" output from this Choreo execution. ((integer) The digits that the call recipient entered into the keypad after receiving the call from Nexmo.)
        """
        return self._output.get('Digits', None)

class CaptureTextToSpeechPromptChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CaptureTextToSpeechPromptResultSet(response, path)
