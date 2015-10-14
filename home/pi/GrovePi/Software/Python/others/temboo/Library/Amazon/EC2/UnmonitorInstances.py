# -*- coding: utf-8 -*-

###############################################################################
#
# UnmonitorInstances
# Disable monitoring for a specified instance.
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

class UnmonitorInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UnmonitorInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UnmonitorInstances, self).__init__(temboo_session, '/Library/Amazon/EC2/UnmonitorInstances')


    def new_input_set(self):
        return UnmonitorInstancesInputSet()

    def _make_result_set(self, result, path):
        return UnmonitorInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnmonitorInstancesChoreographyExecution(session, exec_id, path)

class UnmonitorInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UnmonitorInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UnmonitorInstancesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UnmonitorInstancesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The ID(s) of the instance(s) you want to stop monitoring. This can be a comma-separated list of up to 10 instance IDs.)
        """
        super(UnmonitorInstancesInputSet, self)._set_input('InstanceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UnmonitorInstancesInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(UnmonitorInstancesInputSet, self)._set_input('UserRegion', value)

class UnmonitorInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UnmonitorInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UnmonitorInstancesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UnmonitorInstancesResultSet(response, path)
