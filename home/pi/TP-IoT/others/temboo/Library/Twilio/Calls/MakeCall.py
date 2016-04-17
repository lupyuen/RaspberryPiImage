# -*- coding: utf-8 -*-

###############################################################################
#
# MakeCall
# Initiates a call from the specified Twilio account.
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

class MakeCall(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MakeCall Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MakeCall, self).__init__(temboo_session, '/Library/Twilio/Calls/MakeCall')


    def new_input_set(self):
        return MakeCallInputSet()

    def _make_result_set(self, result, path):
        return MakeCallResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MakeCallChoreographyExecution(session, exec_id, path)

class MakeCallInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MakeCall
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(MakeCallInputSet, self)._set_input('AccountSID', value)
    def set_ApplicationSID(self, value):
        """
        Set the value of the ApplicationSID input for this Choreo. ((conditional, string) The 34 character sid of the application Twilio should use to handle this phone call. Required unless providing the URL parameter.)
        """
        super(MakeCallInputSet, self)._set_input('ApplicationSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(MakeCallInputSet, self)._set_input('AuthToken', value)
    def set_FallbackMethod(self, value):
        """
        Set the value of the FallbackMethod input for this Choreo. ((optional, string) The HTTP method that Twilio should use to request the FallbackUrl. Valid values are: GET and POST.)
        """
        super(MakeCallInputSet, self)._set_input('FallbackMethod', value)
    def set_FallbackURL(self, value):
        """
        Set the value of the FallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs making a request to the URL provided. This is ignored when ApplicationSID is provided.)
        """
        super(MakeCallInputSet, self)._set_input('FallbackURL', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The Twilio phone number or client identifier to use as the caller id.)
        """
        super(MakeCallInputSet, self)._set_input('From', value)
    def set_IfMachine(self, value):
        """
        Set the value of the IfMachine input for this Choreo. ((optional, string) Indicates if Twilio should to try and determine if a machine (like voicemail) or a human has answered the call. Possible values are "Continue" and "Hangup".)
        """
        super(MakeCallInputSet, self)._set_input('IfMachine', value)
    def set_Method(self, value):
        """
        Set the value of the Method input for this Choreo. ((optional, string) This the HTTP method Twilio will use when making its request to the URL (when the URL input is provided). Defaults to POST. This is ignored when ApplicationSID is provided.)
        """
        super(MakeCallInputSet, self)._set_input('Method', value)
    def set_Record(self, value):
        """
        Set the value of the Record input for this Choreo. ((optional, boolean) Set this parameter to 'true' to record the entirety of a phone call.)
        """
        super(MakeCallInputSet, self)._set_input('Record', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(MakeCallInputSet, self)._set_input('ResponseFormat', value)
    def set_SendDigits(self, value):
        """
        Set the value of the SendDigits input for this Choreo. ((optional, string) A string of keys to dial after connecting to the number. Valid digits in the string include: any digit (0-9), '#', '*' and 'w' (to insert a half second pause).)
        """
        super(MakeCallInputSet, self)._set_input('SendDigits', value)
    def set_StatusCallbackMethod(self, value):
        """
        Set the value of the StatusCallbackMethod input for this Choreo. ((optional, string) The HTTP method Twilio should use when requesting the StatusCallback URL. Defaults to POST. If an ApplicationSid parameter is present, this parameter is ignored.)
        """
        super(MakeCallInputSet, self)._set_input('StatusCallbackMethod', value)
    def set_StatusCallback(self, value):
        """
        Set the value of the StatusCallback input for this Choreo. ((optional, string) A URL that Twilio will request when the call ends to notify your app. This is ignored when ApplicationSID is provided.)
        """
        super(MakeCallInputSet, self)._set_input('StatusCallback', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with this call. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        super(MakeCallInputSet, self)._set_input('SubAccountSID', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, integer) The integer number of seconds that Twilio should allow the phone to ring before assuming there is no answer. Default is 60 seconds, the maximum is 999 seconds.)
        """
        super(MakeCallInputSet, self)._set_input('Timeout', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The phone number or client identifier to call.)
        """
        super(MakeCallInputSet, self)._set_input('To', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) The fully qualified URL that should be consulted when the call connects. Required unless providing the ApplicationSID parameter.)
        """
        super(MakeCallInputSet, self)._set_input('URL', value)

class MakeCallResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MakeCall Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class MakeCallChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MakeCallResultSet(response, path)
