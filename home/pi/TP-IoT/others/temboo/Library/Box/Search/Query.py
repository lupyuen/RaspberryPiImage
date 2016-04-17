# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Searches a user's Box account for items that match a specified keyword.
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
        super(Query, self).__init__(temboo_session, '/Library/Box/Search/Query')


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
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(QueryInputSet, self)._set_input('AccessToken', value)
    def set_AncestorFolderIDs(self, value):
        """
        Set the value of the AncestorFolderIDs input for this Choreo. ((optional, string) A comma-seperated list of folder IDs which are used to filter your search.)
        """
        super(QueryInputSet, self)._set_input('AncestorFolderIDs', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(QueryInputSet, self)._set_input('AsUser', value)
    def set_ContentTypes(self, value):
        """
        Set the value of the ContentTypes input for this Choreo. ((optional, string) A comma-seperated list of content types used to filter your search.  Acceptable types are: name, description, file_content, comments, and tags.)
        """
        super(QueryInputSet, self)._set_input('ContentTypes', value)
    def set_CreatedAtRange(self, value):
        """
        Set the value of the CreatedAtRange input for this Choreo. ((optional, date) A comma-seperated date range in ISO-8601 (2012-11-02T11:43:14-07:00) format used to filter your search.  Acceptable values are "from-date, to-date", "from-date, " and ", to-date".)
        """
        super(QueryInputSet, self)._set_input('CreatedAtRange', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(QueryInputSet, self)._set_input('Fields', value)
    def set_FileExtensions(self, value):
        """
        Set the value of the FileExtensions input for this Choreo. ((optional, string) A comma-seperated list of extension types used to filter your search (e.g., pdf, png doc).)
        """
        super(QueryInputSet, self)._set_input('FileExtensions', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of search results to return. Defaults to 30.)
        """
        super(QueryInputSet, self)._set_input('Limit', value)
    def set_MDFilters(self, value):
        """
        Set the value of the MDFilters input for this Choreo. ((optional, string) Filters for a specific metadata template. Visit the metadata search documentation for more information (See Choreo notes for more details).)
        """
        super(QueryInputSet, self)._set_input('MDFilters', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The search result at which to start the response. Defaults to 0.)
        """
        super(QueryInputSet, self)._set_input('Offset', value)
    def set_OwnerUserIDs(self, value):
        """
        Set the value of the OwnerUserIDs input for this Choreo. ((optional, string) A comma-seperated list of owner IDs which are used to filter your search.)
        """
        super(QueryInputSet, self)._set_input('OwnerUserIDs', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) The string to search for; can be matched against item names, descriptions, text content of a file, and other fields of the different item types.)
        """
        super(QueryInputSet, self)._set_input('Query', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) The scope for which you want to limit your search to. Can be user_content for a search limited to only the current user or enterprise_content for the entire enterprise.)
        """
        super(QueryInputSet, self)._set_input('Scope', value)
    def set_SizeRange(self, value):
        """
        Set the value of the SizeRange input for this Choreo. ((optional, string) Filter by a file size range. Specify the file size range in bytes separated by a comma (e.g., 50, 100).)
        """
        super(QueryInputSet, self)._set_input('SizeRange', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type you want to return in your search. Can be file, folder, or web_link.)
        """
        super(QueryInputSet, self)._set_input('Type', value)
    def set_UpdatedAtRange(self, value):
        """
        Set the value of the UpdatedAtRange input for this Choreo. ((optional, date) A comma-seperated date range in ISO-8601 (2012-11-02T11:43:14-07:00) format used to filter your search.  Acceptable values are "from-date, to-date", "from-date, " and ", to-date".)
        """
        super(QueryInputSet, self)._set_input('UpdatedAtRange', value)


class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
