# -*- coding: utf-8 -*-

###############################################################################
#
# CreateQueue
# Creates a new queue with a specified queue name.
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

class CreateQueue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateQueue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateQueue, self).__init__(temboo_session, '/Library/Amazon/SQS/CreateQueue')


    def new_input_set(self):
        return CreateQueueInputSet()

    def _make_result_set(self, result, path):
        return CreateQueueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateQueueChoreographyExecution(session, exec_id, path)

class CreateQueueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateQueue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateQueueInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateQueueInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DefaultVisibilityTimeout(self, value):
        """
        Set the value of the DefaultVisibilityTimeout input for this Choreo. ((optional, integer) The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30.)
        """
        super(CreateQueueInputSet, self)._set_input('DefaultVisibilityTimeout', value)
    def set_MaximumMessageSize(self, value):
        """
        Set the value of the MaximumMessageSize input for this Choreo. ((optional, integer) The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB))
        """
        super(CreateQueueInputSet, self)._set_input('MaximumMessageSize', value)
    def set_MessageRetentionPeriod(self, value):
        """
        Set the value of the MessageRetentionPeriod input for this Choreo. ((optional, integer) The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).)
        """
        super(CreateQueueInputSet, self)._set_input('MessageRetentionPeriod', value)
    def set_Policy(self, value):
        """
        Set the value of the Policy input for this Choreo. ((optional, json) The queue's policy.)
        """
        super(CreateQueueInputSet, self)._set_input('Policy', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to create.)
        """
        super(CreateQueueInputSet, self)._set_input('QueueName', value)
    def set_ReceiveMessageWaitTimeSeconds(self, value):
        """
        Set the value of the ReceiveMessageWaitTimeSeconds input for this Choreo. ((optional, integer) The time for which a ReceiveMessage call will wait for a message to arrive. An integer from 0 to 20 (seconds). The default for this attribute is 0.)
        """
        super(CreateQueueInputSet, self)._set_input('ReceiveMessageWaitTimeSeconds', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateQueueInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(CreateQueueInputSet, self)._set_input('UserRegion', value)

class CreateQueueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateQueue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateQueueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateQueueResultSet(response, path)
