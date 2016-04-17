# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntity
# Retrieves the LittleSis record for a given Entity (person or organization) by its ID.
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

class GetEntity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEntity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetEntity, self).__init__(temboo_session, '/Library/LittleSis/Entity/GetEntity')


    def new_input_set(self):
        return GetEntityInputSet()

    def _make_result_set(self, result, path):
        return GetEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntityChoreographyExecution(session, exec_id, path)

class GetEntityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEntity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetEntityInputSet, self)._set_input('APIKey', value)
    def set_Details(self, value):
        """
        Set the value of the Details input for this Choreo. ((optional, string) Indicate "details" to retrieve detailed information associated with this record, including aliases. Otherwise, only a basic record will be returned.)
        """
        super(GetEntityInputSet, self)._set_input('Details', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, integer) The EntityID of the person or organization record to be returned.)
        """
        super(GetEntityInputSet, self)._set_input('EntityID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetEntityInputSet, self)._set_input('ResponseFormat', value)

class GetEntityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEntity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetEntityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetEntityResultSet(response, path)
