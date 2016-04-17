# -*- coding: utf-8 -*-

###############################################################################
#
# GetCategoryFeatures
# Returns information that describes the feature and value settings that apply to the set of eBay categories.
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

class GetCategoryFeatures(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCategoryFeatures Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCategoryFeatures, self).__init__(temboo_session, '/Library/eBay/Trading/GetCategoryFeatures')


    def new_input_set(self):
        return GetCategoryFeaturesInputSet()

    def _make_result_set(self, result, path):
        return GetCategoryFeaturesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCategoryFeaturesChoreographyExecution(session, exec_id, path)

class GetCategoryFeaturesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCategoryFeatures
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AllFeaturesForCategory(self, value):
        """
        Set the value of the AllFeaturesForCategory input for this Choreo. ((optional, boolean) A flag used to view all of the feature settings for a specific category.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('AllFeaturesForCategory', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((optional, string) The ID of the category for which you want to retrieve the feature settings.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('CategoryID', value)
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The level of detail to return in the response. Valid values are: ReturnAll and ReturnSummary.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('DetailLevel', value)
    def set_FeatureID(self, value):
        """
        Set the value of the FeatureID input for this Choreo. ((optional, string) Use this field if you want to know if specific features are enabled at the site or root category level. Multiple FeatureIDs can be specified in a comma-separated list.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('FeatureID', value)
    def set_LevelLimit(self, value):
        """
        Set the value of the LevelLimit input for this Choreo. ((optional, string) Indicates the maximum depth of the category hierarchy to retrieve, where the top-level categories (meta-categories) are at level 1. Default is 0.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('LevelLimit', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('UserToken', value)
    def set_ViewAllNodes(self, value):
        """
        Set the value of the ViewAllNodes input for this Choreo. ((optional, boolean) Indicates that eBay should return the site defaults along with all the categories that override the feature settings they inherit. DetailLevel must be 'ReturnAll' when setting this parameter to true.)
        """
        super(GetCategoryFeaturesInputSet, self)._set_input('ViewAllNodes', value)

class GetCategoryFeaturesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCategoryFeatures Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetCategoryFeaturesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCategoryFeaturesResultSet(response, path)
