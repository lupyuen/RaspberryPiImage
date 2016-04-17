# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteRole
# Retrieves a given role.
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

class DeleteRole(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteRole Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteRole, self).__init__(temboo_session, '/Library/Parse/Roles/DeleteRole')


    def new_input_set(self):
        return DeleteRoleInputSet()

    def _make_result_set(self, result, path):
        return DeleteRoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteRoleChoreographyExecution(session, exec_id, path)

class DeleteRoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteRole
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the role to delete.)
        """
        super(DeleteRoleInputSet, self)._set_input('ObjectID', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(DeleteRoleInputSet, self)._set_input('ApplicationID', value)
    def set_MasterKey(self, value):
        """
        Set the value of the MasterKey input for this Choreo. ((required, string) The Master Key provided by Parse.)
        """
        super(DeleteRoleInputSet, self)._set_input('MasterKey', value)

class DeleteRoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteRole Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class DeleteRoleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteRoleResultSet(response, path)
