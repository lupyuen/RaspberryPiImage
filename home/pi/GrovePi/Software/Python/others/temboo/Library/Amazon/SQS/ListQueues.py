# -*- coding: utf-8 -*-

###############################################################################
#
# ListQueues
# Returns a list of your queues.
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

class ListQueues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListQueues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListQueues, self).__init__(temboo_session, '/Library/Amazon/SQS/ListQueues')


    def new_input_set(self):
        return ListQueuesInputSet()

    def _make_result_set(self, result, path):
        return ListQueuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListQueuesChoreographyExecution(session, exec_id, path)

class ListQueuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListQueues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListQueuesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListQueuesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_QueueNamePrefix(self, value):
        """
        Set the value of the QueueNamePrefix input for this Choreo. ((optional, string) A string used to filter the list of queues.)
        """
        super(ListQueuesInputSet, self)._set_input('QueueNamePrefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListQueuesInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(ListQueuesInputSet, self)._set_input('UserRegion', value)

class ListQueuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListQueues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ListQueuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListQueuesResultSet(response, path)
