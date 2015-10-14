# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns a list of legislators that meet a specified search criteria.
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

class GetList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetList, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

class GetListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetListInputSet, self)._set_input('APIKey', value)
    def set_AllLegislators(self, value):
        """
        Set the value of the AllLegislators input for this Choreo. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        super(GetListInputSet, self)._set_input('AllLegislators', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) The bioguide_id of the legislator to return.)
        """
        super(GetListInputSet, self)._set_input('BioguideID', value)
    def set_CRPID(self, value):
        """
        Set the value of the CRPID input for this Choreo. ((optional, string) The crp_id associated with a legislator to return.)
        """
        super(GetListInputSet, self)._set_input('CRPID', value)
    def set_District(self, value):
        """
        Set the value of the District input for this Choreo. ((optional, integer) Narrows the search result by district number.)
        """
        super(GetListInputSet, self)._set_input('District', value)
    def set_FECID(self, value):
        """
        Set the value of the FECID input for this Choreo. ((optional, string) The fec_id associated with the legislator to return.)
        """
        super(GetListInputSet, self)._set_input('FECID', value)
    def set_FacebookID(self, value):
        """
        Set the value of the FacebookID input for this Choreo. ((optional, string) The facebook id of a legislator to return.)
        """
        super(GetListInputSet, self)._set_input('FacebookID', value)
    def set_Filters(self, value):
        """
        Set the value of the Filters input for this Choreo. ((optional, json) A JSON object containing key/value pairs to be used as filters.)
        """
        super(GetListInputSet, self)._set_input('Filters', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of a legislator to return.)
        """
        super(GetListInputSet, self)._set_input('FirstName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) Narrows the search result by gender.)
        """
        super(GetListInputSet, self)._set_input('Gender', value)
    def set_GovTrackID(self, value):
        """
        Set the value of the GovTrackID input for this Choreo. ((optional, string) The govetrack_id associated with a legistlator to return.)
        """
        super(GetListInputSet, self)._set_input('GovTrackID', value)
    def set_InOffice(self, value):
        """
        Set the value of the InOffice input for this Choreo. ((optional, boolean) Whether or not the individual is in office currently. Valid values are true or false.)
        """
        super(GetListInputSet, self)._set_input('InOffice', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the legislator to return.)
        """
        super(GetListInputSet, self)._set_input('LastName', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Used to order the results by field name (e.g. field__asc).)
        """
        super(GetListInputSet, self)._set_input('Order', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page offset.)
        """
        super(GetListInputSet, self)._set_input('Page', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Narrows the search result by party (i.e. "D" or "R").)
        """
        super(GetListInputSet, self)._set_input('Party', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page.)
        """
        super(GetListInputSet, self)._set_input('PerPage', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search term.)
        """
        super(GetListInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetListInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) A state abbreviation to narrow the search results.)
        """
        super(GetListInputSet, self)._set_input('State', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title associated with the individual to return.)
        """
        super(GetListInputSet, self)._set_input('Title', value)
    def set_TwitterID(self, value):
        """
        Set the value of the TwitterID input for this Choreo. ((optional, string) The twitter id of the legislator to return (note, this can be a twitter screen name).)
        """
        super(GetListInputSet, self)._set_input('TwitterID', value)
    def set_VoteSmartID(self, value):
        """
        Set the value of the VoteSmartID input for this Choreo. ((optional, integer) The votesmart_id of a legislator to return.)
        """
        super(GetListInputSet, self)._set_input('VoteSmartID', value)

class GetListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
