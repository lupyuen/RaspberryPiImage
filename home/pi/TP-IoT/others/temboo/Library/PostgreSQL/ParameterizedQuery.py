# -*- coding: utf-8 -*-

###############################################################################
#
# ParameterizedQuery
# Allows you to run a parameterized query.
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

class ParameterizedQuery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ParameterizedQuery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ParameterizedQuery, self).__init__(temboo_session, '/Library/PostgreSQL/ParameterizedQuery')


    def new_input_set(self):
        return ParameterizedQueryInputSet()

    def _make_result_set(self, result, path):
        return ParameterizedQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ParameterizedQueryChoreographyExecution(session, exec_id, path)

class ParameterizedQueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ParameterizedQuery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database to connect to.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('DatabaseName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The password for the database user.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Password', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The database port. Defaults to 5432.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Port', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The preferred format for the database results. Accepted formats are json (the default) and xml. This input only applies when providing a SELECT statement for the SQL input.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('ResponseFormat', value)
    def set_SQL(self, value):
        """
        Set the value of the SQL input for this Choreo. ((required, string) A SQL statement that includes placholders (e.g., select * from users where id = ?). Items in the Values input will be sanitized and substituted in for placeholders.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('SQL', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The name or IP address of the database server.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The database username.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Username', value)
    def set_Values(self, value):
        """
        Set the value of the Values input for this Choreo. ((required, json) The values to be sanitized and passed into the parameterized SQL statement.)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Values', value)
    def set_Version(self, value):
        """
        Set the value of the Version input for this Choreo. ((optional, integer) The version of the Postgres database. Allowed values are 8 and 9 (the default).)
        """
        super(ParameterizedQueryInputSet, self)._set_input('Version', value)

class ParameterizedQueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ParameterizedQuery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResultData(self):
        """
        Retrieve the value for the "ResultData" output from this Choreo execution. (The data returned from the database. This output will only contain a value when a SELECT statement is provided. Results are returned as JSON or XML depending on the ResponseFormat.)
        """
        return self._output.get('ResultData', None)
    def get_Success(self):
        """
        Retrieve the value for the "Success" output from this Choreo execution. ((boolean) Indicates the result of the database command. The value will be "true" when the SQL statement executes successfully.)
        """
        return self._output.get('Success', None)

class ParameterizedQueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ParameterizedQueryResultSet(response, path)
