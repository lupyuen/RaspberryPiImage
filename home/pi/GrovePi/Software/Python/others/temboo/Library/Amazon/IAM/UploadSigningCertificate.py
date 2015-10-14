# -*- coding: utf-8 -*-

###############################################################################
#
# UploadSigningCertificate
# Uploads an X.509 signing certificate and associates it with the specified user.
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

class UploadSigningCertificate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadSigningCertificate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UploadSigningCertificate, self).__init__(temboo_session, '/Library/Amazon/IAM/UploadSigningCertificate')


    def new_input_set(self):
        return UploadSigningCertificateInputSet()

    def _make_result_set(self, result, path):
        return UploadSigningCertificateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadSigningCertificateChoreographyExecution(session, exec_id, path)

class UploadSigningCertificateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadSigningCertificate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UploadSigningCertificateInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UploadSigningCertificateInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_CertificateBody(self, value):
        """
        Set the value of the CertificateBody input for this Choreo. ((required, multiline) The contents of the signing certificate.)
        """
        super(UploadSigningCertificateInputSet, self)._set_input('CertificateBody', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UploadSigningCertificateInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((optional, string) The name of the user.)
        """
        super(UploadSigningCertificateInputSet, self)._set_input('UserName', value)

class UploadSigningCertificateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadSigningCertificate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UploadSigningCertificateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadSigningCertificateResultSet(response, path)
