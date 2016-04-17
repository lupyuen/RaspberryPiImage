# -*- coding: utf-8 -*-

###############################################################################
#
# RevokeDBSecurityGroupIngress
# Revokes access from a DBSecurityGroup for previously authorized IP ranges or EC2 Security Groups.
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

class RevokeDBSecurityGroupIngress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RevokeDBSecurityGroupIngress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RevokeDBSecurityGroupIngress, self).__init__(temboo_session, '/Library/Amazon/RDS/RevokeDBSecurityGroupIngress')


    def new_input_set(self):
        return RevokeDBSecurityGroupIngressInputSet()

    def _make_result_set(self, result, path):
        return RevokeDBSecurityGroupIngressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RevokeDBSecurityGroupIngressChoreographyExecution(session, exec_id, path)

class RevokeDBSecurityGroupIngressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RevokeDBSecurityGroupIngress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_CIDRIP(self, value):
        """
        Set the value of the CIDRIP input for this Choreo. ((conditional, string) IP range that should be revoked. Required unless EC2SecurityGroupName and EC2SecurityGroupOwnerId are used.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('CIDRIP', value)
    def set_DBSecurityGroupName(self, value):
        """
        Set the value of the DBSecurityGroupName input for this Choreo. ((required, string) A unique name for the security group you want to revoke ingress from.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('DBSecurityGroupName', value)
    def set_EC2SecurityGroupName(self, value):
        """
        Set the value of the EC2SecurityGroupName input for this Choreo. ((conditional, string) The EC2 security group to revoke. This and EC2SecurityGroupOwnerId are required if CIDRIP is not used.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('EC2SecurityGroupName', value)
    def set_EC2SecurityGroupOwnerId(self, value):
        """
        Set the value of the EC2SecurityGroupOwnerId input for this Choreo. ((conditional, string) The account number for the security group owner to revoke. This and EC2SecurityGroupName are required if CIDRIP is not used.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('EC2SecurityGroupOwnerId', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(RevokeDBSecurityGroupIngressInputSet, self)._set_input('UserRegion', value)

class RevokeDBSecurityGroupIngressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RevokeDBSecurityGroupIngress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class RevokeDBSecurityGroupIngressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RevokeDBSecurityGroupIngressResultSet(response, path)
