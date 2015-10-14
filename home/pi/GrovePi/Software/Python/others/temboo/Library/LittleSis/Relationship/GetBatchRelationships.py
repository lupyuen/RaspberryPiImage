# -*- coding: utf-8 -*-

###############################################################################
#
# GetBatchRelationships
# Retrieves information about a batch of relationships in LittleSis according to the relationship IDs provided.
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

class GetBatchRelationships(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBatchRelationships Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBatchRelationships, self).__init__(temboo_session, '/Library/LittleSis/Relationship/GetBatchRelationships')


    def new_input_set(self):
        return GetBatchRelationshipsInputSet()

    def _make_result_set(self, result, path):
        return GetBatchRelationshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBatchRelationshipsChoreographyExecution(session, exec_id, path)

class GetBatchRelationshipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBatchRelationships
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetBatchRelationshipsInputSet, self)._set_input('APIKey', value)
    def set_Details(self, value):
        """
        Set the value of the Details input for this Choreo. ((optional, integer) Indicate 1 to include details for each relationship record returned. Otherwise, only a basic record will be returned.)
        """
        super(GetBatchRelationshipsInputSet, self)._set_input('Details', value)
    def set_RelationshipIDs(self, value):
        """
        Set the value of the RelationshipIDs input for this Choreo. ((required, string) The IDs of the relationship records to be returned as a comma delimited string.)
        """
        super(GetBatchRelationshipsInputSet, self)._set_input('RelationshipIDs', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetBatchRelationshipsInputSet, self)._set_input('ResponseFormat', value)

class GetBatchRelationshipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBatchRelationships Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetBatchRelationshipsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBatchRelationshipsResultSet(response, path)
