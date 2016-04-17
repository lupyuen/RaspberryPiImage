# -*- coding: utf-8 -*-

###############################################################################
#
# GetStockQuote
# Retrieves information for the specified stock symbol from Yahoo Finance.
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

class GetStockQuote(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetStockQuote Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetStockQuote, self).__init__(temboo_session, '/Library/Yahoo/Finance/GetStockQuote')


    def new_input_set(self):
        return GetStockQuoteInputSet()

    def _make_result_set(self, result, path):
        return GetStockQuoteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStockQuoteChoreographyExecution(session, exec_id, path)

class GetStockQuoteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetStockQuote
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetStockQuoteInputSet, self)._set_input('ResponseFormat', value)
    def set_StockSymbol(self, value):
        """
        Set the value of the StockSymbol input for this Choreo. ((required, string) The stock ticker symbol to search for (e.g., AAPL, GOOG, etc).)
        """
        super(GetStockQuoteInputSet, self)._set_input('StockSymbol', value)

class GetStockQuoteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetStockQuote Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo Finance.)
        """
        return self._output.get('Response', None)
    def get_Ask(self):
        """
        Retrieve the value for the "Ask" output from this Choreo execution. ((decimal) The asking price.)
        """
        return self._output.get('Ask', None)
    def get_Bid(self):
        """
        Retrieve the value for the "Bid" output from this Choreo execution. ((decimal) The bid price.)
        """
        return self._output.get('Bid', None)
    def get_Change(self):
        """
        Retrieve the value for the "Change" output from this Choreo execution. ((string) The change in the stock price.)
        """
        return self._output.get('Change', None)
    def get_DaysHigh(self):
        """
        Retrieve the value for the "DaysHigh" output from this Choreo execution. ((decimal) The high price of the day.)
        """
        return self._output.get('DaysHigh', None)
    def get_DaysLow(self):
        """
        Retrieve the value for the "DaysLow" output from this Choreo execution. ((decimal) The low price of the day.)
        """
        return self._output.get('DaysLow', None)
    def get_LastTradePriceOnly(self):
        """
        Retrieve the value for the "LastTradePriceOnly" output from this Choreo execution. ((decimal) The last trade price.)
        """
        return self._output.get('LastTradePriceOnly', None)
    def get_Open(self):
        """
        Retrieve the value for the "Open" output from this Choreo execution. ((decimal) The price when the market last opened.)
        """
        return self._output.get('Open', None)
    def get_PreviousClose(self):
        """
        Retrieve the value for the "PreviousClose" output from this Choreo execution. ((decimal) The previous closing price.)
        """
        return self._output.get('PreviousClose', None)
    def get_Volume(self):
        """
        Retrieve the value for the "Volume" output from this Choreo execution. ((integer) The volume traded.)
        """
        return self._output.get('Volume', None)
    def get_YearHigh(self):
        """
        Retrieve the value for the "YearHigh" output from this Choreo execution. ((decimal) The price for the year high.)
        """
        return self._output.get('YearHigh', None)
    def get_YearLow(self):
        """
        Retrieve the value for the "YearLow" output from this Choreo execution. ((decimal) The price for the year low.)
        """
        return self._output.get('YearLow', None)

class GetStockQuoteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetStockQuoteResultSet(response, path)
