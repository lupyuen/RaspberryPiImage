# -*- coding: utf-8 -*-

###############################################################################
#
# AddBasicListing
# Allows you create a basic listing on eBay using scalar inputs rather than an XML request.
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

class AddBasicListing(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddBasicListing Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddBasicListing, self).__init__(temboo_session, '/Library/eBay/Trading/AddBasicListing')


    def new_input_set(self):
        return AddBasicListingInputSet()

    def _make_result_set(self, result, path):
        return AddBasicListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddBasicListingChoreographyExecution(session, exec_id, path)

class AddBasicListingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddBasicListing
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BuyItNowPrice(self, value):
        """
        Set the value of the BuyItNowPrice input for this Choreo. ((optional, decimal) Allows a user to purchase the item at a Buy It Now price and end the auction immediately.)
        """
        super(AddBasicListingInputSet, self)._set_input('BuyItNowPrice', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((conditional, integer) The numeric ID for a category on eBay. Category IDs can be retrieved with the GetCategories Choreo.)
        """
        super(AddBasicListingInputSet, self)._set_input('CategoryID', value)
    def set_ConditionID(self, value):
        """
        Set the value of the ConditionID input for this Choreo. ((conditional, integer) The numeric ID (e.g., 1000) for the item condition.)
        """
        super(AddBasicListingInputSet, self)._set_input('ConditionID', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((conditional, string) The country where the item is located in.)
        """
        super(AddBasicListingInputSet, self)._set_input('Country', value)
    def set_Currency(self, value):
        """
        Set the value of the Currency input for this Choreo. ((conditional, string) The currency associated with the item price.)
        """
        super(AddBasicListingInputSet, self)._set_input('Currency', value)
    def set_DispatchTimeMax(self, value):
        """
        Set the value of the DispatchTimeMax input for this Choreo. ((conditional, integer) Specifies the maximum number of business days the seller commits to for preparing an item to be shipped after receiving a cleared payment.)
        """
        super(AddBasicListingInputSet, self)._set_input('DispatchTimeMax', value)
    def set_ExpeditedService(self, value):
        """
        Set the value of the ExpeditedService input for this Choreo. ((optional, boolean) Whether or not the seller is offering expedited shipping service options.)
        """
        super(AddBasicListingInputSet, self)._set_input('ExpeditedService', value)
    def set_ItemDescription(self, value):
        """
        Set the value of the ItemDescription input for this Choreo. ((conditional, string) The seller's description of the item.)
        """
        super(AddBasicListingInputSet, self)._set_input('ItemDescription', value)
    def set_ListingDuration(self, value):
        """
        Set the value of the ListingDuration input for this Choreo. ((conditional, string) The number of days the seller wants the listing to be active (e.g., Days_7). A complete list of accepted values is returned when calling GetCategoryFeatures with DetailLevel set to ReturnAll.)
        """
        super(AddBasicListingInputSet, self)._set_input('ListingDuration', value)
    def set_ListingType(self, value):
        """
        Set the value of the ListingType input for this Choreo. ((optional, string) The format of the listing the seller wants to use. Valid values are: AdType, Chinese, FixedPriceItem, Half, LeadGeneration.)
        """
        super(AddBasicListingInputSet, self)._set_input('ListingType', value)
    def set_PayPalEmailAddress(self, value):
        """
        Set the value of the PayPalEmailAddress input for this Choreo. ((conditional, string) The seller's PayPal email address. Required when a PaymentMethod is PayPal.)
        """
        super(AddBasicListingInputSet, self)._set_input('PayPalEmailAddress', value)
    def set_PaymentMethods(self, value):
        """
        Set the value of the PaymentMethods input for this Choreo. ((conditional, string) Identifies the payment method (such as PayPal) that the seller will accept when the buyer pays for the item. This can be a comma-separated list (e.g., VisaMC,PayPal).)
        """
        super(AddBasicListingInputSet, self)._set_input('PaymentMethods', value)
    def set_PictureURL(self, value):
        """
        Set the value of the PictureURL input for this Choreo. ((conditional, string) The URL for a picture associated with an item. Multiple URLs can be specified as a comma-separated list.)
        """
        super(AddBasicListingInputSet, self)._set_input('PictureURL', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((conditional, string) The Postal code of the place where the item is located.)
        """
        super(AddBasicListingInputSet, self)._set_input('PostalCode', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((conditional, integer) Indicates the quantity of items available for purchase in the listing. Required for all auction listings and for non-variation, fixed-price listings. For auction listings, this value is always '1'.)
        """
        super(AddBasicListingInputSet, self)._set_input('Quantity', value)
    def set_RefundOption(self, value):
        """
        Set the value of the RefundOption input for this Choreo. ((optional, string) Indicates how the seller will compensate the buyer for a returned item (e.g. MoneyBack).)
        """
        super(AddBasicListingInputSet, self)._set_input('RefundOption', value)
    def set_ReservePrice(self, value):
        """
        Set the value of the ReservePrice input for this Choreo. ((optional, decimal) The lowest price at which the seller is willing to sell the item.)
        """
        super(AddBasicListingInputSet, self)._set_input('ReservePrice', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(AddBasicListingInputSet, self)._set_input('ResponseFormat', value)
    def set_ReturnPolicyDescription(self, value):
        """
        Set the value of the ReturnPolicyDescription input for this Choreo. ((optional, string) The text description of return policy details.)
        """
        super(AddBasicListingInputSet, self)._set_input('ReturnPolicyDescription', value)
    def set_ReturnsAcceptedOption(self, value):
        """
        Set the value of the ReturnsAcceptedOption input for this Choreo. ((conditional, string) Indicates whether the seller allows the buyer to return the item (e.g., ReturnsAccepted).)
        """
        super(AddBasicListingInputSet, self)._set_input('ReturnsAcceptedOption', value)
    def set_ReturnsWithinOption(self, value):
        """
        Set the value of the ReturnsWithinOption input for this Choreo. ((optional, string) The period of time the buyer has to return the item (e.g., Days_14). To accepted values for this field, call GeteBayDetails with DetailName set to ReturnPolicyDetails.)
        """
        super(AddBasicListingInputSet, self)._set_input('ReturnsWithinOption', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(AddBasicListingInputSet, self)._set_input('SandboxMode', value)
    def set_ShippingServiceAdditionalCost(self, value):
        """
        Set the value of the ShippingServiceAdditionalCost input for this Choreo. ((optional, decimal) Shipping costs in addition to the value specified for the ShippingServiceCost parameter.)
        """
        super(AddBasicListingInputSet, self)._set_input('ShippingServiceAdditionalCost', value)
    def set_ShippingServiceCost(self, value):
        """
        Set the value of the ShippingServiceCost input for this Choreo. ((conditional, decimal) The cost for shipping the item.)
        """
        super(AddBasicListingInputSet, self)._set_input('ShippingServiceCost', value)
    def set_ShippingService(self, value):
        """
        Set the value of the ShippingService input for this Choreo. ((conditional, string) The name of the shipping service offered (e.g. UPSGround, USPSMedia).)
        """
        super(AddBasicListingInputSet, self)._set_input('ShippingService', value)
    def set_ShippingType(self, value):
        """
        Set the value of the ShippingType input for this Choreo. ((conditional, string) The shipping cost model offered by the seller. Valid values are: Calculated, CalculatedDomesticFlatInternational, Flat, FlatDomesticCalculatedInternational, FreightFlat, NotSpecified.)
        """
        super(AddBasicListingInputSet, self)._set_input('ShippingType', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(AddBasicListingInputSet, self)._set_input('SiteID', value)
    def set_Site(self, value):
        """
        Set the value of the Site input for this Choreo. ((optional, string) The name of the site on which the item is listed. This should corresponse to the SiteID. Default value is "US".)
        """
        super(AddBasicListingInputSet, self)._set_input('Site', value)
    def set_StartPrice(self, value):
        """
        Set the value of the StartPrice input for this Choreo. ((conditional, decimal) This value indicates the starting price of the item when it is listed for the first time.)
        """
        super(AddBasicListingInputSet, self)._set_input('StartPrice', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the item as it appears in the listing or search results.)
        """
        super(AddBasicListingInputSet, self)._set_input('Title', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(AddBasicListingInputSet, self)._set_input('UserToken', value)

class AddBasicListingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddBasicListing Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class AddBasicListingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddBasicListingResultSet(response, path)
