# -*- coding: utf-8 -*-

###############################################################################
#
# GetBestSellerHistory
# Retrieves information about New York Times best-sellers that match a specified search criteria.
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

class GetBestSellerHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBestSellerHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBestSellerHistory, self).__init__(temboo_session, '/Library/NYTimes/BestSellers/GetBestSellerHistory')


    def new_input_set(self):
        return GetBestSellerHistoryInputSet()

    def _make_result_set(self, result, path):
        return GetBestSellerHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBestSellerHistoryChoreographyExecution(session, exec_id, path)

class GetBestSellerHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBestSellerHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('APIKey', value)
    def set_AgeGroup(self, value):
        """
        Set the value of the AgeGroup input for this Choreo. ((optional, string) The target age group for the best seller.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('AgeGroup', value)
    def set_Author(self, value):
        """
        Set the value of the Author input for this Choreo. ((optional, string) The author of the best seller.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Author', value)
    def set_Contributor(self, value):
        """
        Set the value of the Contributor input for this Choreo. ((optional, string) The author of the best seller, as well as other contributors such as the illustrator.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Contributor', value)
    def set_ISBN(self, value):
        """
        Set the value of the ISBN input for this Choreo. ((optional, string) International Standard Book Number, 10 or 13 digits.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('ISBN', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Offset', value)
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((optional, decimal) The publisher's list price of the best seller, including decimal point.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Price', value)
    def set_Publisher(self, value):
        """
        Set the value of the Publisher input for this Choreo. ((optional, string) The standardized name of the publisher.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Publisher', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should bein. Valid values are: json (the default), and xml.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('ResponseFormat', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The column name to sort by. Valid values are: age-group, author, contributor, isbn, price, publisher, and title.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) The sort order. Valid values are: ASC and DESC.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('SortOrder', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the best seller to retrieve data for.)
        """
        super(GetBestSellerHistoryInputSet, self)._set_input('Title', value)

class GetBestSellerHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBestSellerHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetBestSellerHistoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBestSellerHistoryResultSet(response, path)
