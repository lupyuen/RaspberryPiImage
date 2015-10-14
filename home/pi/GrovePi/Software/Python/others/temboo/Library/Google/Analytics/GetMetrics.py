# -*- coding: utf-8 -*-

###############################################################################
#
# GetMetrics
# Retrieves metrics such as visits, page views, bounces within a specified time frame.
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

class GetMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMetrics, self).__init__(temboo_session, '/Library/Google/Analytics/GetMetrics')


    def new_input_set(self):
        return GetMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMetricsChoreographyExecution(session, exec_id, path)

class GetMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(GetMetricsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetMetricsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetMetricsInputSet, self)._set_input('ClientSecret', value)
    def set_Dimensions(self, value):
        """
        Set the value of the Dimensions input for this Choreo. ((optional, string) Defines the primary data keys for your Analytics report. Use dimensions to segment your web property metrics (e.g.  ga:browser or ga:city).)
        """
        super(GetMetricsInputSet, self)._set_input('Dimensions', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The end date for the range of data you want to retrieve. Epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        super(GetMetricsInputSet, self)._set_input('EndDate', value)
    def set_Filters(self, value):
        """
        Set the value of the Filters input for this Choreo. ((optional, string) Restricts the data returned by a dimension or metric you want to filter by using an expression (i.e. ga:timeOnPage==10).)
        """
        super(GetMetricsInputSet, self)._set_input('Filters', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The max results to be returned in the feed. Defaults to 50.)
        """
        super(GetMetricsInputSet, self)._set_input('MaxResults', value)
    def set_Metrics(self, value):
        """
        Set the value of the Metrics input for this Choreo. ((optional, string) This is a comma separated list of metrics you want to retrieve. Defaults to: ga:visits,ga:bounces,ga:pageviews.)
        """
        super(GetMetricsInputSet, self)._set_input('Metrics', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Deprecated (retained for backward compatibility only).)
        """
        super(GetMetricsInputSet, self)._set_input('Password', value)
    def set_ProfileId(self, value):
        """
        Set the value of the ProfileId input for this Choreo. ((required, integer) The Google Analytics Profile ID to access. This is also known as the View ID. It can be found in the Admin > View Settings section of a particular profile.)
        """
        super(GetMetricsInputSet, self)._set_input('ProfileId', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetMetricsInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: XML (the default) and JSON.)
        """
        super(GetMetricsInputSet, self)._set_input('ResponseFormat', value)
    def set_Segment(self, value):
        """
        Set the value of the Segment input for this Choreo. ((optional, string) Used to segment your data by dimensions and/or metrics. You can use expressions for segments just as you would for the Filters parameter.)
        """
        super(GetMetricsInputSet, self)._set_input('Segment', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Indicates the sorting order and direction for the returned data. Values can be separated by commas (i.e. ga:browser,ga:pageviews).)
        """
        super(GetMetricsInputSet, self)._set_input('Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The start date for the range of data to retrieve. Use epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        super(GetMetricsInputSet, self)._set_input('StartDate', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The starting entry for the feed. Defaults to 1.)
        """
        super(GetMetricsInputSet, self)._set_input('StartIndex', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Deprecated (retained for backward compatibility only).)
        """
        super(GetMetricsInputSet, self)._set_input('Username', value)

class GetMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)
    def get_Bounces(self):
        """
        Retrieve the value for the "Bounces" output from this Choreo execution. ((integer) The bounces metrics parsed from the Google Analytics response)
        """
        return self._output.get('Bounces', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_PageViews(self):
        """
        Retrieve the value for the "PageViews" output from this Choreo execution. ((integer) The page views parsed from the Google Analytics response)
        """
        return self._output.get('PageViews', None)
    def get_Visits(self):
        """
        Retrieve the value for the "Visits" output from this Choreo execution. ((integer) The visits metrics parsed from the Google Analytics response.)
        """
        return self._output.get('Visits', None)

class GetMetricsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMetricsResultSet(response, path)
