# -*- coding: utf-8 -*-

###############################################################################
#
# GetReferences
# Retrieves references for the data included in any record obtained from LittleSis.
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

class GetReferences(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReferences Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReferences, self).__init__(temboo_session, '/Library/LittleSis/Reference/GetReferences')


    def new_input_set(self):
        return GetReferencesInputSet()

    def _make_result_set(self, result, path):
        return GetReferencesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReferencesChoreographyExecution(session, exec_id, path)

class GetReferencesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReferences
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetReferencesInputSet, self)._set_input('APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, decimal) The ID of the record for which you want references. This can be either an entity or a relationship ID.)
        """
        super(GetReferencesInputSet, self)._set_input('ID', value)
    def set_RecordType(self, value):
        """
        Set the value of the RecordType input for this Choreo. ((required, string) Specify type of record for which you want to obtain references: entity (for a person or an institution record) or relationship (for a relationship record).)
        """
        super(GetReferencesInputSet, self)._set_input('RecordType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetReferencesInputSet, self)._set_input('ResponseFormat', value)

class GetReferencesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReferences Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetReferencesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReferencesResultSet(response, path)
