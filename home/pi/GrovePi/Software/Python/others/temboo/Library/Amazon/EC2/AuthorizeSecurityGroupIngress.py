# -*- coding: utf-8 -*-

###############################################################################
#
# AuthorizeSecurityGroupIngress
# Adds an ingress rule to a security group.
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

class AuthorizeSecurityGroupIngress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AuthorizeSecurityGroupIngress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AuthorizeSecurityGroupIngress, self).__init__(temboo_session, '/Library/Amazon/EC2/AuthorizeSecurityGroupIngress')


    def new_input_set(self):
        return AuthorizeSecurityGroupIngressInputSet()

    def _make_result_set(self, result, path):
        return AuthorizeSecurityGroupIngressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AuthorizeSecurityGroupIngressChoreographyExecution(session, exec_id, path)

class AuthorizeSecurityGroupIngressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AuthorizeSecurityGroupIngress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_GroupId(self, value):
        """
        Set the value of the GroupId input for this Choreo. ((conditional, string) The ID of the security group to modify. Can be used instead of GroupName.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('GroupId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((conditional, string) The name of the security group to modify. Can be used instead of GroupId.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('GroupName', value)
    def set_IpPermissionsCidrIp(self, value):
        """
        Set the value of the IpPermissionsCidrIp input for this Choreo. ((optional, string) The CIDR range. Cannot be used when specifying a source security group.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsCidrIp', value)
    def set_IpPermissionsFromPort(self, value):
        """
        Set the value of the IpPermissionsFromPort input for this Choreo. ((optional, integer) The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, you can use -1 to specify all ICMP types.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsFromPort', value)
    def set_IpPermissionsGroupId(self, value):
        """
        Set the value of the IpPermissionsGroupId input for this Choreo. ((optional, string) The ID of the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsGroupId', value)
    def set_IpPermissionsGroupName(self, value):
        """
        Set the value of the IpPermissionsGroupName input for this Choreo. ((optional, string) The name of the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsGroupName', value)
    def set_IpPermissionsIpProtocol(self, value):
        """
        Set the value of the IpPermissionsIpProtocol input for this Choreo. ((required, string) The IP protocol name or number. Valid values for EC2-Classic: tcp, udp, icmp (or 6, 17, 1). Valid values for EC2-VPC: tcp, udp, icmp, any valid protocol number (0-254), or -1 (to specify all).)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsIpProtocol', value)
    def set_IpPermissionsToPort(self, value):
        """
        Set the value of the IpPermissionsToPort input for this Choreo. ((optional, integer) The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, you can use -1 to specify all ICMP codes for the given ICMP type.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsToPort', value)
    def set_IpPermissionsUserId(self, value):
        """
        Set the value of the IpPermissionsUserId input for this Choreo. ((optional, string) The AWS account ID that owns the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('IpPermissionsUserId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(AuthorizeSecurityGroupIngressInputSet, self)._set_input('UserRegion', value)

class AuthorizeSecurityGroupIngressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AuthorizeSecurityGroupIngress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AuthorizeSecurityGroupIngressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AuthorizeSecurityGroupIngressResultSet(response, path)
