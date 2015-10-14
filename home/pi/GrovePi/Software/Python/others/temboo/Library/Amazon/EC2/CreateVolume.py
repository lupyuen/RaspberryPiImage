# -*- coding: utf-8 -*-

###############################################################################
#
# CreateVolume
# Creates a new EBS volume that your EC2 instance can attach to.
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

class CreateVolume(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateVolume Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateVolume, self).__init__(temboo_session, '/Library/Amazon/EC2/CreateVolume')


    def new_input_set(self):
        return CreateVolumeInputSet()

    def _make_result_set(self, result, path):
        return CreateVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateVolumeChoreographyExecution(session, exec_id, path)

class CreateVolumeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateVolume
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateVolumeInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateVolumeInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AvailabilityZone(self, value):
        """
        Set the value of the AvailabilityZone input for this Choreo. ((required, string) The Availability Zone to use when creating thew new volume (i.e us-east-1a).)
        """
        super(CreateVolumeInputSet, self)._set_input('AvailabilityZone', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((optional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000. Required when the volume type is io1.)
        """
        super(CreateVolumeInputSet, self)._set_input('Iops', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateVolumeInputSet, self)._set_input('ResponseFormat', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((conditional, integer) The size for the volume (in gigabytes) that you are creating. Valid Values are 1-1024. Required if you're not creating a volume from a snapshot. If the volume type is io1, the min size is 10 GiB.)
        """
        super(CreateVolumeInputSet, self)._set_input('Size', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) The snapshot from which to create the new volume. Required if you are creating a volume from a snapshot.)
        """
        super(CreateVolumeInputSet, self)._set_input('SnapshotId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(CreateVolumeInputSet, self)._set_input('UserRegion', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type.Valid values are: "standard" (the default) and "io1".)
        """
        super(CreateVolumeInputSet, self)._set_input('VolumeType', value)

class CreateVolumeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateVolume Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateVolumeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateVolumeResultSet(response, path)
