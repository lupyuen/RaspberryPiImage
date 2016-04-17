# -*- coding: utf-8 -*-

###############################################################################
#
# SetupApp
# Sets up a previously activated app.
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

class SetupApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetupApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetupApp, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/SetupApp')


    def new_input_set(self):
        return SetupAppInputSet()

    def _make_result_set(self, result, path):
        return SetupAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetupAppChoreographyExecution(session, exec_id, path)

class SetupAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetupApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(SetupAppInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(SetupAppInputSet, self)._set_input('APIUser', value)
    def set_AppName(self, value):
        """
        Set the value of the AppName input for this Choreo. ((required, string) The name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        super(SetupAppInputSet, self)._set_input('AppName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Enter the password for the app that is being setup.  For example, if setting up a Twitter app, enter a valid Twitter account password.)
        """
        super(SetupAppInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(SetupAppInputSet, self)._set_input('ResponseFormat', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username for the app that is being setup. For example, if setting up a Twitter app, enter a valid Twitter account username.)
        """
        super(SetupAppInputSet, self)._set_input('Username', value)


class SetupAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetupApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class SetupAppChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetupAppResultSet(response, path)
