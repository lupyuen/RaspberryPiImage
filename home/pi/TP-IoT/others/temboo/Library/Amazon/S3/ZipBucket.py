# -*- coding: utf-8 -*-

###############################################################################
#
# ZipBucket
# Creates a zip file containing all objects within the specified bucket and returns a download link for the new compressed file.
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

class ZipBucket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipBucket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ZipBucket, self).__init__(temboo_session, '/Library/Amazon/S3/ZipBucket')


    def new_input_set(self):
        return ZipBucketInputSet()

    def _make_result_set(self, result, path):
        return ZipBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipBucketChoreographyExecution(session, exec_id, path)

class ZipBucketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipBucket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ZipBucketInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ZipBucketInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the list of objects that you want to zip.)
        """
        super(ZipBucketInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((conditional, string) This sets the permissions for the newly created zip file. Valid values are: private, public-read, public-read-write, authenticated-read, bucket-owner-read, or bucket-owner-full-control.)
        """
        super(ZipBucketInputSet, self)._set_input('CannedACL', value)
    def set_Delimiter(self, value):
        """
        Set the value of the Delimiter input for this Choreo. ((optional, string) A delimiter is a character you use to group keys. All keys that contain the delimiter are grouped under a single result element, Common Prefixes. For more information see Amazon documentation.)
        """
        super(ZipBucketInputSet, self)._set_input('Delimiter', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((optional, string) Limits the response to keys that begin with the specified prefix - useful for separating a bucket into different groupings of keys. Ex: specify 'test' to get a list of objects starting with 'test'.)
        """
        super(ZipBucketInputSet, self)._set_input('Prefix', value)
    def set_ZipFileLocation(self, value):
        """
        Set the value of the ZipFileLocation input for this Choreo. ((optional, string) The name of the bucket to put the new zip file in. When not specified, the zip file will be put in the bucket that contains the files being zipped.)
        """
        super(ZipBucketInputSet, self)._set_input('ZipFileLocation', value)
    def set_ZipFileName(self, value):
        """
        Set the value of the ZipFileName input for this Choreo. ((optional, string) The name of the zip file that will be created. If not specified, the original bucket name will be used with .zip extension.)
        """
        super(ZipBucketInputSet, self)._set_input('ZipFileName', value)

class ZipBucketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipBucket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The URL location of the new zip file.)
        """
        return self._output.get('URL', None)

class ZipBucketChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ZipBucketResultSet(response, path)
