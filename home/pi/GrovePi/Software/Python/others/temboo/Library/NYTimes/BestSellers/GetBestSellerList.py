# -*- coding: utf-8 -*-

###############################################################################
#
# GetBestSellerList
# Retrieves data from a New York Times best-seller list for a specified date.
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

class GetBestSellerList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBestSellerList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBestSellerList, self).__init__(temboo_session, '/Library/NYTimes/BestSellers/GetBestSellerList')


    def new_input_set(self):
        return GetBestSellerListInputSet()

    def _make_result_set(self, result, path):
        return GetBestSellerListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBestSellerListChoreographyExecution(session, exec_id, path)

class GetBestSellerListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBestSellerList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(GetBestSellerListInputSet, self)._set_input('APIKey', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The best-seller list publication date in YYYY-MM-DD format.)
        """
        super(GetBestSellerListInputSet, self)._set_input('Date', value)
    def set_ListName(self, value):
        """
        Set the value of the ListName input for this Choreo. ((required, string) The Times best-seller list to retrieve (i.e. e-book-fiction or hardcover-fiction).)
        """
        super(GetBestSellerListInputSet, self)._set_input('ListName', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value.)
        """
        super(GetBestSellerListInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetBestSellerListInputSet, self)._set_input('ResponseFormat', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The column name to sort by. Valid values are: bestsellers-date, date, isbn, list, list-name, published-date, rank, rank-last-week, and weeks-on-list.)
        """
        super(GetBestSellerListInputSet, self)._set_input('SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) The sort order. Valid values are: ASC and DESC.)
        """
        super(GetBestSellerListInputSet, self)._set_input('SortOrder', value)

class GetBestSellerListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBestSellerList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetBestSellerListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBestSellerListResultSet(response, path)
