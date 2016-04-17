# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewsItem
# Queries the Newswire API for a specific news item.
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

class GetNewsItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNewsItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNewsItem, self).__init__(temboo_session, '/Library/NYTimes/TimesNewswire/GetNewsItem')


    def new_input_set(self):
        return GetNewsItemInputSet()

    def _make_result_set(self, result, path):
        return GetNewsItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsItemChoreographyExecution(session, exec_id, path)

class GetNewsItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNewsItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(GetNewsItemInputSet, self)._set_input('APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetNewsItemInputSet, self)._set_input('ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The complete URL of a specific news item. This URL is returned in the output of the GetRecentNews Choreo.)
        """
        super(GetNewsItemInputSet, self)._set_input('URL', value)

class GetNewsItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNewsItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetNewsItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNewsItemResultSet(response, path)
