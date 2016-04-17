# -*- coding: utf-8 -*-

###############################################################################
#
# FindItemsByProduct
# Finds items based upon a product ID, such as an ISBN, UPC, EAN, or ePID.
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

class FindItemsByProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindItemsByProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindItemsByProduct, self).__init__(temboo_session, '/Library/eBay/Finding/FindItemsByProduct')


    def new_input_set(self):
        return FindItemsByProductInputSet()

    def _make_result_set(self, result, path):
        return FindItemsByProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindItemsByProductChoreographyExecution(session, exec_id, path)

class FindItemsByProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindItemsByProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FindItemsByProductRequest(self, value):
        """
        Set the value of the FindItemsByProductRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        super(FindItemsByProductInputSet, self)._set_input('FindItemsByProductRequest', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(FindItemsByProductInputSet, self)._set_input('AppID', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        super(FindItemsByProductInputSet, self)._set_input('EntriesPerPage', value)
    def set_GlobalID(self, value):
        """
        Set the value of the GlobalID input for this Choreo. ((optional, integer) The global ID of the eBay site to access (e.g., EBAY-US).)
        """
        super(FindItemsByProductInputSet, self)._set_input('GlobalID', value)
    def set_ItemFilters(self, value):
        """
        Set the value of the ItemFilters input for this Choreo. ((optional, json) A dictionary of key/value pairs to use as item filters for the request.)
        """
        super(FindItemsByProductInputSet, self)._set_input('ItemFilters', value)
    def set_OutputSelector(self, value):
        """
        Set the value of the OutputSelector input for this Choreo. ((optional, string) Controls the fields that are returned in the response (e.g., GalleryInfo).)
        """
        super(FindItemsByProductInputSet, self)._set_input('OutputSelector', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        super(FindItemsByProductInputSet, self)._set_input('PageNumber', value)
    def set_ProductIDType(self, value):
        """
        Set the value of the ProductIDType input for this Choreo. ((required, string) The type of identifier being used to find a product. Valid values are: ReferenceID, ISBN, UPC, and EAN.)
        """
        super(FindItemsByProductInputSet, self)._set_input('ProductIDType', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The ID of a product to find.)
        """
        super(FindItemsByProductInputSet, self)._set_input('ProductID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(FindItemsByProductInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(FindItemsByProductInputSet, self)._set_input('SandboxMode', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Valid values: BestMatch, BidCountMost, CountryAscending, CountryDescending, DistanceNearest, CurrentPriceHighest, EndTimeSoonest, PricePlusShippingHighest, PricePlusShippingLowest, StartTimeNewest.)
        """
        super(FindItemsByProductInputSet, self)._set_input('SortOrder', value)

class FindItemsByProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindItemsByProduct Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class FindItemsByProductChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindItemsByProductResultSet(response, path)
