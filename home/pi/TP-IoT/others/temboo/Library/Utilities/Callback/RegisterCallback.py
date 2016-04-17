# -*- coding: utf-8 -*-

###############################################################################
#
# RegisterCallback
# Allows you to generate a unique URL that can "listen" for incoming data from web request.
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

class RegisterCallback(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegisterCallback Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RegisterCallback, self).__init__(temboo_session, '/Library/Utilities/Callback/RegisterCallback')


    def new_input_set(self):
        return RegisterCallbackInputSet()

    def _make_result_set(self, result, path):
        return RegisterCallbackResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegisterCallbackChoreographyExecution(session, exec_id, path)

class RegisterCallbackInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegisterCallback
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CustomCallbackD(self, value):
        """
        Set the value of the CustomCallbackD input for this Choreo. ((optional, string) This value is used to register a unique URL associated with your account. If omitted, a random identifier is generated. Using a custom value here is useful when you need the URL to be static.)
        """
        super(RegisterCallbackInputSet, self)._set_input('CustomCallbackD', value)
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((optional, string) When using a Custom Callback ID, it can be useful to filter requests using a query parameter. This value is used as a query parameter name, and can be used to lookup request data.)
        """
        super(RegisterCallbackInputSet, self)._set_input('FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((optional, string) When using a Custom Callback ID, it can be useful to filter requests using a query parameter. This value is used as a query parameter value, and can be used to lookup request data.)
        """
        super(RegisterCallbackInputSet, self)._set_input('FilterValue', value)
    def set_ForwardingURL(self, value):
        """
        Set the value of the ForwardingURL input for this Choreo. ((optional, string) The URL that Temboo will redirect a users to after they visit your URL. This should include the "https://" or "http://" prefix and be a fully qualified URL.)
        """
        super(RegisterCallbackInputSet, self)._set_input('ForwardingURL', value)

class RegisterCallbackResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegisterCallback Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_CallbackID(self):
        """
        Retrieve the value for the "CallbackID" output from this Choreo execution. ((string) The ID that can used to retrieve request data that the Callback URL captures.)
        """
        return self._output.get('CallbackID', None)
    def get_CallbackURL(self):
        """
        Retrieve the value for the "CallbackURL" output from this Choreo execution. ((string) The URL that is listening for an incoming request. Note that this URL will expire in 10 minutes.)
        """
        return self._output.get('CallbackURL', None)

class RegisterCallbackChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RegisterCallbackResultSet(response, path)
