# -*- coding: utf-8 -*-

###############################################################################
#
# ReceiveMessage
# Returns one or more messages from the specified queue.
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

class ReceiveMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReceiveMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReceiveMessage, self).__init__(temboo_session, '/Library/Amazon/SQS/ReceiveMessage')


    def new_input_set(self):
        return ReceiveMessageInputSet()

    def _make_result_set(self, result, path):
        return ReceiveMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReceiveMessageChoreographyExecution(session, exec_id, path)

class ReceiveMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReceiveMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ReceiveMessageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The id for the AWS account associated with the queue you're retrieving a message from (remove all dashes in the account number).)
        """
        super(ReceiveMessageInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ReceiveMessageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((optional, string) The attribute you wish to return. Values are: All (default), SenderId, SentTimestamp, ApproximateReceiveCount, or ApproximateFirstReceiveTimestamp.)
        """
        super(ReceiveMessageInputSet, self)._set_input('AttributeName', value)
    def set_MaxNumberOfMessages(self, value):
        """
        Set the value of the MaxNumberOfMessages input for this Choreo. ((optional, integer) The maximum number of messages to return. Defaults to 1.)
        """
        super(ReceiveMessageInputSet, self)._set_input('MaxNumberOfMessages', value)
    def set_MessageAttributeName(self, value):
        """
        Set the value of the MessageAttributeName input for this Choreo. ((optional, string) The name of a message attribute to return. You can return all of the attributes by specifying "All".)
        """
        super(ReceiveMessageInputSet, self)._set_input('MessageAttributeName', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to retrieve a message from.)
        """
        super(ReceiveMessageInputSet, self)._set_input('QueueName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ReceiveMessageInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(ReceiveMessageInputSet, self)._set_input('UserRegion', value)
    def set_VisibilityTimeout(self, value):
        """
        Set the value of the VisibilityTimeout input for this Choreo. ((optional, integer) The duration (in seconds) that the received messages are hidden from future retrieve requests after a ReceiveMessage request (max is 43200).)
        """
        super(ReceiveMessageInputSet, self)._set_input('VisibilityTimeout', value)
    def set_WaitTimeSeconds(self, value):
        """
        Set the value of the WaitTimeSeconds input for this Choreo. ((optional, integer) The duration (in seconds) for which the call will wait for a message to arrive in the queue before returning. If a message is available, the call will return sooner than WaitTimeSeconds.)
        """
        super(ReceiveMessageInputSet, self)._set_input('WaitTimeSeconds', value)

class ReceiveMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReceiveMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_Body(self):
        """
        Retrieve the value for the "Body" output from this Choreo execution. ((string) The body of the latest message.)
        """
        return self._output.get('Body', None)
    def get_MessageId(self):
        """
        Retrieve the value for the "MessageId" output from this Choreo execution. ((string) A unique identifier for the latest message.)
        """
        return self._output.get('MessageId', None)
    def get_ReceiptHandle(self):
        """
        Retrieve the value for the "ReceiptHandle" output from this Choreo execution. ((string) An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. Provide the last received receipt handle to delete the message.)
        """
        return self._output.get('ReceiptHandle', None)

class ReceiveMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReceiveMessageResultSet(response, path)
