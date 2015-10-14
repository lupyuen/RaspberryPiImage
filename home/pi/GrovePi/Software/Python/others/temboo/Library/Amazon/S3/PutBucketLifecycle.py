# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketLifecycle
# Sets lifecycle configuration for your bucket. This is used to remove objects from a bucket automatically after a certain time or at a certain date.
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

class PutBucketLifecycle(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketLifecycle Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketLifecycle, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketLifecycle')


    def new_input_set(self):
        return PutBucketLifecycleInputSet()

    def _make_result_set(self, result, path):
        return PutBucketLifecycleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketLifecycleChoreographyExecution(session, exec_id, path)

class PutBucketLifecycleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketLifecycle
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create or update a policy for.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('BucketName', value)
    def set_CustomLifecycleConfiguration(self, value):
        """
        Set the value of the CustomLifecycleConfiguration input for this Choreo. ((optional, xml) Write a custom LifecycleConfiguration xml request for advanced customization. Note - this will overwrite all other inputs other than the AWS AccessKeyId, SecretKeyId, and BucketName.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('CustomLifecycleConfiguration', value)
    def set_DateOfExpiration(self, value):
        """
        Set the value of the DateOfExpiration input for this Choreo. ((optional, date) Date when the rule takes effect. You can specify either DateOfExpiration OR NumberOfDays. The date value must be in ISO 8601 format, time is always midnight UTC. Ex: 2013-04-24T00:00:00.000Z.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('DateOfExpiration', value)
    def set_LifecycleId(self, value):
        """
        Set the value of the LifecycleId input for this Choreo. ((optional, string) A unique ID for this lifecycle (i.e. delete-logs-in-30-days-rule).)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('LifecycleId', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((conditional, integer) The number of days to wait until the lifecycle expiration kicks in. Required unless you specify DateOfExpiration or a CustomLifecycleConfiguration instead.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('NumberOfDays', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((optional, string) Indicating that objects with this prefix will expire and be removed after the number of days specified. If not specified this lifecycle will apply to all objects in the bucket.)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('Prefix', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) The lifecycle status. Accepted values are: "Enabled" or "Disabled". Defaults to "Enabled".)
        """
        super(PutBucketLifecycleInputSet, self)._set_input('Status', value)

class PutBucketLifecycleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketLifecycle Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful lifecycle creation, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketLifecycleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketLifecycleResultSet(response, path)
