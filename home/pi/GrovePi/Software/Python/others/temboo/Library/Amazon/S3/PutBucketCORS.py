# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketCORS
# Sets the CORS (Cross-Origin Resource Sharing) configuration for a specified bucket.
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

class PutBucketCORS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketCORS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketCORS, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketCORS')


    def new_input_set(self):
        return PutBucketCORSInputSet()

    def _make_result_set(self, result, path):
        return PutBucketCORSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketCORSChoreographyExecution(session, exec_id, path)

class PutBucketCORSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketCORS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CORSConfiguration(self, value):
        """
        Set the value of the CORSConfiguration input for this Choreo. ((optional, xml) The CORS Configuration XML containing one or more CORS Rules for advanced configuration. If provided the Choreo will ignore all other inputs except your AWS Key/Secret and BucketName.)
        """
        super(PutBucketCORSInputSet, self)._set_input('CORSConfiguration', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketCORSInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketCORSInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AllowedHeader(self, value):
        """
        Set the value of the AllowedHeader input for this Choreo. ((optional, string) Specifies which headers are allowed in a pre-flight OPTIONS request via the Access-Control-Request-Headers header.)
        """
        super(PutBucketCORSInputSet, self)._set_input('AllowedHeader', value)
    def set_AllowedMethod(self, value):
        """
        Set the value of the AllowedMethod input for this Choreo. ((conditional, string) The HTTP verb that you want to allow the origin to execute. Valid values are: GET, PUT, HEAD, POST, DELETE.)
        """
        super(PutBucketCORSInputSet, self)._set_input('AllowedMethod', value)
    def set_AllowedOrigin(self, value):
        """
        Set the value of the AllowedOrigin input for this Choreo. ((conditional, string) An origin that you want to allow cross-domain requests from. This can contain at most one * wild character (i.e. http://*.example.com).)
        """
        super(PutBucketCORSInputSet, self)._set_input('AllowedOrigin', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to set a CORS configuration for.)
        """
        super(PutBucketCORSInputSet, self)._set_input('BucketName', value)
    def set_ExposeHeader(self, value):
        """
        Set the value of the ExposeHeader input for this Choreo. ((optional, string) A header in the response that you want customers to be able to access from their applications.)
        """
        super(PutBucketCORSInputSet, self)._set_input('ExposeHeader', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((optional, string) A unique identifier for the rule. The ID value can be up to 255 characters long.)
        """
        super(PutBucketCORSInputSet, self)._set_input('ID', value)
    def set_MaxAgeSeconds(self, value):
        """
        Set the value of the MaxAgeSeconds input for this Choreo. ((optional, integer) The time in seconds that your browser is to cache the preflight response for the specified resource.)
        """
        super(PutBucketCORSInputSet, self)._set_input('MaxAgeSeconds', value)

class PutBucketCORSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketCORS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that for a successful exection, this API operation returns an empty 200 response.)
        """
        return self._output.get('Response', None)

class PutBucketCORSChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketCORSResultSet(response, path)
