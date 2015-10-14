# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucket
# Creates a new bucket in your Amazon S3 account.
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

class PutBucket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucket, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucket')


    def new_input_set(self):
        return PutBucketInputSet()

    def _make_result_set(self, result, path):
        return PutBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketChoreographyExecution(session, exec_id, path)

class PutBucketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be created.)
        """
        super(PutBucketInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((optional, string) By default all objects are private (only owner has full access control). Valid values: private, public-read, public-read-write, authenticated-read, bucket-owner-read, bucket-owner-full-control.)
        """
        super(PutBucketInputSet, self)._set_input('CannedACL', value)
    def set_LocationConstraint(self, value):
        """
        Set the value of the LocationConstraint input for this Choreo. ((optional, string) The region to create the bucket in. Valid Values: EU, eu-west-1, us-west-1, us-west-2, ap-southeast-1, ap-southeast-2, ap-northeast-1, sa-east-1, empty string (Default US Classic Region). )
        """
        super(PutBucketInputSet, self)._set_input('LocationConstraint', value)

class PutBucketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for successful uploads.)
        """
        return self._output.get('Response', None)

class PutBucketChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketResultSet(response, path)
