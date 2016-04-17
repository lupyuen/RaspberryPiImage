# -*- coding: utf-8 -*-

###############################################################################
#
# GetSecondDegreeRelationships
# Retrieves a list of all the Entities (people or organizations) that are two-degrees removed by Relationships from the given Entity.
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

class GetSecondDegreeRelationships(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSecondDegreeRelationships Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSecondDegreeRelationships, self).__init__(temboo_session, '/Library/LittleSis/Entity/GetSecondDegreeRelationships')


    def new_input_set(self):
        return GetSecondDegreeRelationshipsInputSet()

    def _make_result_set(self, result, path):
        return GetSecondDegreeRelationshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSecondDegreeRelationshipsChoreographyExecution(session, exec_id, path)

class GetSecondDegreeRelationshipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSecondDegreeRelationships
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('APIKey', value)
    def set_Category1(self, value):
        """
        Set the value of the Category1 input for this Choreo. ((optional, string) Comma delimited list of Category IDs. Restricts the categories of Relationships that the given Entity and all first degree Entities returned should be connected through.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Category1', value)
    def set_Category2(self, value):
        """
        Set the value of the Category2 input for this Choreo. ((optional, string) Comma delimited list of Category IDs. Restricts the categories of Relationships that the given Entity and all second degree Entities returned should be connected through.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Category2', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, integer) The ID of the person or organization for which records are to be returned.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('EntityID', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120. Defaults to 20.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Number', value)
    def set_Order1(self, value):
        """
        Set the value of the Order1 input for this Choreo. ((optional, integer) Specifies the order of the Entities returned in the first degree Relationship. Acceptable values: 1 or 2. See documentation for more on Relationship order.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Order1', value)
    def set_Order2(self, value):
        """
        Set the value of the Order2 input for this Choreo. ((optional, integer) Specifies the order of the first degree Entity in the second degree Relationship. Acceptable values: 1 or 2. See documentation for more on Relationship order.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Order2', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specifies what page of results to show. Used in conjunction with Number parameter. A number of 20 and a Page of 6 will show results 100-120.)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetSecondDegreeRelationshipsInputSet, self)._set_input('ResponseFormat', value)

class GetSecondDegreeRelationshipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSecondDegreeRelationships Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetSecondDegreeRelationshipsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSecondDegreeRelationshipsResultSet(response, path)
