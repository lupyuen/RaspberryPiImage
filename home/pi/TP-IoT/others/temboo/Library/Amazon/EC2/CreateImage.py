# -*- coding: utf-8 -*-

###############################################################################
#
# CreateImage
# Creates an Amazon Machine Image from an Amazon EBS-backed instance. The image can be used later to launch other identical servers.
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

class CreateImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateImage, self).__init__(temboo_session, '/Library/Amazon/EC2/CreateImage')


    def new_input_set(self):
        return CreateImageInputSet()

    def _make_result_set(self, result, path):
        return CreateImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateImageChoreographyExecution(session, exec_id, path)

class CreateImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateImage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateImageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateImageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DeleteOnTermination(self, value):
        """
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Whether the volume is deleted on instance termination. Defaults to "true".)
        """
        super(CreateImageInputSet, self)._set_input('DeleteOnTermination', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the image you want to create.)
        """
        super(CreateImageInputSet, self)._set_input('Description', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((conditional, string) The device name exposed to the instance (i.e. /dev/sdh or xvdh). When registering an AMI from a snapshot, DiviceName is required as well as SnapshotId.)
        """
        super(CreateImageInputSet, self)._set_input('DeviceName', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The ID of the instance to create the image on.)
        """
        super(CreateImageInputSet, self)._set_input('InstanceId', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((conditional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000.)
        """
        super(CreateImageInputSet, self)._set_input('Iops', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name for the image you are creating.)
        """
        super(CreateImageInputSet, self)._set_input('Name', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Suppresses a device mapping. Defaults to "true".)
        """
        super(CreateImageInputSet, self)._set_input('NoDevice', value)
    def set_NoReboot(self, value):
        """
        Set the value of the NoReboot input for this Choreo. ((optional, boolean) Defaults to "false". Amazon EC2 will attempt to shut down the instance before and after creating the image. Set to "true" for NoReboot.)
        """
        super(CreateImageInputSet, self)._set_input('NoReboot', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CreateImageInputSet, self)._set_input('ResponseFormat', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) The ID of the snapshot. Required when registering from a snapshot. You must also specify DeviceName with the root device name.)
        """
        super(CreateImageInputSet, self)._set_input('SnapshotId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(CreateImageInputSet, self)._set_input('UserRegion', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The name of the virtual device.)
        """
        super(CreateImageInputSet, self)._set_input('VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((conditional, string) The size of the volume, in GiBs. Required unless you're creating the volume from a snapshot which indicates that the size will be the size of the snapshot.)
        """
        super(CreateImageInputSet, self)._set_input('VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard (the default) and io1.)
        """
        super(CreateImageInputSet, self)._set_input('VolumeType', value)

class CreateImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateImageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateImageResultSet(response, path)
