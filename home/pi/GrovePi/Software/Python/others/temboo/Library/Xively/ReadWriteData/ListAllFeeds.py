# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllFeeds
# Returns filterable data on all feeds viewable by the authenticated account.
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

class ListAllFeeds(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllFeeds Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAllFeeds, self).__init__(temboo_session, '/Library/Xively/ReadWriteData/ListAllFeeds')


    def new_input_set(self):
        return ListAllFeedsInputSet()

    def _make_result_set(self, result, path):
        return ListAllFeedsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllFeedsChoreographyExecution(session, exec_id, path)

class ListAllFeedsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllFeeds
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(ListAllFeedsInputSet, self)._set_input('APIKey', value)
    def set_Content(self, value):
        """
        Set the value of the Content input for this Choreo. ((optional, string) Describes whether to return full or summary results. Full - all datastream values are returned, summary - returns the environment metadata for each feed. Valid values: 'full' or 'summary'.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Content', value)
    def set_DistanceUnits(self, value):
        """
        Set the value of the DistanceUnits input for this Choreo. ((optional, string) Units of distance. Valid values: "miles" or "kms" (default).)
        """
        super(ListAllFeedsInputSet, self)._set_input('DistanceUnits', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, decimal) Search radius (units like miles or kilometers defined by DistanceUnits). Ex: 5.0.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Distance', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being returned. Valid values are "json" (the default), "xml" and "csv". No metadata is returned for the csv feed.)
        """
        super(ListAllFeedsInputSet, self)._set_input('FeedType', value)
    def set_FullTextSearch(self, value):
        """
        Set the value of the FullTextSearch input for this Choreo. ((optional, string) Returns any feeds matching this string.)
        """
        super(ListAllFeedsInputSet, self)._set_input('FullTextSearch', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Used to find feeds located around this latitude. Ex. 51.5235375648154.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Used to find feeds located around this longitude. Ex: -0.0807666778564453.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Longitude', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates which page of results you are requesting. Starts from 1.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Defines how many results to return per page (1 to 1000).)
        """
        super(ListAllFeedsInputSet, self)._set_input('PerPage', value)
    def set_ShowUser(self, value):
        """
        Set the value of the ShowUser input for this Choreo. ((optional, string) Include user login and user level for each feed. Valid values: true, false (default).)
        """
        super(ListAllFeedsInputSet, self)._set_input('ShowUser', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Order of returned feeds. Valid values: "created_at", "retrieved_at" or "relevance".)
        """
        super(ListAllFeedsInputSet, self)._set_input('SortOrder', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Sets whether to search for only live feeds, only frozen feeds, or all feeds. Valid values: "live", "frozen", "all" (default).)
        """
        super(ListAllFeedsInputSet, self)._set_input('Status', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Returns feeds containing datastreams tagged with the search query.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Tag', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Returns feeds containing datastreams with units specified by the search query. Ex: Celsius.)
        """
        super(ListAllFeedsInputSet, self)._set_input('Units', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((optional, string) Returns feeds created by the user specified.)
        """
        super(ListAllFeedsInputSet, self)._set_input('User', value)

class ListAllFeedsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllFeeds Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ListAllFeedsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAllFeedsResultSet(response, path)
