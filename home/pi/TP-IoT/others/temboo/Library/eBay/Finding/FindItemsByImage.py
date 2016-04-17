# -*- coding: utf-8 -*-

###############################################################################
#
# FindItemsByImage
# Finds items based on their image similarity to the specified item.
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

class FindItemsByImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindItemsByImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindItemsByImage, self).__init__(temboo_session, '/Library/eBay/Finding/FindItemsByImage')


    def new_input_set(self):
        return FindItemsByImageInputSet()

    def _make_result_set(self, result, path):
        return FindItemsByImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindItemsByImageChoreographyExecution(session, exec_id, path)

class FindItemsByImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindItemsByImage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FindItemsByImageRequest(self, value):
        """
        Set the value of the FindItemsByImageRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        super(FindItemsByImageInputSet, self)._set_input('FindItemsByImageRequest', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(FindItemsByImageInputSet, self)._set_input('AppID', value)
    def set_AspectFilters(self, value):
        """
        Set the value of the AspectFilters input for this Choreo. ((optional, json) A dictionary of key/value pairs to use as aspect filters for the request.)
        """
        super(FindItemsByImageInputSet, self)._set_input('AspectFilters', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((optional, string) Filters the results by category ID.)
        """
        super(FindItemsByImageInputSet, self)._set_input('CategoryID', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        super(FindItemsByImageInputSet, self)._set_input('EntriesPerPage', value)
    def set_GlobalID(self, value):
        """
        Set the value of the GlobalID input for this Choreo. ((optional, integer) The global ID of the eBay site to access (e.g., EBAY-US).)
        """
        super(FindItemsByImageInputSet, self)._set_input('GlobalID', value)
    def set_ItemFilters(self, value):
        """
        Set the value of the ItemFilters input for this Choreo. ((optional, json) A dictionary of key/value pairs to use as item filters for the request.)
        """
        super(FindItemsByImageInputSet, self)._set_input('ItemFilters', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The ID of an item associated with the image you want to use for matching. The item must be active and listed in a Clothing, Shoes & Accessories category (parent category ID 11450 on the eBay US site).)
        """
        super(FindItemsByImageInputSet, self)._set_input('ItemID', value)
    def set_OutputSelector(self, value):
        """
        Set the value of the OutputSelector input for this Choreo. ((optional, string) Controls the fields that are returned in the response (e.g., GalleryInfo).)
        """
        super(FindItemsByImageInputSet, self)._set_input('OutputSelector', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        super(FindItemsByImageInputSet, self)._set_input('PageNumber', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(FindItemsByImageInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(FindItemsByImageInputSet, self)._set_input('SandboxMode', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Valid values: BestMatch, BidCountMost, CountryAscending, CountryDescending, DistanceNearest, CurrentPriceHighest, EndTimeSoonest, PricePlusShippingHighest, PricePlusShippingLowest, StartTimeNewest.)
        """
        super(FindItemsByImageInputSet, self)._set_input('SortOrder', value)

class FindItemsByImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindItemsByImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class FindItemsByImageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindItemsByImageResultSet(response, path)
