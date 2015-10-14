# -*- coding: utf-8 -*-

###############################################################################
#
# FullTextSearch
# Returns a list of Congressional Record documents in which the given phrase appears.
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

class FullTextSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FullTextSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FullTextSearch, self).__init__(temboo_session, '/Library/SunlightLabs/CapitolWords/FullTextSearch')


    def new_input_set(self):
        return FullTextSearchInputSet()

    def _make_result_set(self, result, path):
        return FullTextSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FullTextSearchChoreographyExecution(session, exec_id, path)

class FullTextSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FullTextSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(FullTextSearchInputSet, self)._set_input('APIKey', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) Limit results to the member of Congress with the given Bioguide ID. The Bioguide ID of any current or past congressonal member can be found at bioguide.congress.gov.)
        """
        super(FullTextSearchInputSet, self)._set_input('BioguideID', value)
    def set_CRPages(self, value):
        """
        Set the value of the CRPages input for this Choreo. ((optional, string) The pages in the Congressional Record to search.)
        """
        super(FullTextSearchInputSet, self)._set_input('CRPages', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        super(FullTextSearchInputSet, self)._set_input('Chamber', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        super(FullTextSearchInputSet, self)._set_input('Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        super(FullTextSearchInputSet, self)._set_input('EndDate', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to show. 100 shown at a time.)
        """
        super(FullTextSearchInputSet, self)._set_input('Page', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        super(FullTextSearchInputSet, self)._set_input('Party', value)
    def set_Phrase(self, value):
        """
        Set the value of the Phrase input for this Choreo. ((required, string) A phrase to search the body of each Congressional Record document for. Either Phrase or Title inputs are required.)
        """
        super(FullTextSearchInputSet, self)._set_input('Phrase', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        super(FullTextSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        super(FullTextSearchInputSet, self)._set_input('StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        super(FullTextSearchInputSet, self)._set_input('State', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, integer) A phrase to search the title of each Congressional Record document for. Either Phrase or Title are required.)
        """
        super(FullTextSearchInputSet, self)._set_input('Title', value)

class FullTextSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FullTextSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CapitolWords.)
        """
        return self._output.get('Response', None)

class FullTextSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FullTextSearchResultSet(response, path)
