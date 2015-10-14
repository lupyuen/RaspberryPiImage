# -*- coding: utf-8 -*-

###############################################################################
#
# CreateObject
# Creates a new object on Parse.
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

class CreateObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateObject, self).__init__(temboo_session, '/Library/Parse/Objects/CreateObject')


    def new_input_set(self):
        return CreateObjectInputSet()

    def _make_result_set(self, result, path):
        return CreateObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateObjectChoreographyExecution(session, exec_id, path)

class CreateObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectContents(self, value):
        """
        Set the value of the ObjectContents input for this Choreo. ((required, json) A JSON string containing the object contents.)
        """
        super(CreateObjectInputSet, self)._set_input('ObjectContents', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(CreateObjectInputSet, self)._set_input('ApplicationID', value)
    def set_ClassName(self, value):
        """
        Set the value of the ClassName input for this Choreo. ((required, string) The class name for the object being created.)
        """
        super(CreateObjectInputSet, self)._set_input('ClassName', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(CreateObjectInputSet, self)._set_input('RESTAPIKey', value)

class CreateObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class CreateObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateObjectResultSet(response, path)
