# -*- coding: utf-8 -*-

###############################################################################
#
# RegisterImage
# Registers a new AMI with Amazon EC2.
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

class RegisterImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegisterImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RegisterImage, self).__init__(temboo_session, '/Library/Amazon/EC2/RegisterImage')


    def new_input_set(self):
        return RegisterImageInputSet()

    def _make_result_set(self, result, path):
        return RegisterImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegisterImageChoreographyExecution(session, exec_id, path)

class RegisterImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegisterImage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(RegisterImageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(RegisterImageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Architecture(self, value):
        """
        Set the value of the Architecture input for this Choreo. ((optional, string) The architecture of the image. Valid values are: i386 or x86_64. Defaults to i386.)
        """
        super(RegisterImageInputSet, self)._set_input('Architecture', value)
    def set_DeleteOnTermination(self, value):
        """
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Whether the Amazon EBS volume is deleted on instance termination. Defaults to true.)
        """
        super(RegisterImageInputSet, self)._set_input('DeleteOnTermination', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the AMI.)
        """
        super(RegisterImageInputSet, self)._set_input('Description', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, specify this input with the root device name (e.g., /dev/sda1, or xvda), and SnapshotId.)
        """
        super(RegisterImageInputSet, self)._set_input('DeviceName', value)
    def set_ImageLocation(self, value):
        """
        Set the value of the ImageLocation input for this Choreo. ((conditional, string) Full path to your AMI manifest in Amazon S3 storage. Required if registering an Amazon-S3 backed AMI.)
        """
        super(RegisterImageInputSet, self)._set_input('ImageLocation', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((conditional, integer) The number of I/O operations per second (IOPS) that the volume supports. A valid range is: 100 to 2000.)
        """
        super(RegisterImageInputSet, self)._set_input('Iops', value)
    def set_KernelId(self, value):
        """
        Set the value of the KernelId input for this Choreo. ((optional, string) The ID of the kernel to select.)
        """
        super(RegisterImageInputSet, self)._set_input('KernelId', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) A name for your AMI.)
        """
        super(RegisterImageInputSet, self)._set_input('Name', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Specifies that no device should be mapped. Defaults to 1 (true).)
        """
        super(RegisterImageInputSet, self)._set_input('NoDevice', value)
    def set_RamdiskId(self, value):
        """
        Set the value of the RamdiskId input for this Choreo. ((optional, string) The ID of the RAM disk to select.)
        """
        super(RegisterImageInputSet, self)._set_input('RamdiskId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(RegisterImageInputSet, self)._set_input('ResponseFormat', value)
    def set_RootDeviceName(self, value):
        """
        Set the value of the RootDeviceName input for this Choreo. ((conditional, string) The root device name (e.g., /dev/sda1, or xvda). Required if registering an Amazon EBS-backed AMI.)
        """
        super(RegisterImageInputSet, self)._set_input('RootDeviceName', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, you must at least specify this input with the snapshot ID, and DeviceName with the root device name.)
        """
        super(RegisterImageInputSet, self)._set_input('SnapshotId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(RegisterImageInputSet, self)._set_input('UserRegion', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The virtual device name.)
        """
        super(RegisterImageInputSet, self)._set_input('VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((conditional, integer) The size of the volume, in GiBs. Required if you are not creating a volume from a snapshot.)
        """
        super(RegisterImageInputSet, self)._set_input('VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard and io.)
        """
        super(RegisterImageInputSet, self)._set_input('VolumeType', value)

class RegisterImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegisterImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class RegisterImageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RegisterImageResultSet(response, path)
