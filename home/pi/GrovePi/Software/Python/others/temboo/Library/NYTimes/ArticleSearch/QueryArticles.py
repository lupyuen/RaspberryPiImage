# -*- coding: utf-8 -*-

###############################################################################
#
# QueryArticles
# Searches New York Times articles and retrieves headlines, abstracts, lead paragraphs, links to associated multimedia, and other article metadata.
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

class QueryArticles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the QueryArticles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(QueryArticles, self).__init__(temboo_session, '/Library/NYTimes/ArticleSearch/QueryArticles')


    def new_input_set(self):
        return QueryArticlesInputSet()

    def _make_result_set(self, result, path):
        return QueryArticlesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryArticlesChoreographyExecution(session, exec_id, path)

class QueryArticlesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the QueryArticles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(QueryArticlesInputSet, self)._set_input('APIKey', value)
    def set_BeginDate(self, value):
        """
        Set the value of the BeginDate input for this Choreo. ((optional, date) Filters the result for articles with publication dates of the date specified or later. Dates should be formatted like YYYYMMDD.)
        """
        super(QueryArticlesInputSet, self)._set_input('BeginDate', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Filters the result for articles with publication dates of the date specified or earlier. Dates should be formatted like YYYYMMDD.)
        """
        super(QueryArticlesInputSet, self)._set_input('EndDate', value)
    def set_FacetFilter(self, value):
        """
        Set the value of the FacetFilter input for this Choreo. ((optional, boolean) When set to "true", facet counts will respect any applied filters such as Query, BeginDate, EndDate, etc.)
        """
        super(QueryArticlesInputSet, self)._set_input('FacetFilter', value)
    def set_Facets(self, value):
        """
        Set the value of the Facets input for this Choreo. ((optional, string) A comma-delimited list of facets. This indicates the sets of facet values to include in the response. Valid facets include: section_name, document_type, type_of_material, source, and day_of_week.)
        """
        super(QueryArticlesInputSet, self)._set_input('Facets', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-delimited list of fields to return.)
        """
        super(QueryArticlesInputSet, self)._set_input('Fields', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) An advanced search option that allows you to filter by specific fields. See Choreo notes for syntax details.)
        """
        super(QueryArticlesInputSet, self)._set_input('Filter', value)
    def set_Highlighting(self, value):
        """
        Set the value of the Highlighting input for this Choreo. ((optional, boolean) Enables highlighting in search results. When set to "true", the value of Query is highlighted in the headline and lead_paragraph fields. Defaults to "false".)
        """
        super(QueryArticlesInputSet, self)._set_input('Highlighting', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) This corresponds to which set of 10 results is returned. Used to page through results. Set to 0 to return records 0-9, set to 1 to return records 10-19, etc.)
        """
        super(QueryArticlesInputSet, self)._set_input('Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) Searches the article body, headline and byline for the specified term.)
        """
        super(QueryArticlesInputSet, self)._set_input('Query', value)
    def set_Rank(self, value):
        """
        Set the value of the Rank input for this Choreo. ((optional, string) By default, search results are sorted by their relevance to the Query provided. Set to "newest" or "oldest" to sort by publication date.)
        """
        super(QueryArticlesInputSet, self)._set_input('Rank', value)

class QueryArticlesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the QueryArticles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class QueryArticlesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryArticlesResultSet(response, path)
