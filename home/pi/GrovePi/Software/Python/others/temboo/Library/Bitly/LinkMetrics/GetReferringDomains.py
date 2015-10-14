# -*- coding: utf-8 -*-

###############################################################################
#
# GetReferringDomains
# Returns metrics about the domains referring click traffic to a single Bitly link.
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

class GetReferringDomains(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReferringDomains Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReferringDomains, self).__init__(temboo_session, '/Library/Bitly/LinkMetrics/GetReferringDomains')


    def new_input_set(self):
        return GetReferringDomainsInputSet()

    def _make_result_set(self, result, path):
        return GetReferringDomainsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReferringDomainsChoreographyExecution(session, exec_id, path)

class GetReferringDomainsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReferringDomains
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The OAuth access token provided by Bitly.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('AccessToken', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The result limit. Defaults to 100. Range is 1 to 1000.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('Limit', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((required, string) A Bitly link.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('Link', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(GetReferringDomainsInputSet, self)._set_input('ResponseFormat', value)
    def set_Rollup(self, value):
        """
        Set the value of the Rollup input for this Choreo. ((optional, boolean) Accepted values are true or false. When set to true, this returns data for multiple units rolled up to a single result instead of a separate value for each period of time.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('Rollup', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) An epoch timestamp, indicating the most recent time for which to pull metrics.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('Timestamp', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) An integer hour offset from UTC (-12..12), or a timezone string. Defaults to "America/New_York".)
        """
        super(GetReferringDomainsInputSet, self)._set_input('Timezone', value)
    def set_UnitName(self, value):
        """
        Set the value of the UnitName input for this Choreo. ((optional, string) The unit of time that corresponds to query you want to run. Accepted values are: minute, hour, day, week, month, and day. Defaults to "day".)
        """
        super(GetReferringDomainsInputSet, self)._set_input('UnitName', value)
    def set_UnitValue(self, value):
        """
        Set the value of the UnitValue input for this Choreo. ((optional, integer) An integer representing the amount of time to query for. Corresponds to the UnitName input. Defaults to -1 indicating to return all units of time.)
        """
        super(GetReferringDomainsInputSet, self)._set_input('UnitValue', value)

class GetReferringDomainsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReferringDomains Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetReferringDomainsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReferringDomainsResultSet(response, path)
