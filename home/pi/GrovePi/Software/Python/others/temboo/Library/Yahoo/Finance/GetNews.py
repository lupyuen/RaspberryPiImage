# -*- coding: utf-8 -*-

###############################################################################
#
# GetNews
# Retrieves the most recent Yahoo Finance Company or Industry news items as an RSS feed.
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

class GetNews(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNews Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNews, self).__init__(temboo_session, '/Library/Yahoo/Finance/GetNews')


    def new_input_set(self):
        return GetNewsInputSet()

    def _make_result_set(self, result, path):
        return GetNewsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsChoreographyExecution(session, exec_id, path)

class GetNewsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNews
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Company(self, value):
        """
        Set the value of the Company input for this Choreo. ((required, string) Ticker symbol for one or more companies to search, separated by commas (e.g. YHOO,DIS to include news about Yahoo! and Disney).)
        """
        super(GetNewsInputSet, self)._set_input('Company', value)
    def set_NewsType(self, value):
        """
        Set the value of the NewsType input for this Choreo. ((required, string) Enter the type of news items you want to see in the RSS feed: headline or industry.)
        """
        super(GetNewsInputSet, self)._set_input('NewsType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetNewsInputSet, self)._set_input('ResponseFormat', value)

class GetNewsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNews Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo Finance.)
        """
        return self._output.get('Response', None)

class GetNewsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNewsResultSet(response, path)
