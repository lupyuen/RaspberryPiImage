# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRole
# Updates an existing role.
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

class UpdateRole(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRole Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateRole, self).__init__(temboo_session, '/Library/Parse/Roles/UpdateRole')


    def new_input_set(self):
        return UpdateRoleInputSet()

    def _make_result_set(self, result, path):
        return UpdateRoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRoleChoreographyExecution(session, exec_id, path)

class UpdateRoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRole
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((required, json) A JSON string containing the role information to be updated. See documentation for formatting details.)
        """
        super(UpdateRoleInputSet, self)._set_input('Role', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(UpdateRoleInputSet, self)._set_input('ApplicationID', value)
    def set_MasterKey(self, value):
        """
        Set the value of the MasterKey input for this Choreo. ((required, string) The Master Key provided by Parse.)
        """
        super(UpdateRoleInputSet, self)._set_input('MasterKey', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the role to update.)
        """
        super(UpdateRoleInputSet, self)._set_input('ObjectID', value)

class UpdateRoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRole Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateRoleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateRoleResultSet(response, path)
