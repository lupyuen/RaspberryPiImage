# -*- coding: utf-8 -*-

###############################################################################
#
# RestoreDBInstanceFromDBSnapshot
# Creates a new DB Instance from a DB snapshot.
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

class RestoreDBInstanceFromDBSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RestoreDBInstanceFromDBSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RestoreDBInstanceFromDBSnapshot, self).__init__(temboo_session, '/Library/Amazon/RDS/RestoreDBInstanceFromDBSnapshot')


    def new_input_set(self):
        return RestoreDBInstanceFromDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return RestoreDBInstanceFromDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestoreDBInstanceFromDBSnapshotChoreographyExecution(session, exec_id, path)

class RestoreDBInstanceFromDBSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RestoreDBInstanceFromDBSnapshot
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AutoMinorVersionUpgrade(self, value):
        """
        Set the value of the AutoMinorVersionUpgrade input for this Choreo. ((optional, boolean) Indicates that minor version upgrades will be applied automatically to the DB Instance during the maintenance window. Defaults to 0 (false).)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('AutoMinorVersionUpgrade', value)
    def set_AvailabilityZone(self, value):
        """
        Set the value of the AvailabilityZone input for this Choreo. ((optional, string) The EC2 Availability Zone that the database instance will be created in. A random one is chose if not provided. Can not be specified if the MultiAZ parameter is set to 1 (true).)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('AvailabilityZone', value)
    def set_DBInstanceClass(self, value):
        """
        Set the value of the DBInstanceClass input for this Choreo. ((optional, string) The compute and memory capacity of the Amazon RDS DB instance. Valid Values: db.m1.small | db.m1.large | db.m1.xlarge | db.m2.2xlarge | db.m2.4xlarge.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('DBInstanceClass', value)
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((required, string) The identifier for the new DB instance that will be created from the specified Snapshot.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('DBInstanceIdentifier', value)
    def set_DBName(self, value):
        """
        Set the value of the DBName input for this Choreo. ((optional, string) The database name for the restored DB Instance. Note that this parameter doesn't apply to the MySQL engine.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('DBName', value)
    def set_DBSnapshotIdentifier(self, value):
        """
        Set the value of the DBSnapshotIdentifier input for this Choreo. ((required, string) The name of the DB Snapshot to use.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('DBSnapshotIdentifier', value)
    def set_Engine(self, value):
        """
        Set the value of the Engine input for this Choreo. ((optional, string) The database engine to use for the new instance. Valid Values: MySQL | oracle-se1 | oracle-se | oracle-ee.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('Engine', value)
    def set_LicenseModel(self, value):
        """
        Set the value of the LicenseModel input for this Choreo. ((optional, string) License model information for the restored DB Instance. Valid values: license-included | bring-your-own-license | general-public-license.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('LicenseModel', value)
    def set_MultiAZ(self, value):
        """
        Set the value of the MultiAZ input for this Choreo. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment. Do not specify the AvailabilityZone parameter if the MultiAZ parameter is set to 1 (true).)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('MultiAZ', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The port number on which the database accepts connections.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('Port', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(RestoreDBInstanceFromDBSnapshotInputSet, self)._set_input('UserRegion', value)

class RestoreDBInstanceFromDBSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RestoreDBInstanceFromDBSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class RestoreDBInstanceFromDBSnapshotChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RestoreDBInstanceFromDBSnapshotResultSet(response, path)
