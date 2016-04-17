# -*- coding: utf-8 -*-

###############################################################################
#
# UploadServerCertificate
# Uploads a server certificate entity for the AWS account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded.
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

class UploadServerCertificate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadServerCertificate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UploadServerCertificate, self).__init__(temboo_session, '/Library/Amazon/IAM/UploadServerCertificate')


    def new_input_set(self):
        return UploadServerCertificateInputSet()

    def _make_result_set(self, result, path):
        return UploadServerCertificateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadServerCertificateChoreographyExecution(session, exec_id, path)

class UploadServerCertificateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadServerCertificate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_CertificateBody(self, value):
        """
        Set the value of the CertificateBody input for this Choreo. ((required, multiline) The contents of the signing certificate.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('CertificateBody', value)
    def set_CertificateChain(self, value):
        """
        Set the value of the CertificateChain input for this Choreo. ((optional, multiline) The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of the chain.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('CertificateChain', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) The path for the server certificate.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('Path', value)
    def set_PrivateKey(self, value):
        """
        Set the value of the PrivateKey input for this Choreo. ((required, multiline) The contents of the private key in PEM-encoded format.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('PrivateKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UploadServerCertificateInputSet, self)._set_input('ResponseFormat', value)
    def set_ServerCertificateName(self, value):
        """
        Set the value of the ServerCertificateName input for this Choreo. ((required, string) The name for the server certificate. Do not include the path in this value.)
        """
        super(UploadServerCertificateInputSet, self)._set_input('ServerCertificateName', value)

class UploadServerCertificateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadServerCertificate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UploadServerCertificateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadServerCertificateResultSet(response, path)
