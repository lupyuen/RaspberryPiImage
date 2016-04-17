# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketRequestPayment
# Sets the request payment configuration of a bucket. 
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

class PutBucketRequestPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketRequestPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketRequestPayment, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketRequestPayment')


    def new_input_set(self):
        return PutBucketRequestPaymentInputSet()

    def _make_result_set(self, result, path):
        return PutBucketRequestPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketRequestPaymentChoreographyExecution(session, exec_id, path)

class PutBucketRequestPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketRequestPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketRequestPaymentInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketRequestPaymentInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create a request payment configuration for.)
        """
        super(PutBucketRequestPaymentInputSet, self)._set_input('BucketName', value)
    def set_Payer(self, value):
        """
        Set the value of the Payer input for this Choreo. ((required, string) Specifies who pays for the download and request fees. Valid values:  Requester or BucketOwner.)
        """
        super(PutBucketRequestPaymentInputSet, self)._set_input('Payer', value)

class PutBucketRequestPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketRequestPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful execution, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketRequestPaymentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketRequestPaymentResultSet(response, path)
