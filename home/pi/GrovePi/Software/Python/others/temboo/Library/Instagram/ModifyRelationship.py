# -*- coding: utf-8 -*-

###############################################################################
#
# ModifyRelationship
# Modifies the relationship between the authenticating user and the target user.
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

class ModifyRelationship(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ModifyRelationship Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ModifyRelationship, self).__init__(temboo_session, '/Library/Instagram/ModifyRelationship')


    def new_input_set(self):
        return ModifyRelationshipInputSet()

    def _make_result_set(self, result, path):
        return ModifyRelationshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ModifyRelationshipChoreographyExecution(session, exec_id, path)

class ModifyRelationshipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ModifyRelationship
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        super(ModifyRelationshipInputSet, self)._set_input('AccessToken', value)
    def set_Action(self, value):
        """
        Set the value of the Action input for this Choreo. ((required, string) The type of relationship modification to perform. Valid values are: follow, unfollow, block, unblock, approve, or deny.)
        """
        super(ModifyRelationshipInputSet, self)._set_input('Action', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the target user.)
        """
        super(ModifyRelationshipInputSet, self)._set_input('UserID', value)

class ModifyRelationshipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ModifyRelationship Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class ModifyRelationshipChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ModifyRelationshipResultSet(response, path)
