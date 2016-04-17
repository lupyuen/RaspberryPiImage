# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketPolicy
# Allows you to add to or replace a policy on a bucket.
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

class PutBucketPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketPolicy, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketPolicy')


    def new_input_set(self):
        return PutBucketPolicyInputSet()

    def _make_result_set(self, result, path):
        return PutBucketPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketPolicyChoreographyExecution(session, exec_id, path)

class PutBucketPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Policy(self, value):
        """
        Set the value of the Policy input for this Choreo. ((required, json) A JSON string containing the policy information.  See Choreo documentation for a sample JSON policy.)
        """
        super(PutBucketPolicyInputSet, self)._set_input('Policy', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketPolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketPolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create or update a policy for.)
        """
        super(PutBucketPolicyInputSet, self)._set_input('BucketName', value)

class PutBucketPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful policy creation, no content is returned and this output variable is empty.)
        """
        return self._output.get('Response', None)

class PutBucketPolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketPolicyResultSet(response, path)
