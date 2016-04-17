# -*- coding: utf-8 -*-

###############################################################################
#
# CreateLoginProfile
# Creates a password for the specified user, which gives the user the ability to access AWS services through the AWS Management Console.
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

class CreateLoginProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateLoginProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateLoginProfile, self).__init__(temboo_session, '/Library/Amazon/IAM/CreateLoginProfile')


    def new_input_set(self):
        return CreateLoginProfileInputSet()

    def _make_result_set(self, result, path):
        return CreateLoginProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateLoginProfileChoreographyExecution(session, exec_id, path)

class CreateLoginProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateLoginProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateLoginProfileInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateLoginProfileInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_MustChangePassword(self, value):
        """
        Set the value of the MustChangePassword input for this Choreo. ((optional, boolean) Whether or not the user is required to change their password immediately.  Valid values are true/false or 1/0.)
        """
        super(CreateLoginProfileInputSet, self)._set_input('MustChangePassword', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The new password for the user.)
        """
        super(CreateLoginProfileInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateLoginProfileInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) The name of the user to create a password for.)
        """
        super(CreateLoginProfileInputSet, self)._set_input('UserName', value)

class CreateLoginProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateLoginProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateLoginProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateLoginProfileResultSet(response, path)
