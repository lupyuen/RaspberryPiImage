# -*- coding: utf-8 -*-

###############################################################################
#
# AddPermission
# Creates a statement for a topic's access control policy which allows an AWS account to have access to the specified Amazon SNS actions.
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

class AddPermission(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddPermission Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddPermission, self).__init__(temboo_session, '/Library/Amazon/SNS/AddPermission')


    def new_input_set(self):
        return AddPermissionInputSet()

    def _make_result_set(self, result, path):
        return AddPermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPermissionChoreographyExecution(session, exec_id, path)

class AddPermissionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddPermission
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(AddPermissionInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The AWS account number of the user that will be granted access to a specified action. Enter account number omitting any dashes.)
        """
        super(AddPermissionInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(AddPermissionInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ActionName(self, value):
        """
        Set the value of the ActionName input for this Choreo. ((required, string) The action you want to allow for a specified user (i.e. DeleteTopic, Publish, GetTopicAttributes, etc).)
        """
        super(AddPermissionInputSet, self)._set_input('ActionName', value)
    def set_Label(self, value):
        """
        Set the value of the Label input for this Choreo. ((required, string) The unique identifier for the new policy statement.)
        """
        super(AddPermissionInputSet, self)._set_input('Label', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic whos access control policy you want to adjust.)
        """
        super(AddPermissionInputSet, self)._set_input('TopicArn', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(AddPermissionInputSet, self)._set_input('UserRegion', value)

class AddPermissionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddPermission Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class AddPermissionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddPermissionResultSet(response, path)
