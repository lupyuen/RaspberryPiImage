# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketACL
# Sets the access control list (ACL) permissions for an existing bucket.
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

class PutBucketACL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketACL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketACL, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketACL')


    def new_input_set(self):
        return PutBucketACLInputSet()

    def _make_result_set(self, result, path):
        return PutBucketACLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketACLChoreographyExecution(session, exec_id, path)

class PutBucketACLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketACL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketACLInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketACLInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AccessControlList(self, value):
        """
        Set the value of the AccessControlList input for this Choreo. ((optional, xml) Custom Access Control List xml for advanced configuration. See description for an example, plus Amazon documentation.)
        """
        super(PutBucketACLInputSet, self)._set_input('AccessControlList', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create or update a policy for.)
        """
        super(PutBucketACLInputSet, self)._set_input('BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((conditional, string) Most common ACL usage, required unless creating a custom policy. Values: private, public-read, public-read-write, or authenticated-read.)
        """
        super(PutBucketACLInputSet, self)._set_input('CannedACL', value)
    def set_OwnerEmailAddress(self, value):
        """
        Set the value of the OwnerEmailAddress input for this Choreo. ((optional, string) The email address of the owner who is granting permission. Required if creating your own custom ACL policy.)
        """
        super(PutBucketACLInputSet, self)._set_input('OwnerEmailAddress', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The canonical user ID of the owner who is granting permission. Required if creating your own custom ACL policy.)
        """
        super(PutBucketACLInputSet, self)._set_input('OwnerId', value)

class PutBucketACLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketACL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful ACL creation, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketACLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketACLResultSet(response, path)
