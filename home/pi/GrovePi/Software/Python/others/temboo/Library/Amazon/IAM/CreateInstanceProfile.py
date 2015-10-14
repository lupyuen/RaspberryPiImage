# -*- coding: utf-8 -*-

###############################################################################
#
# CreateInstanceProfile
# Creates a new instance profile.
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

class CreateInstanceProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateInstanceProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateInstanceProfile, self).__init__(temboo_session, '/Library/Amazon/IAM/CreateInstanceProfile')


    def new_input_set(self):
        return CreateInstanceProfileInputSet()

    def _make_result_set(self, result, path):
        return CreateInstanceProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateInstanceProfileChoreographyExecution(session, exec_id, path)

class CreateInstanceProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateInstanceProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateInstanceProfileInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateInstanceProfileInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_InstanceProfileName(self, value):
        """
        Set the value of the InstanceProfileName input for this Choreo. ((required, string) Name of the instance profile to create.)
        """
        super(CreateInstanceProfileInputSet, self)._set_input('InstanceProfileName', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) The path for the user name. If it is not included, it defaults to a slash (/).)
        """
        super(CreateInstanceProfileInputSet, self)._set_input('Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateInstanceProfileInputSet, self)._set_input('ResponseFormat', value)

class CreateInstanceProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateInstanceProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateInstanceProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateInstanceProfileResultSet(response, path)
