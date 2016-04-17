# -*- coding: utf-8 -*-

###############################################################################
#
# SetTopicAttributes
# Allows a topic owner to update the attribute of a topic to a new value.
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

class SetTopicAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetTopicAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetTopicAttributes, self).__init__(temboo_session, '/Library/Amazon/SNS/SetTopicAttributes')


    def new_input_set(self):
        return SetTopicAttributesInputSet()

    def _make_result_set(self, result, path):
        return SetTopicAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetTopicAttributesChoreographyExecution(session, exec_id, path)

class SetTopicAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetTopicAttributes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((required, string) The name of the attribute you want to modify. Valid values are: Policy and DisplayName.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('AttributeName', value)
    def set_AttributeValue(self, value):
        """
        Set the value of the AttributeValue input for this Choreo. ((required, string) The new value for the attribute that you want to update.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('AttributeValue', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic that has an attribute that you want to set.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('TopicArn', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(SetTopicAttributesInputSet, self)._set_input('UserRegion', value)

class SetTopicAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetTopicAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class SetTopicAttributesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetTopicAttributesResultSet(response, path)
