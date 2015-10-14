# -*- coding: utf-8 -*-

###############################################################################
#
# CandidateLeadersByCategory
# Retrieve a list of the 20 top candidates in terms of contributions received.
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

class CandidateLeadersByCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CandidateLeadersByCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CandidateLeadersByCategory, self).__init__(temboo_session, '/Library/NYTimes/CampaignFinance/Candidates/CandidateLeadersByCategory')


    def new_input_set(self):
        return CandidateLeadersByCategoryInputSet()

    def _make_result_set(self, result, path):
        return CandidateLeadersByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CandidateLeadersByCategoryChoreographyExecution(session, exec_id, path)

class CandidateLeadersByCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CandidateLeadersByCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(CandidateLeadersByCategoryInputSet, self)._set_input('APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        super(CandidateLeadersByCategoryInputSet, self)._set_input('CampaignCycle', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) Specify thecategory to be retrieved. Example: contribution-total, returns the total amount of financial contributions received by this candidate's campaign.  See Description for more info.)
        """
        super(CandidateLeadersByCategoryInputSet, self)._set_input('Category', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        super(CandidateLeadersByCategoryInputSet, self)._set_input('ResponseFormat', value)

class CandidateLeadersByCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CandidateLeadersByCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class CandidateLeadersByCategoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CandidateLeadersByCategoryResultSet(response, path)
