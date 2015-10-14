# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketWebsiteRedirectAll
# Configures the specified bucket as a website and redirects all web requests to the designated hostname.
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

class PutBucketWebsiteRedirectAll(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketWebsiteRedirectAll Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketWebsiteRedirectAll, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketWebsiteRedirectAll')


    def new_input_set(self):
        return PutBucketWebsiteRedirectAllInputSet()

    def _make_result_set(self, result, path):
        return PutBucketWebsiteRedirectAllResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketWebsiteRedirectAllChoreographyExecution(session, exec_id, path)

class PutBucketWebsiteRedirectAllInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketWebsiteRedirectAll
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketWebsiteRedirectAllInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketWebsiteRedirectAllInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that you wish to configure.)
        """
        super(PutBucketWebsiteRedirectAllInputSet, self)._set_input('BucketName', value)
    def set_HostName(self, value):
        """
        Set the value of the HostName input for this Choreo. ((required, string) Name of the host where requests will be redirected. Ex.: example.com)
        """
        super(PutBucketWebsiteRedirectAllInputSet, self)._set_input('HostName', value)
    def set_Protocol(self, value):
        """
        Set the value of the Protocol input for this Choreo. ((optional, string) Protocol to use (http, https) when redirecting requests. The default is http.)
        """
        super(PutBucketWebsiteRedirectAllInputSet, self)._set_input('Protocol', value)

class PutBucketWebsiteRedirectAllResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketWebsiteRedirectAll Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful website configuration request, no content is returned and this output variable will be empty.)
        """
        return self._output.get('Response', None)

class PutBucketWebsiteRedirectAllChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketWebsiteRedirectAllResultSet(response, path)
