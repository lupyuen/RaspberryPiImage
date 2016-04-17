# -*- coding: utf-8 -*-

###############################################################################
#
# CommitteeContributions
# Obtain contributions made by a Political Action Committee (PAC) in an election cycle.
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

class CommitteeContributions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CommitteeContributions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CommitteeContributions, self).__init__(temboo_session, '/Library/NYTimes/CampaignFinance/Committees/CommitteeContributions')


    def new_input_set(self):
        return CommitteeContributionsInputSet()

    def _make_result_set(self, result, path):
        return CommitteeContributionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeContributionsChoreographyExecution(session, exec_id, path)

class CommitteeContributionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CommitteeContributions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(CommitteeContributionsInputSet, self)._set_input('APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        super(CommitteeContributionsInputSet, self)._set_input('CampaignCycle', value)
    def set_CommitteeFECID(self, value):
        """
        Set the value of the CommitteeFECID input for this Choreo. ((conditional, string) Enter a political action committee's FEC ID.  Either CommitteeFECID, OR Name must be provided.)
        """
        super(CommitteeContributionsInputSet, self)._set_input('CommitteeFECID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) Enter the name of a political action committee (PAC) whose contributions will be obtained. Either Name or CommitteeFECID must be provided.)
        """
        super(CommitteeContributionsInputSet, self)._set_input('Name', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value (e.g., Offset=40 displays results 41–60).)
        """
        super(CommitteeContributionsInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        super(CommitteeContributionsInputSet, self)._set_input('ResponseFormat', value)

class CommitteeContributionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CommitteeContributions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class CommitteeContributionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CommitteeContributionsResultSet(response, path)
