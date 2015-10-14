# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketWebsiteRedirect
# Configures the specified bucket as a website and sets the web request redirects to a designated endpoint.
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

class PutBucketWebsiteRedirect(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketWebsiteRedirect Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketWebsiteRedirect, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketWebsiteRedirect')


    def new_input_set(self):
        return PutBucketWebsiteRedirectInputSet()

    def _make_result_set(self, result, path):
        return PutBucketWebsiteRedirectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketWebsiteRedirectChoreographyExecution(session, exec_id, path)

class PutBucketWebsiteRedirectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketWebsiteRedirect
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that you wish to configure.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('BucketName', value)
    def set_CustomWebsiteRedirection(self, value):
        """
        Set the value of the CustomWebsiteRedirection input for this Choreo. ((optional, xml) A custom xml file for adding advanced website redirection rule(s). See description and Amazon  docs for details. Note - inputting a custom xml file will overwrite all other optional input values.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('CustomWebsiteRedirection', value)
    def set_ErrorDocument(self, value):
        """
        Set the value of the ErrorDocument input for this Choreo. ((optional, string) The object key name to use when a 4XX class error occurs. Returns specified page when such an error occurs. Ex.: Error.html.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('ErrorDocument', value)
    def set_HostName(self, value):
        """
        Set the value of the HostName input for this Choreo. ((optional, string) Name of the host where requests will be redirected. Used when setting redirect rules, optional if specifying ReplaceKeyPrefixWith or ReplaceKeyWith input variables). Ex.: example.com.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('HostName', value)
    def set_HttpErrorCodeReturnedEquals(self, value):
        """
        Set the value of the HttpErrorCodeReturnedEquals input for this Choreo. ((optional, string) The HTTP error code condition for which a redirect occurs. If there's an error and the error code equals this value, then the specified redirect is applied. Can use with KeyPrefixEquals. Ex:  404.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('HttpErrorCodeReturnedEquals', value)
    def set_HttpRedirectCode(self, value):
        """
        Set the value of the HttpRedirectCode input for this Choreo. ((optional, string) The HTTP redirect code to use on the response.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('HttpRedirectCode', value)
    def set_KeyPrefixEquals(self, value):
        """
        Set the value of the KeyPrefixEquals input for this Choreo. ((optional, string) The name or prefix condition of the object that will trigger the redirect action. Can use with HttpErrorCodeReturnedEquals. Ex:  Single page: ExamplePage.html, All pages with prefix: /images.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('KeyPrefixEquals', value)
    def set_Protocol(self, value):
        """
        Set the value of the Protocol input for this Choreo. ((optional, string) Sets protocol to use when redirecting requests. Optional if you are specifying either ReplaceKeyPrefixWith or ReplaceKeyWith optional inputs. Possible values: http, https.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('Protocol', value)
    def set_ReplaceKeyPrefixWith(self, value):
        """
        Set the value of the ReplaceKeyPrefixWith input for this Choreo. ((optional, string) The object key prefix to use in the redirect request. Redirects requests to the specified prefix. Cannot be used with ReplaceKeyWith. Ex.: /documents.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('ReplaceKeyPrefixWith', value)
    def set_ReplaceKeyWith(self, value):
        """
        Set the value of the ReplaceKeyWith input for this Choreo. ((optional, string) The specific object key to use in the redirect request. Cannot be used with ReplaceKeyPrefixWith. Ex.: error.html.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('ReplaceKeyWith', value)
    def set_Suffix(self, value):
        """
        Set the value of the Suffix input for this Choreo. ((optional, string) The default page returned when there is a request to a directory. I.e.: if you input index.html, a request for /images/ will return the data for the object '/images/index.html'. Default is index.html.)
        """
        super(PutBucketWebsiteRedirectInputSet, self)._set_input('Suffix', value)

class PutBucketWebsiteRedirectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketWebsiteRedirect Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful website configuration request, no content is returned and this output variable will be empty.)
        """
        return self._output.get('Response', None)

class PutBucketWebsiteRedirectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketWebsiteRedirectResultSet(response, path)
