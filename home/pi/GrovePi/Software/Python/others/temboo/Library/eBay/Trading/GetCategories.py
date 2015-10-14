# -*- coding: utf-8 -*-

###############################################################################
#
# GetCategories
# Returns the latest category hierarchy for the eBay site.
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

class GetCategories(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCategories Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCategories, self).__init__(temboo_session, '/Library/eBay/Trading/GetCategories')


    def new_input_set(self):
        return GetCategoriesInputSet()

    def _make_result_set(self, result, path):
        return GetCategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCategoriesChoreographyExecution(session, exec_id, path)

class GetCategoriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCategories
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CategoryParent(self, value):
        """
        Set the value of the CategoryParent input for this Choreo. ((optional, string) Indicates the ID of the highest-level category to return. Multiple CategoryParent IDs can be specified in a comma-separated list.)
        """
        super(GetCategoriesInputSet, self)._set_input('CategoryParent', value)
    def set_CategorySiteID(self, value):
        """
        Set the value of the CategorySiteID input for this Choreo. ((optional, string) The ID for the site for which to retrieve the category hierarchy. Use the numeric site code (e.g., 0 for US, 77 for eBay Germany, etc).)
        """
        super(GetCategoriesInputSet, self)._set_input('CategorySiteID', value)
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The level of detail to return in the response. Valid values are: ReturnAll.)
        """
        super(GetCategoriesInputSet, self)._set_input('DetailLevel', value)
    def set_LevelLimit(self, value):
        """
        Set the value of the LevelLimit input for this Choreo. ((optional, string) Indicates the maximum depth of the category hierarchy to retrieve, where the top-level categories (meta-categories) are at level 1. Default is 0.)
        """
        super(GetCategoriesInputSet, self)._set_input('LevelLimit', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetCategoriesInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetCategoriesInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetCategoriesInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetCategoriesInputSet, self)._set_input('UserToken', value)
    def set_ViewAllNodes(self, value):
        """
        Set the value of the ViewAllNodes input for this Choreo. ((optional, boolean) A flag that controls whether all eBay categories are returned, or only leaf categories are returned. To retrieve leaf categories, set this parameter to 'false'.)
        """
        super(GetCategoriesInputSet, self)._set_input('ViewAllNodes', value)

class GetCategoriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCategories Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetCategoriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCategoriesResultSet(response, path)
