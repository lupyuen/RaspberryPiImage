# -*- coding: utf-8 -*-

###############################################################################
#
# RunCommand
# Executes a SQL command for a MySQL database.
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

class RunCommand(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunCommand Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RunCommand, self).__init__(temboo_session, '/Library/MySQL/RunCommand')


    def new_input_set(self):
        return RunCommandInputSet()

    def _make_result_set(self, result, path):
        return RunCommandResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunCommandChoreographyExecution(session, exec_id, path)

class RunCommandInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunCommand
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database to connect to.)
        """
        super(RunCommandInputSet, self)._set_input('DatabaseName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for the database user.)
        """
        super(RunCommandInputSet, self)._set_input('Password', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The database port. Defaults to 3306.)
        """
        super(RunCommandInputSet, self)._set_input('Port', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The preferred format for the database results. Accepted formats are json (the default) and xml. This input only applies when providing a SELECT, SHOW, or DESCRIBE statement for the SQL input.)
        """
        super(RunCommandInputSet, self)._set_input('ResponseFormat', value)
    def set_SQL(self, value):
        """
        Set the value of the SQL input for this Choreo. ((required, multiline) A SQL statement to execute.)
        """
        super(RunCommandInputSet, self)._set_input('SQL', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The name or IP address of the database server.)
        """
        super(RunCommandInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The database username.)
        """
        super(RunCommandInputSet, self)._set_input('Username', value)

class RunCommandResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunCommand Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResultData(self):
        """
        Retrieve the value for the "ResultData" output from this Choreo execution. (The data returned from the database. This output will only contain a value when a SELECT, SHOW, or DESCRIBE statement is provided. Results are returned as JSON or XML depending on the ResponseFormat.)
        """
        return self._output.get('ResultData', None)
    def get_Success(self):
        """
        Retrieve the value for the "Success" output from this Choreo execution. ((boolean) Indicates the result of the database command. The value will be "true" when the SQL statement executes successfully.)
        """
        return self._output.get('Success', None)

class RunCommandChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RunCommandResultSet(response, path)
