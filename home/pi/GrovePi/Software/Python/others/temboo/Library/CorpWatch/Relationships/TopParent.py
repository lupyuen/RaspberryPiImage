# -*- coding: utf-8 -*-

###############################################################################
#
# TopParent
# For a given ID of the highest-level owning parent of a family of corporations, retrieves all of the companies that are "below" it in the hierarchy.
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

class TopParent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopParent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TopParent, self).__init__(temboo_session, '/Library/CorpWatch/Relationships/TopParent')


    def new_input_set(self):
        return TopParentInputSet()

    def _make_result_set(self, result, path):
        return TopParentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopParentChoreographyExecution(session, exec_id, path)

class TopParentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopParent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(TopParentInputSet, self)._set_input('APIKey', value)
    def set_CWID(self, value):
        """
        Set the value of the CWID input for this Choreo. ((required, string) The CWID of the highest-level owning parent of a family of corprorations (or Top Parent). Most company records contain a field for top_parent_id.)
        """
        super(TopParentInputSet, self)._set_input('CWID', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(TopParentInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(TopParentInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(TopParentInputSet, self)._set_input('ResponseType', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only subsidiaries for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        super(TopParentInputSet, self)._set_input('Year', value)

class TopParentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopParent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class TopParentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopParentResultSet(response, path)
