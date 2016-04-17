# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateConnectApp
# Updates the details for an individual Connect App associated with a Twilio account.
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

class UpdateConnectApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateConnectApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateConnectApp, self).__init__(temboo_session, '/Library/Twilio/ConnectApps/UpdateConnectApp')


    def new_input_set(self):
        return UpdateConnectAppInputSet()

    def _make_result_set(self, result, path):
        return UpdateConnectAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateConnectAppChoreographyExecution(session, exec_id, path)

class UpdateConnectAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateConnectApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('AuthToken', value)
    def set_AuthorizeRedirectURL(self, value):
        """
        Set the value of the AuthorizeRedirectURL input for this Choreo. ((optional, string) The URL the user's browser will redirect to after Twilio authenticates the user and obtains authorization for this Connect App.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('AuthorizeRedirectURL', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) The company name for this Connect App.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('CompanyName', value)
    def set_ConnectAppSID(self, value):
        """
        Set the value of the ConnectAppSID input for this Choreo. ((required, string) The id of the Connect App to update.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('ConnectAppSID', value)
    def set_DeauthorizeCallbackMethod(self, value):
        """
        Set the value of the DeauthorizeCallbackMethod input for this Choreo. ((optional, string) The HTTP method to be used when making a request to the DeauthorizeCallbackUrl. Either GET or POST.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('DeauthorizeCallbackMethod', value)
    def set_DeauthorizeCallbackURL(self, value):
        """
        Set the value of the DeauthorizeCallbackURL input for this Choreo. ((optional, string) The URL to which Twilio will send a request when a user de-authorizes this Connect App.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('DeauthorizeCallbackURL', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A more detailed human readable description of the Connect App.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('Description', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) A human readable description of the Connect App, with maximum length 64 characters.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('FriendlyName', value)
    def set_HomepageURL(self, value):
        """
        Set the value of the HomepageURL input for this Choreo. ((optional, string) The public URL where users can obtain more information about this Connect App.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('HomepageURL', value)
    def set_Permissions(self, value):
        """
        Set the value of the Permissions input for this Choreo. ((optional, string) A comma-separated list of permssions you will request from users of this ConnectApp. Valid permssions are get-all or post-all.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('Permissions', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(UpdateConnectAppInputSet, self)._set_input('ResponseFormat', value)

class UpdateConnectAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateConnectApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class UpdateConnectAppChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateConnectAppResultSet(response, path)
