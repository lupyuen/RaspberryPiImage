# -*- coding: utf-8 -*-

###############################################################################
#
# EntityTypes
# Retrieves a list of the types of Entities (people or organizations) in LittleSis, along with TypeIDs.
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

class EntityTypes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EntityTypes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EntityTypes, self).__init__(temboo_session, '/Library/LittleSis/Entity/EntityTypes')


    def new_input_set(self):
        return EntityTypesInputSet()

    def _make_result_set(self, result, path):
        return EntityTypesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntityTypesChoreographyExecution(session, exec_id, path)

class EntityTypesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EntityTypes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from LittleSis.org. Acceptable inputs: xml or json. Defautls to xml.)
        """
        super(EntityTypesInputSet, self)._set_input('ResponseFormat', value)

class EntityTypesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EntityTypes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class EntityTypesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EntityTypesResultSet(response, path)
