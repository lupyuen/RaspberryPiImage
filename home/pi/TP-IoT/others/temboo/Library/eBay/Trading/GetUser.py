# -*- coding: utf-8 -*-

###############################################################################
#
# GetUser
# Retrieves data pertaining to a single eBay user.
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

class GetUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUser, self).__init__(temboo_session, '/Library/eBay/Trading/GetUser')


    def new_input_set(self):
        return GetUserInputSet()

    def _make_result_set(self, result, path):
        return GetUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserChoreographyExecution(session, exec_id, path)

class GetUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The level of detail to return in the response. Valid values are: ReturnAll or ReturnSummary.)
        """
        super(GetUserInputSet, self)._set_input('DetailLevel', value)
    def set_IncludeFeatureEligibility(self, value):
        """
        Set the value of the IncludeFeatureEligibility input for this Choreo. ((optional, boolean) Whether or not to include feature eligibility information in the response. Set to true or false.)
        """
        super(GetUserInputSet, self)._set_input('IncludeFeatureEligibility', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((optional, string) The ID of the item of a successfully concluded listing in which the requestor and target user were participants as buyer and seller.)
        """
        super(GetUserInputSet, self)._set_input('ItemID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetUserInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetUserInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetUserInputSet, self)._set_input('SiteID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The eBay User ID for the user whose data you want to retrieve.)
        """
        super(GetUserInputSet, self)._set_input('UserID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetUserInputSet, self)._set_input('UserToken', value)

class GetUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUserResultSet(response, path)
