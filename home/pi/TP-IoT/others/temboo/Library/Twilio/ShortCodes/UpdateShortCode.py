# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateShortCode
# Attempts to update an existing short code resource.
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

class UpdateShortCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateShortCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateShortCode, self).__init__(temboo_session, '/Library/Twilio/ShortCodes/UpdateShortCode')


    def new_input_set(self):
        return UpdateShortCodeInputSet()

    def _make_result_set(self, result, path):
        return UpdateShortCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateShortCodeChoreographyExecution(session, exec_id, path)

class UpdateShortCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateShortCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIVersion(self, value):
        """
        Set the value of the APIVersion input for this Choreo. ((optional, string) SMSs to this short code will start a new TwiML session with this API version. Either 2010-04-01 or 2008-08-01.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('APIVersion', value)
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) A human readable description of the short code, with maximum length 64 characters.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('FriendlyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('ResponseFormat', value)
    def set_ShortCodeSID(self, value):
        """
        Set the value of the ShortCodeSID input for this Choreo. ((required, string) The id of the short code to update.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('ShortCodeSID', value)
    def set_SmsFallbackMethod(self, value):
        """
        Set the value of the SmsFallbackMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsFallbackUrl. Either GET or POST.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('SmsFallbackMethod', value)
    def set_SmsFallbackURL(self, value):
        """
        Set the value of the SmsFallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs requesting or executing the TwiML at the SmsUrl.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('SmsFallbackURL', value)
    def set_SmsMethod(self, value):
        """
        Set the value of the SmsMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsUrl. Either GET or POST.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('SmsMethod', value)
    def set_SmsURL(self, value):
        """
        Set the value of the SmsURL input for this Choreo. ((optional, string) The URL that Twilio should request when somebody sends an SMS to the short code.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('SmsURL', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with short code. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        super(UpdateShortCodeInputSet, self)._set_input('SubAccountSID', value)

class UpdateShortCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateShortCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class UpdateShortCodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateShortCodeResultSet(response, path)
