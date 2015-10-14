# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUser
# Updates the name and/or the path of a specified user.
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

class UpdateUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateUser, self).__init__(temboo_session, '/Library/Amazon/IAM/UpdateUser')


    def new_input_set(self):
        return UpdateUserInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserChoreographyExecution(session, exec_id, path)

class UpdateUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UpdateUserInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UpdateUserInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_NewPath(self, value):
        """
        Set the value of the NewPath input for this Choreo. ((optional, string) The new path for the user. Include a value here only if you are changing the user's existing path. The path needs to start with and end with a slash(/).  For example, "/Division/HR/".)
        """
        super(UpdateUserInputSet, self)._set_input('NewPath', value)
    def set_NewUserName(self, value):
        """
        Set the value of the NewUserName input for this Choreo. ((optional, string) The new name of the user. Include a value here only if you are updating the user's name.)
        """
        super(UpdateUserInputSet, self)._set_input('NewUserName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UpdateUserInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) The name of the user to update.)
        """
        super(UpdateUserInputSet, self)._set_input('UserName', value)

class UpdateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateUserResultSet(response, path)
