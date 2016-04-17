# -*- coding: utf-8 -*-

###############################################################################
#
# GetPicks
# Retrieves lists of reviews and NYT Critics' Picks.
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

class GetPicks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPicks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPicks, self).__init__(temboo_session, '/Library/NYTimes/MovieReviews/GetPicks')


    def new_input_set(self):
        return GetPicksInputSet()

    def _make_result_set(self, result, path):
        return GetPicksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPicksChoreographyExecution(session, exec_id, path)

class GetPicksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPicks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by NY Times.)
        """
        super(GetPicksInputSet, self)._set_input('APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return.)
        """
        super(GetPicksInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) A numeric value indicating the starting point of the result set. Used to page through results.)
        """
        super(GetPicksInputSet, self)._set_input('Offset', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Sets the sort order of the results. Accepted values are: by-title, by-publication-date, by-opening-date, by-dvd-release-date.)
        """
        super(GetPicksInputSet, self)._set_input('Order', value)
    def set_ResourceType(self, value):
        """
        Set the value of the ResourceType input for this Choreo. ((optional, string) Specify "picks" to get NYT Critics' Picks in theaters or "dvd-picks" to get NYT Critics' Picks on DVD. Specify "all" to retrieve all reviews.)
        """
        super(GetPicksInputSet, self)._set_input('ResourceType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetPicksInputSet, self)._set_input('ResponseFormat', value)

class GetPicksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPicks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetPicksChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPicksResultSet(response, path)
