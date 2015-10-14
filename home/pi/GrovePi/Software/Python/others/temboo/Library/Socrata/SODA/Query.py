# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Performs queries against data on the Socrata Platform.
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
        super(Query, self).__init__(temboo_session, '/Library/Socrata/SODA/Query')


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
    def set_AppToken(self, value):
        """
        Set the value of the AppToken input for this Choreo. ((optional, string) The App Token provided by Socrata.)
        """
        super(QueryInputSet, self)._set_input('AppToken', value)
    def set_Domain(self, value):
        """
        Set the value of the Domain input for this Choreo. ((required, string) The domain used in the request (i.e. soda.demo.socrata.com).)
        """
        super(QueryInputSet, self)._set_input('Domain', value)
    def set_Group(self, value):
        """
        Set the value of the Group input for this Choreo. ((optional, string) Groups results based on the column name provided.)
        """
        super(QueryInputSet, self)._set_input('Group', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, string) The maximum number of results to return. Used in combination with the Offset input for pagination. Defaults to 100.)
        """
        super(QueryInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, string) Indicates the starting point of the result set. Used in combination with the Limit input for pagination. Defaults to 0.)
        """
        super(QueryInputSet, self)._set_input('Offset', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Determines how results will be sorted. This input can take a column name, and can sort in either ascending or descending order (i.e. datetime asc).)
        """
        super(QueryInputSet, self)._set_input('Order', value)
    def set_Resource(self, value):
        """
        Set the value of the Resource input for this Choreo. ((required, string) The unique identifier for a dataset to retrieve (i.e 4tka-6guv or earthquakes).)
        """
        super(QueryInputSet, self)._set_input('Resource', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), xml, csv, and rdf.)
        """
        super(QueryInputSet, self)._set_input('ResponseFormat', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((optional, string) A search clause. This wll do a full text search for a value.)
        """
        super(QueryInputSet, self)._set_input('Search', value)
    def set_Select(self, value):
        """
        Set the value of the Select input for this Choreo. ((optional, string) Indicates which columns to return. If not specified, all columns will be returned.)
        """
        super(QueryInputSet, self)._set_input('Select', value)
    def set_Where(self, value):
        """
        Set the value of the Where input for this Choreo. ((optional, string) Filters the results using a WHERE clause.)
        """
        super(QueryInputSet, self)._set_input('Where', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Fields(self):
        """
        Retrieve the value for the "Fields" output from this Choreo execution. ((json) This lists the fields returned in this response in a JSON array.)
        """
        return self._output.get('Fields', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response form Socrata.)
        """
        return self._output.get('Response', None)
    def get_Types(self):
        """
        Retrieve the value for the "Types" output from this Choreo execution. ((json) This is a list of SODA2 types in a JSON array. These will match up in the same order as the fields in X-SODA2-Fields.)
        """
        return self._output.get('Types', None)
    def get_LastModified(self):
        """
        Retrieve the value for the "LastModified" output from this Choreo execution. ((date) Contains the date returned in the Last-Modified response header.)
        """
        return self._output.get('LastModified', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
