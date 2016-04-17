# -*- coding: utf-8 -*-

###############################################################################
#
# Search
# Search public objects across the social graph.
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

class Search(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Search Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Search, self).__init__(temboo_session, '/Library/Facebook/Searching/Search')


    def new_input_set(self):
        return SearchInputSet()

    def _make_result_set(self, result, path):
        return SearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchChoreographyExecution(session, exec_id, path)

class SearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Search
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved from the final OAuth step.)
        """
        super(SearchInputSet, self)._set_input('AccessToken', value)
    def set_Center(self, value):
        """
        Set the value of the Center input for this Choreo. ((conditional, string) The coordinates for a place (such as 37.76,122.427). Used only when specifying an object type of "place".)
        """
        super(SearchInputSet, self)._set_input('Center', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, integer) The distance search parameter used only when specifying an object type of "place". Defaults to 1000.)
        """
        super(SearchInputSet, self)._set_input('Distance', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        super(SearchInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the response.)
        """
        super(SearchInputSet, self)._set_input('Limit', value)
    def set_ObjectType(self, value):
        """
        Set the value of the ObjectType input for this Choreo. ((required, string) The type of object to search for such as: user, page, event, group, or place.)
        """
        super(SearchInputSet, self)._set_input('ObjectType', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results. Returns results starting from the specified number.)
        """
        super(SearchInputSet, self)._set_input('Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) The Facebook query term to send in the request.)
        """
        super(SearchInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(SearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        super(SearchInputSet, self)._set_input('Since', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        super(SearchInputSet, self)._set_input('Until', value)

class SearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Search Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_HasNext(self):
        """
        Retrieve the value for the "HasNext" output from this Choreo execution. ((boolean) A boolean flag indicating that a next page exists.)
        """
        return self._output.get('HasNext', None)
    def get_HasPrevious(self):
        """
        Retrieve the value for the "HasPrevious" output from this Choreo execution. ((boolean) A boolean flag indicating that a previous page exists.)
        """
        return self._output.get('HasPrevious', None)

class SearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
