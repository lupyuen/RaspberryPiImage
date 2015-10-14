# -*- coding: utf-8 -*-

###############################################################################
#
# SendSMS
# Sends an SMS to a specified phone number using the Twilio API.
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

class SendSMS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendSMS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendSMS, self).__init__(temboo_session, '/Library/Twilio/SMSMessages/SendSMS')


    def new_input_set(self):
        return SendSMSInputSet()

    def _make_result_set(self, result, path):
        return SendSMSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendSMSChoreographyExecution(session, exec_id, path)

class SendSMSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendSMS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(SendSMSInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(SendSMSInputSet, self)._set_input('AuthToken', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((conditional, string) The text of the message.)
        """
        super(SendSMSInputSet, self)._set_input('Body', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The purchased Twilio phone number, Twilio Sandbox number, or short code enabled for the type of message you wish to send (SMS or MMS). Format with a '+' and country code e.g., +16175551212.)
        """
        super(SendSMSInputSet, self)._set_input('From', value)
    def set_MediaURL(self, value):
        """
        Set the value of the MediaURL input for this Choreo. ((optional, string) One or more URLs for media you wish to send with the message. Supported formats include: png, gif, and jpeg. Multiple URLs (up-to 10) should be separated by commas.)
        """
        super(SendSMSInputSet, self)._set_input('MediaURL', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(SendSMSInputSet, self)._set_input('ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to send the message from. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        super(SendSMSInputSet, self)._set_input('SubAccountSID', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The destination phone number. Format with a '+' and country code e.g., +16175551212.)
        """
        super(SendSMSInputSet, self)._set_input('To', value)

class SendSMSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendSMS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The Twilio response.)
        """
        return self._output.get('Response', None)

class SendSMSChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendSMSResultSet(response, path)
