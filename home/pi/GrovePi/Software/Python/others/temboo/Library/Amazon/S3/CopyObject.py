# -*- coding: utf-8 -*-

###############################################################################
#
# CopyObject
# Makes a copy of an existing object in S3 Storage.
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

class CopyObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CopyObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CopyObject, self).__init__(temboo_session, '/Library/Amazon/S3/CopyObject')


    def new_input_set(self):
        return CopyObjectInputSet()

    def _make_result_set(self, result, path):
        return CopyObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyObjectChoreographyExecution(session, exec_id, path)

class CopyObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CopyObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CopyObjectInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CopyObjectInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be the file destination.)
        """
        super(CopyObjectInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((optional, string) By default all objects are private (only owner has full access control). Valid values: private, public-read, public-read-write, authenticated-read, bucket-owner-read, bucket-owner-full-control.)
        """
        super(CopyObjectInputSet, self)._set_input('CannedACL', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) ContentType. Default is application/octet-stream.)
        """
        super(CopyObjectInputSet, self)._set_input('ContentType', value)
    def set_FileToCopy(self, value):
        """
        Set the value of the FileToCopy input for this Choreo. ((required, string) The name of the file to copy.)
        """
        super(CopyObjectInputSet, self)._set_input('FileToCopy', value)
    def set_IfMatch(self, value):
        """
        Set the value of the IfMatch input for this Choreo. ((optional, string) Copies the object if its entity tag (ETag) matches the specified tag; otherwise returns a 412 HTTP status code error (failed precondition).)
        """
        super(CopyObjectInputSet, self)._set_input('IfMatch', value)
    def set_IfModifiedSince(self, value):
        """
        Set the value of the IfModifiedSince input for this Choreo. ((optional, date) Copies if it has been modified since the specified time; otherwise returns a 412 HTTP status code error (failed precondition). Must be valid HTTP date. Can be used with IfMatch only.)
        """
        super(CopyObjectInputSet, self)._set_input('IfModifiedSince', value)
    def set_IfNoneMatch(self, value):
        """
        Set the value of the IfNoneMatch input for this Choreo. ((optional, string) Copies the object if its entity tag (ETag) is different from the specified tag; otherwise returns a 412 HTTP status code error (failed precondition).)
        """
        super(CopyObjectInputSet, self)._set_input('IfNoneMatch', value)
    def set_IfUnmodifiedSince(self, value):
        """
        Set the value of the IfUnmodifiedSince input for this Choreo. ((optional, date) Copies if it hasn't been modified since the specified time; otherwise returns a 412 HTTP status code error (failed precondition). Must be valid HTTP date. Can be used with IfMatch or IfNoneMatch only.)
        """
        super(CopyObjectInputSet, self)._set_input('IfUnmodifiedSince', value)
    def set_NewFileName(self, value):
        """
        Set the value of the NewFileName input for this Choreo. ((required, string) The file name for the new copy.)
        """
        super(CopyObjectInputSet, self)._set_input('NewFileName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CopyObjectInputSet, self)._set_input('ResponseFormat', value)
    def set_SSECAlgorithm(self, value):
        """
        Set the value of the SSECAlgorithm input for this Choreo. ((optional, string) Specifies the server-side encryption with customer-provided encryption keys (SSE-C) algorithm to use when Amazon S3 creates the target object. Valid value: AES256.)
        """
        super(CopyObjectInputSet, self)._set_input('SSECAlgorithm', value)
    def set_SSECKey(self, value):
        """
        Set the value of the SSECKey input for this Choreo. ((optional, string) The customer-provided AES-256 256-bit (32-byte) encryption key for Amazon S3 to use to encrypt or decrypt your copied data object.)
        """
        super(CopyObjectInputSet, self)._set_input('SSECKey', value)
    def set_SSECSourceAlgorithm(self, value):
        """
        Set the value of the SSECSourceAlgorithm input for this Choreo. ((optional, string) Specifies the server-side encryption with customer-provided encryption keys (SSE-C) algorithm to use to decrypt the Amazon S3 source object being copied. Valid value: AES256.)
        """
        super(CopyObjectInputSet, self)._set_input('SSECSourceAlgorithm', value)
    def set_SSECSourceKey(self, value):
        """
        Set the value of the SSECSourceKey input for this Choreo. ((optional, string) The customer-provided AES-256 256-bit (32-byte) encryption key for Amazon S3 to use to decrypt the copy source object.)
        """
        super(CopyObjectInputSet, self)._set_input('SSECSourceKey', value)
    def set_ServerSideEncryption(self, value):
        """
        Set the value of the ServerSideEncryption input for this Choreo. ((optional, string) Specifies the server-side encryption algorithm to use when Amazon S3 creates the target object. Valid value: AES256.)
        """
        super(CopyObjectInputSet, self)._set_input('ServerSideEncryption', value)
    def set_StorageClass(self, value):
        """
        Set the value of the StorageClass input for this Choreo. ((optional, string) Enables RRS customers to store their noncritical, reproducible data at lower levels of redundancy than Amazon S3's standard storage. Valid Values: STANDARD (default), REDUCED_REDUNDANCY.)
        """
        super(CopyObjectInputSet, self)._set_input('StorageClass', value)
    def set_WebsiteRedirectLocation(self, value):
        """
        Set the value of the WebsiteRedirectLocation input for this Choreo. ((optional, string) If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Ex: /anotherPage.html, http://www.page.com. Length limit: 2 K.)
        """
        super(CopyObjectInputSet, self)._set_input('WebsiteRedirectLocation', value)


class CopyObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CopyObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CopyObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CopyObjectResultSet(response, path)
