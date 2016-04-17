# -*- coding: utf-8 -*-

###############################################################################
#
# InitializeOAuth
# Generates an authorization URL and callback ID that an application can use to complete the first step in the OAuth process.
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

class InitializeOAuth(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InitializeOAuth Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InitializeOAuth, self).__init__(temboo_session, '/Library/Dwolla/OAuth/InitializeOAuth')


    def new_input_set(self):
        return InitializeOAuthInputSet()

    def _make_result_set(self, result, path):
        return InitializeOAuthResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InitializeOAuthChoreographyExecution(session, exec_id, path)

class InitializeOAuthInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InitializeOAuth
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(InitializeOAuthInputSet, self)._set_input('AccountName', value)
    def set_AppKeyName(self, value):
        """
        Set the value of the AppKeyName input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(InitializeOAuthInputSet, self)._set_input('AppKeyName', value)
    def set_AppKeyValue(self, value):
        """
        Set the value of the AppKeyValue input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(InitializeOAuthInputSet, self)._set_input('AppKeyValue', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Dwolla after registering your application.)
        """
        super(InitializeOAuthInputSet, self)._set_input('ClientID', value)
    def set_CustomCallbackID(self, value):
        """
        Set the value of the CustomCallbackID input for this Choreo. ((optional, string) A unique identifier that you can pass to eliminate the need to wait for a Temboo generated CallbackID. Callback identifiers may only contain numbers, letters, periods, and hyphens.)
        """
        super(InitializeOAuthInputSet, self)._set_input('CustomCallbackID', value)
    def set_ForwardingURL(self, value):
        """
        Set the value of the ForwardingURL input for this Choreo. ((optional, string) The URL that Temboo will redirect your users to after they grant access to your application. This should include the "https://" or "http://" prefix and be a fully qualified URL.)
        """
        super(InitializeOAuthInputSet, self)._set_input('ForwardingURL', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((required, string) Lists which access permissions the app requires. Multiple scopes - separated by '|' (ex of all: "AccountInfoFull|Contacts|Transactions|Balance|Send|Request|Funding" ). For more info see docs.)
        """
        super(InitializeOAuthInputSet, self)._set_input('Scope', value)

class InitializeOAuthResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InitializeOAuth Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AuthorizationURL(self):
        """
        Retrieve the value for the "AuthorizationURL" output from this Choreo execution. ((string) The authorization URL that the application's user needs to go to in order to grant access to your application.)
        """
        return self._output.get('AuthorizationURL', None)
    def get_CallbackID(self):
        """
        Retrieve the value for the "CallbackID" output from this Choreo execution. ((string) An ID used to retrieve the callback data that Temboo stores once your application's user authorizes.)
        """
        return self._output.get('CallbackID', None)

class InitializeOAuthChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InitializeOAuthResultSet(response, path)
