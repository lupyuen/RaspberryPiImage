# -*- coding: utf-8 -*-

###############################################################################
#
# ZipObject
# Creates a zipped version of the specified S3 file and returns a download link for the new compressed file.
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

class ZipObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ZipObject, self).__init__(temboo_session, '/Library/Amazon/S3/ZipObject')


    def new_input_set(self):
        return ZipObjectInputSet()

    def _make_result_set(self, result, path):
        return ZipObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipObjectChoreographyExecution(session, exec_id, path)

class ZipObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ZipObjectInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ZipObjectInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the object to retrieve and zip.)
        """
        super(ZipObjectInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((conditional, string) This sets the permissions for the newly created zip file. Valid values are: private, public-read, public-read-write, authenticated-read, bucket-owner-read, or bucket-owner-full-control.)
        """
        super(ZipObjectInputSet, self)._set_input('CannedACL', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file to retrieve and zip.)
        """
        super(ZipObjectInputSet, self)._set_input('FileName', value)
    def set_ZipFileLocation(self, value):
        """
        Set the value of the ZipFileLocation input for this Choreo. ((optional, string) The name of the bucket to put the new zip file in. When not specified, the zip file will be put in the bucket where the original uncompressed file is located.)
        """
        super(ZipObjectInputSet, self)._set_input('ZipFileLocation', value)
    def set_ZipFileName(self, value):
        """
        Set the value of the ZipFileName input for this Choreo. ((optional, string) The name of the zip file that will be created. If not specified, the original file name will be used with .zip extension.)
        """
        super(ZipObjectInputSet, self)._set_input('ZipFileName', value)

class ZipObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The URL location of the new zip file.)
        """
        return self._output.get('URL', None)

class ZipObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ZipObjectResultSet(response, path)
