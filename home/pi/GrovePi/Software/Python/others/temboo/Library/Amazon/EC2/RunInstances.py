# -*- coding: utf-8 -*-

###############################################################################
#
# RunInstances
# Launches the specified number of instances of an AMI for which you have permissions.
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

class RunInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RunInstances, self).__init__(temboo_session, '/Library/Amazon/EC2/RunInstances')


    def new_input_set(self):
        return RunInstancesInputSet()

    def _make_result_set(self, result, path):
        return RunInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunInstancesChoreographyExecution(session, exec_id, path)

class RunInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(RunInstancesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(RunInstancesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DeleteOnTermination(self, value):
        """
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Sets whether the volume is deleted on instance termination. Defaults to "true". This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('DeleteOnTermination', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((optional, string) The device name exposed to the instance (i.e. /dev/sdh or xvdh). This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('DeviceName', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((required, string) The ID of the AMI.)
        """
        super(RunInstancesInputSet, self)._set_input('ImageId', value)
    def set_InstanceType(self, value):
        """
        Set the value of the InstanceType input for this Choreo. ((optional, string) The instance type (i.e. t1.micro, m1.small, m1.medium, m1.large, m1.xlarge). Default is m1.small.)
        """
        super(RunInstancesInputSet, self)._set_input('InstanceType', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((optional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('Iops', value)
    def set_KernelId(self, value):
        """
        Set the value of the KernelId input for this Choreo. ((optional, string) The ID of the kernel with which to launch the instance.)
        """
        super(RunInstancesInputSet, self)._set_input('KernelId', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((optional, string) The name of the key pair to use.)
        """
        super(RunInstancesInputSet, self)._set_input('KeyName', value)
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((required, integer) The maximum number of instances to launch. If the value is more than Amazon EC2 can launch, the largest possible number above MinCount will be launched instead.)
        """
        super(RunInstancesInputSet, self)._set_input('MaxCount', value)
    def set_MinCount(self, value):
        """
        Set the value of the MinCount input for this Choreo. ((required, integer) The minimum number of instances to launch. If the value is more than Amazon EC2 can launch, no instances are launched at all.)
        """
        super(RunInstancesInputSet, self)._set_input('MinCount', value)
    def set_MonitoringEnabled(self, value):
        """
        Set the value of the MonitoringEnabled input for this Choreo. ((optional, boolean) Enables monitoring for the instance. Defaults to false.)
        """
        super(RunInstancesInputSet, self)._set_input('MonitoringEnabled', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Suppresses a device mapping. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('NoDevice', value)
    def set_PlacementAvailabilityZone(self, value):
        """
        Set the value of the PlacementAvailabilityZone input for this Choreo. ((optional, string) The Availability Zone to launch the instance into.)
        """
        super(RunInstancesInputSet, self)._set_input('PlacementAvailabilityZone', value)
    def set_PlacementGroupName(self, value):
        """
        Set the value of the PlacementGroupName input for this Choreo. ((optional, string) The name of an existing placement group you want to launch the instance into (for cluster instances).)
        """
        super(RunInstancesInputSet, self)._set_input('PlacementGroupName', value)
    def set_PlacementTenancy(self, value):
        """
        Set the value of the PlacementTenancy input for this Choreo. ((optional, string) The tenancy of the instance. When set to "dedicated", the instance will run on single-tenant hardware and can only be launched into a VPC.)
        """
        super(RunInstancesInputSet, self)._set_input('PlacementTenancy', value)
    def set_RamdiskId(self, value):
        """
        Set the value of the RamdiskId input for this Choreo. ((optional, string) The ID of the RAM disk.)
        """
        super(RunInstancesInputSet, self)._set_input('RamdiskId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(RunInstancesInputSet, self)._set_input('ResponseFormat', value)
    def set_SecurityGroupId(self, value):
        """
        Set the value of the SecurityGroupId input for this Choreo. ((optional, string) One or more security group IDs. This can be a comma-separated list of up to 10 security group ids.)
        """
        super(RunInstancesInputSet, self)._set_input('SecurityGroupId', value)
    def set_SecurityGroup(self, value):
        """
        Set the value of the SecurityGroup input for this Choreo. ((optional, string) One or more security group names. This can be a comma-separated list of up to 10 security group names.)
        """
        super(RunInstancesInputSet, self)._set_input('SecurityGroup', value)
    def set_ShutdownBehavior(self, value):
        """
        Set the value of the ShutdownBehavior input for this Choreo. ((optional, string) Whether the instance stops or terminates on instance-initiated shutdown. Valid values are: stop and terminate.)
        """
        super(RunInstancesInputSet, self)._set_input('ShutdownBehavior', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((optional, string) The ID of the snapshot. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('SnapshotId', value)
    def set_SubnetId(self, value):
        """
        Set the value of the SubnetId input for this Choreo. ((optional, string) The ID of the subnet to launch the instance into (i.e. subnet-dea63cb7).)
        """
        super(RunInstancesInputSet, self)._set_input('SubnetId', value)
    def set_UserData(self, value):
        """
        Set the value of the UserData input for this Choreo. ((optional, string) The Base64-encoded MIME user data to be made available to the instance(s).)
        """
        super(RunInstancesInputSet, self)._set_input('UserData', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(RunInstancesInputSet, self)._set_input('UserRegion', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The name of the virtual device. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((optional, string) The size of the volume, in GiBs. Required unless you're creating the volume from a snapshot which indicates that the size will be the size of the snapshot. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard (the default) and io1. This is a Block Device Mapping parameter.)
        """
        super(RunInstancesInputSet, self)._set_input('VolumeType', value)

class RunInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class RunInstancesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RunInstancesResultSet(response, path)
