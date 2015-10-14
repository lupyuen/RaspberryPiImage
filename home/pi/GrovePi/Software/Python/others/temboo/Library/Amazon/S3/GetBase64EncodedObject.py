# -*- coding: utf-8 -*-

###############################################################################
#
# GetBase64EncodedObject
# Retrieves a specified item from an Amazon S3 bucket, returns the file content as base64-encoded data, and returns the values of key response headers as output variables if available.
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

class GetBase64EncodedObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBase64EncodedObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBase64EncodedObject, self).__init__(temboo_session, '/Library/Amazon/S3/GetBase64EncodedObject')


    def new_input_set(self):
        return GetBase64EncodedObjectInputSet()

    def _make_result_set(self, result, path):
        return GetBase64EncodedObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBase64EncodedObjectChoreographyExecution(session, exec_id, path)

class GetBase64EncodedObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBase64EncodedObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the object to retrieve.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('BucketName', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file to retrieve.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('FileName', value)
    def set_IfMatch(self, value):
        """
        Set the value of the IfMatch input for this Choreo. ((optional, string) Returns the object only if its entity tag (ETag) is the same as the one specified, otherwise returns a 412 (precondition failed) error.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('IfMatch', value)
    def set_IfModifiedSince(self, value):
        """
        Set the value of the IfModifiedSince input for this Choreo. ((optional, date) Returns the object only if it has been modified since the specific time, otherwise returns a 304 (not modified) error.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('IfModifiedSince', value)
    def set_IfNoneMatch(self, value):
        """
        Set the value of the IfNoneMatch input for this Choreo. ((optional, string) Returns the object only if its entity tag (ETag) is different from the one specified, otherwise retuns a 304 (not modified) error. Will not work correctly with IfModifiedSince.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('IfNoneMatch', value)
    def set_IfUnmodifiedSince(self, value):
        """
        Set the value of the IfUnmodifiedSince input for this Choreo. ((optional, date) Returns the object only if it has not been modified since the specified time, otherwise returns a 412 (precondition failed) error.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('IfUnmodifiedSince', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((optional, string) Downloads the specific range of bytes of an object. Ex: 0-9 (returns the first 10 bytes of an object), 100-1000, etc. If the range value exceeds the end of file, it will return up to the end of file.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('Range', value)
    def set_SSECAlgorithm(self, value):
        """
        Set the value of the SSECAlgorithm input for this Choreo. ((optional, string) Specifies the server-side encryption with customer-provided encryption keys (SSE-C) algorithm used when Amazon S3 created the target object. Valid value: AES256.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('SSECAlgorithm', value)
    def set_SSECKey(self, value):
        """
        Set the value of the SSECKey input for this Choreo. ((optional, string) The customer-provided AES-256 256-bit (32-byte) encryption key for Amazon S3 to use to encrypt or decrypt your data.)
        """
        super(GetBase64EncodedObjectInputSet, self)._set_input('SSECKey', value)

class GetBase64EncodedObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBase64EncodedObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The base64-encoded contents of the file you are retrieving.)
        """
        return self._output.get('Response', None)
    def get_DeleteMarker(self):
        """
        Retrieve the value for the "DeleteMarker" output from this Choreo execution. ((boolean) Returns true if the object retrieved was a Delete Marker otherwise no value.)
        """
        return self._output.get('DeleteMarker', None)
    def get_Expiration(self):
        """
        Retrieve the value for the "Expiration" output from this Choreo execution. ((string) Appears if the object expiration is configured. It includes expiry-date and URL-encoded rule-id key value pairs providing object expiration information.)
        """
        return self._output.get('Expiration', None)
    def get_Restore(self):
        """
        Retrieve the value for the "Restore" output from this Choreo execution. ((string) Provides information about the object restoration operation and expiration time of the restored object copy.)
        """
        return self._output.get('Restore', None)
    def get_ServerSideEncryption(self):
        """
        Retrieve the value for the "ServerSideEncryption" output from this Choreo execution. ((string) If the object is stored using server-side encryption, response includes this header with value of the encryption algorithm used. Valid Values: AES256.)
        """
        return self._output.get('ServerSideEncryption', None)
    def get_VersionID(self):
        """
        Retrieve the value for the "VersionID" output from this Choreo execution. ((string) Returns the version ID of the retrieved object if it has a unique version ID.)
        """
        return self._output.get('VersionID', None)
    def get_WebsiteRedirectLocation(self):
        """
        Retrieve the value for the "WebsiteRedirectLocation" output from this Choreo execution. ((string) For a bucket configured as a website, this metadata can be set so the website will evaluate the request for the object as a 301 redirect to another object in the same bucket or an external URL.)
        """
        return self._output.get('WebsiteRedirectLocation', None)

class GetBase64EncodedObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBase64EncodedObjectResultSet(response, path)
