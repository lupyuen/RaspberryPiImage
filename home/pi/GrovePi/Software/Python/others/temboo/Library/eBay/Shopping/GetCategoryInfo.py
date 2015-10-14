# -*- coding: utf-8 -*-

###############################################################################
#
# GetCategoryInfo
# Retrieve high-level category information for a specified category.
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

class GetCategoryInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCategoryInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCategoryInfo, self).__init__(temboo_session, '/Library/eBay/Shopping/GetCategoryInfo')


    def new_input_set(self):
        return GetCategoryInfoInputSet()

    def _make_result_set(self, result, path):
        return GetCategoryInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCategoryInfoChoreographyExecution(session, exec_id, path)

class GetCategoryInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCategoryInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('AppID', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((required, string) The ID of a category to retrieve. Use an ID of -1 to retrieve the root category and the top-level (level 1) meta categories.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('CategoryID', value)
    def set_IncludeSelector(self, value):
        """
        Set the value of the IncludeSelector input for this Choreo. ((optional, string) Defines standard subsets of fields to return within the response. Valid values are: ChildCategories.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('IncludeSelector', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetCategoryInfoInputSet, self)._set_input('SiteID', value)

class GetCategoryInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCategoryInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetCategoryInfoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCategoryInfoResultSet(response, path)
