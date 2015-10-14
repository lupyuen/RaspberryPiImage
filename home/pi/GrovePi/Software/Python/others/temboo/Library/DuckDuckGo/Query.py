# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Access DuckDuckGo web search functionality.  
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

class Query(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Query Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Query, self).__init__(temboo_session, '/Library/DuckDuckGo/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

class QueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Query
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) Enter: xml, or json.  Default is set to xml.)
        """
        super(QueryInputSet, self)._set_input('Format', value)
    def set_NoHTML(self, value):
        """
        Set the value of the NoHTML input for this Choreo. ((optional, integer) Enter 1 to remove HTML from text. Set only if Format=json.)
        """
        super(QueryInputSet, self)._set_input('NoHTML', value)
    def set_NoRedirect(self, value):
        """
        Set the value of the NoRedirect input for this Choreo. ((optional, integer) Enter 1 to skip HTTP redirects.  This is useful for !bang commands. Set only if Format=json.)
        """
        super(QueryInputSet, self)._set_input('NoRedirect', value)
    def set_PrettyPrint(self, value):
        """
        Set the value of the PrettyPrint input for this Choreo. ((optional, integer) Enter 1 to pretty-print the JSON output.)
        """
        super(QueryInputSet, self)._set_input('PrettyPrint', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Enter a search query.)
        """
        super(QueryInputSet, self)._set_input('Query', value)
    def set_SkipDisambiguation(self, value):
        """
        Set the value of the SkipDisambiguation input for this Choreo. ((optional, integer) Enter 1 to skip disambiguation. Set only if Format=json.)
        """
        super(QueryInputSet, self)._set_input('SkipDisambiguation', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DuckDuckGo in XML or JSON format.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
