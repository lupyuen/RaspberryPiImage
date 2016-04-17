# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeDBInstances
# Returns information about privisioned database instances.
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

class DescribeDBInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeDBInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DescribeDBInstances, self).__init__(temboo_session, '/Library/Amazon/RDS/DescribeDBInstances')


    def new_input_set(self):
        return DescribeDBInstancesInputSet()

    def _make_result_set(self, result, path):
        return DescribeDBInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeDBInstancesChoreographyExecution(session, exec_id, path)

class DescribeDBInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeDBInstances
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((optional, string) The DB Instance identifier. Should be in all lowercase.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('DBInstanceIdentifier', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, integer) If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('Marker', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) The max number of results to return in the response. Defaults to 100. Minimum is 20.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('MaxRecords', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DescribeDBInstancesInputSet, self)._set_input('UserRegion', value)

class DescribeDBInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeDBInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeDBInstancesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DescribeDBInstancesResultSet(response, path)
