# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopicAttributes
# Returns properties for a specified topic.
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

class GetTopicAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopicAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTopicAttributes, self).__init__(temboo_session, '/Library/Amazon/SNS/GetTopicAttributes')


    def new_input_set(self):
        return GetTopicAttributesInputSet()

    def _make_result_set(self, result, path):
        return GetTopicAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopicAttributesChoreographyExecution(session, exec_id, path)

class GetTopicAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopicAttributes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetTopicAttributesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetTopicAttributesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic you want to retrieve attributes for.)
        """
        super(GetTopicAttributesInputSet, self)._set_input('TopicArn', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(GetTopicAttributesInputSet, self)._set_input('UserRegion', value)

class GetTopicAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopicAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetTopicAttributesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTopicAttributesResultSet(response, path)
