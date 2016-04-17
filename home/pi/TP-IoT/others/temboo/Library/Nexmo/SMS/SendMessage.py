# -*- coding: utf-8 -*-

###############################################################################
#
# SendMessage
# Send a text message to any global number.
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

class SendMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendMessage, self).__init__(temboo_session, '/Library/Nexmo/SMS/SendMessage')


    def new_input_set(self):
        return SendMessageInputSet()

    def _make_result_set(self, result, path):
        return SendMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMessageChoreographyExecution(session, exec_id, path)

class SendMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(SendMessageInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(SendMessageInputSet, self)._set_input('APISecret', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((optional, string) Hex encoded binary data. (e.g. 0011223344556677).  Required when Type is binary.)
        """
        super(SendMessageInputSet, self)._set_input('Body', value)
    def set_CallbackID(self, value):
        """
        Set the value of the CallbackID input for this Choreo. ((conditional, string) A unique identifier that is part of your Temboo callback URL registered at Nexmo. Required in order to listen for a reply. See Choreo description for details.)
        """
        super(SendMessageInputSet, self)._set_input('CallbackID', value)
    def set_ClientReference(self, value):
        """
        Set the value of the ClientReference input for this Choreo. ((optional, string) Include a note for your reference. (40 characters max).)
        """
        super(SendMessageInputSet, self)._set_input('ClientReference', value)
    def set_DeliveryReceipt(self, value):
        """
        Set the value of the DeliveryReceipt input for this Choreo. ((optional, integer) Set to 1 to receive a Delivery Receipt for this message. Make sure to configure your "Callback URL" in your "API Settings".)
        """
        super(SendMessageInputSet, self)._set_input('DeliveryReceipt', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The phone number associated with your Nexmo account e.g. 17185551234.)
        """
        super(SendMessageInputSet, self)._set_input('From', value)
    def set_MessageClass(self, value):
        """
        Set the value of the MessageClass input for this Choreo. ((optional, integer) Set to 0 for Flash SMS.)
        """
        super(SendMessageInputSet, self)._set_input('MessageClass', value)
    def set_NetworkCode(self, value):
        """
        Set the value of the NetworkCode input for this Choreo. ((optional, string) Sends this message to the specifed network operator (MCCMNC).)
        """
        super(SendMessageInputSet, self)._set_input('NetworkCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(SendMessageInputSet, self)._set_input('ResponseFormat', value)
    def set_TTL(self, value):
        """
        Set the value of the TTL input for this Choreo. ((optional, integer) Message life span (Time to  live) in milliseconds.)
        """
        super(SendMessageInputSet, self)._set_input('TTL', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) Required when Type is "text".  Body of the text message (with a maximum length of 3200 characters).)
        """
        super(SendMessageInputSet, self)._set_input('Text', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((conditional, integer) The amount of time (in minutes) to wait for a reply when a CallbackID is provided. Defaults to 10. See Choreo description for details.)
        """
        super(SendMessageInputSet, self)._set_input('Timeout', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The mobile number in international format (e.g. 447525856424 or 00447525856424 when sending to UK).)
        """
        super(SendMessageInputSet, self)._set_input('To', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) This can be omitted for text (default), but is required when sending a Binary (binary), WAP Push (wappush), Unicode message (unicode), VCal (vcal) or VCard (vcard).)
        """
        super(SendMessageInputSet, self)._set_input('Type', value)
    def set_UDH(self, value):
        """
        Set the value of the UDH input for this Choreo. ((optional, string) Hex encoded User data header. (e.g. 06050415811581) (Required when Type is binary).)
        """
        super(SendMessageInputSet, self)._set_input('UDH', value)
    def set_VCal(self, value):
        """
        Set the value of the VCal input for this Choreo. ((optional, string) Correctly formatted VCal text body.)
        """
        super(SendMessageInputSet, self)._set_input('VCal', value)
    def set_VCard(self, value):
        """
        Set the value of the VCard input for this Choreo. ((optional, string) Correctly formatted VCard text body.)
        """
        super(SendMessageInputSet, self)._set_input('VCard', value)

class SendMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMessage Choreo.
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
        Retrieve the value for the "CallbackData" output from this Choreo execution. (The Nexmo callback data retrieved after a user has replied to the SMS message. This is only returned if you've setup your Temboo callback URL at Nexmo, and  have provided the CallbackID input.)
        """
        return self._output.get('CallbackData', None)

class SendMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendMessageResultSet(response, path)
