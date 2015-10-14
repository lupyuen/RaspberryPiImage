# -*- coding: utf-8 -*-

###############################################################################
#
# GetShippingCosts
# Retrieves shipping costs for an item.
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

class GetShippingCosts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetShippingCosts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetShippingCosts, self).__init__(temboo_session, '/Library/eBay/Shopping/GetShippingCosts')


    def new_input_set(self):
        return GetShippingCostsInputSet()

    def _make_result_set(self, result, path):
        return GetShippingCostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetShippingCostsChoreographyExecution(session, exec_id, path)

class GetShippingCostsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetShippingCosts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(GetShippingCostsInputSet, self)._set_input('AppID', value)
    def set_DestinationCountryCode(self, value):
        """
        Set the value of the DestinationCountryCode input for this Choreo. ((conditional, string) The shipment destination country code.)
        """
        super(GetShippingCostsInputSet, self)._set_input('DestinationCountryCode', value)
    def set_DestinationPostalCode(self, value):
        """
        Set the value of the DestinationPostalCode input for this Choreo. ((conditional, string) The shipment destination postal code.)
        """
        super(GetShippingCostsInputSet, self)._set_input('DestinationPostalCode', value)
    def set_IncludeDetails(self, value):
        """
        Set the value of the IncludeDetails input for this Choreo. ((conditional, boolean) Indicates whether to return the ShippingDetails container in the response.)
        """
        super(GetShippingCostsInputSet, self)._set_input('IncludeDetails', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The ID of the item to get shipping costs for.)
        """
        super(GetShippingCostsInputSet, self)._set_input('ItemID', value)
    def set_QuantitySold(self, value):
        """
        Set the value of the QuantitySold input for this Choreo. ((optional, string) The quantity of items being shipped.)
        """
        super(GetShippingCostsInputSet, self)._set_input('QuantitySold', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetShippingCostsInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetShippingCostsInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetShippingCostsInputSet, self)._set_input('SiteID', value)

class GetShippingCostsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetShippingCosts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetShippingCostsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetShippingCostsResultSet(response, path)
