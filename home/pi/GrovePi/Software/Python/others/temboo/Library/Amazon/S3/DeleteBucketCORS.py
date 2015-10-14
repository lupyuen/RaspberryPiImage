# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteBucketCORS
# Deletes the CORS (Cross-Origin Resource Sharing) configuration information set for the specified bucket.
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

class DeleteBucketCORS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteBucketCORS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteBucketCORS, self).__init__(temboo_session, '/Library/Amazon/S3/DeleteBucketCORS')


    def new_input_set(self):
        return DeleteBucketCORSInputSet()

    def _make_result_set(self, result, path):
        return DeleteBucketCORSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBucketCORSChoreographyExecution(session, exec_id, path)

class DeleteBucketCORSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteBucketCORS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteBucketCORSInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteBucketCORSInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that the CORS configuration should be removed from.)
        """
        super(DeleteBucketCORSInputSet, self)._set_input('BucketName', value)

class DeleteBucketCORSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteBucketCORS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that for a successful exection, this API operation returns an empty 204 response.)
        """
        return self._output.get('Response', None)

class DeleteBucketCORSChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteBucketCORSResultSet(response, path)
