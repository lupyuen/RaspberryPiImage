# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketLogging
# Sets the logging parameters for a bucket and specifies permissions for who can view and modify the logging parameters. Can also be used to disable logging.
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

class PutBucketLogging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketLogging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketLogging, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketLogging')


    def new_input_set(self):
        return PutBucketLoggingInputSet()

    def _make_result_set(self, result, path):
        return PutBucketLoggingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketLoggingChoreographyExecution(session, exec_id, path)

class PutBucketLoggingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketLogging
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BucketLoggingStatus(self, value):
        """
        Set the value of the BucketLoggingStatus input for this Choreo. ((optional, xml) An XML file that allows custom config, this can be used as an alternative to the other bucket logging inputs. If provided, the Choreo will ignore all inputs except your AWS Key/Secret and BucketName.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('BucketLoggingStatus', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that you are setting the logging for.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('BucketName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((conditional, string) The email address of the person being granted logging permissions.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('EmailAddress', value)
    def set_Permission(self, value):
        """
        Set the value of the Permission input for this Choreo. ((conditional, string) The logging permissions given to the Grantee for the bucket. Valid values are: FULL_CONTROL, READ, or WRITE.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('Permission', value)
    def set_TargetBucket(self, value):
        """
        Set the value of the TargetBucket input for this Choreo. ((conditional, string) The name of the target bucket. To disable logging, just leave this blank.)
        """
        super(PutBucketLoggingInputSet, self)._set_input('TargetBucket', value)
    def set_TargetPrefix(self, value):
        """
        Set the value of the TargetPrefix input for this Choreo. ((conditional, string) Lets you specify a prefix for the keys that the log files will be stored under. Defaults to "/logs")
        """
        super(PutBucketLoggingInputSet, self)._set_input('TargetPrefix', value)

class PutBucketLoggingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketLogging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. A successful execution returns an empty 200 response.)
        """
        return self._output.get('Response', None)

class PutBucketLoggingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketLoggingResultSet(response, path)
