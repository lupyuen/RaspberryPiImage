# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Retrieves multiple installations at once and allows you to narrow results by specifying query constraints.
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
        super(Query, self).__init__(temboo_session, '/Library/Parse/PushNotifications/Query')


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
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(QueryInputSet, self)._set_input('ApplicationID', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, boolean) A flag indicating to include a count of objects in the response. Set to 1 to include a count. Defaults to 0.)
        """
        super(QueryInputSet, self)._set_input('Count', value)
    def set_Include(self, value):
        """
        Set the value of the Include input for this Choreo. ((optional, string) Specify a field to return multiple types of related objects in this query.  For example, enter: post.author, to retrieve posts and their authors related to this class.)
        """
        super(QueryInputSet, self)._set_input('Include', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of objects to return.)
        """
        super(QueryInputSet, self)._set_input('Limit', value)
    def set_MasterKey(self, value):
        """
        Set the value of the MasterKey input for this Choreo. ((required, string) The Master Key provided by Parse.)
        """
        super(QueryInputSet, self)._set_input('MasterKey', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Returns only records after this number. Used in combination with the Limit input to page through many results.)
        """
        super(QueryInputSet, self)._set_input('Skip', value)
    def set_Where(self, value):
        """
        Set the value of the Where input for this Choreo. ((optional, json) A valid query constraint formatted as a JSON-encoded string. See documentation for syntax rules.)
        """
        super(QueryInputSet, self)._set_input('Where', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
