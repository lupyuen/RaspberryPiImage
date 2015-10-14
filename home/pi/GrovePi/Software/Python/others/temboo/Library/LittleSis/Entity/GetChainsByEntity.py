# -*- coding: utf-8 -*-

###############################################################################
#
# GetChainsByEntity
# Retrieves a chain of connections between two Entities (person or organization) in LittleSis.
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

class GetChainsByEntity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetChainsByEntity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetChainsByEntity, self).__init__(temboo_session, '/Library/LittleSis/Entity/GetChainsByEntity')


    def new_input_set(self):
        return GetChainsByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetChainsByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChainsByEntityChoreographyExecution(session, exec_id, path)

class GetChainsByEntityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetChainsByEntity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetChainsByEntityInputSet, self)._set_input('APIKey', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((optional, integer) Limit the relationships to specific categories by specifying the category number.)
        """
        super(GetChainsByEntityInputSet, self)._set_input('CategoryID', value)
    def set_EntityIDs(self, value):
        """
        Set the value of the EntityIDs input for this Choreo. ((required, integer) The EntityIDs of the two entities for which a relationship chain is to be returned, separated by a semicolon (e.g. 14629;2 ).)
        """
        super(GetChainsByEntityInputSet, self)._set_input('EntityIDs', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, string) Specifies which of the found chain to expand in detail. Default is 1.)
        """
        super(GetChainsByEntityInputSet, self)._set_input('Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetChainsByEntityInputSet, self)._set_input('ResponseFormat', value)

class GetChainsByEntityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetChainsByEntity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetChainsByEntityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetChainsByEntityResultSet(response, path)
