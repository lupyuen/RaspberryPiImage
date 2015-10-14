# -*- coding: utf-8 -*-

###############################################################################
#
# Dates
# Returns the popularity of a given phrase in the Congressional Record over time.
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

class Dates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Dates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Dates, self).__init__(temboo_session, '/Library/SunlightLabs/CapitolWords/Dates')


    def new_input_set(self):
        return DatesInputSet()

    def _make_result_set(self, result, path):
        return DatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DatesChoreographyExecution(session, exec_id, path)

class DatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Dates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(DatesInputSet, self)._set_input('APIKey', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) Limit results to the member of Congress with the given Bioguide ID. The Bioguide ID of any current or past congressional member can be found at bioguide.congress.gov.)
        """
        super(DatesInputSet, self)._set_input('BioguideID', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        super(DatesInputSet, self)._set_input('Chamber', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        super(DatesInputSet, self)._set_input('Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        super(DatesInputSet, self)._set_input('EndDate', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) The length of time covered by each result. Valid values: year, month, day. Defaults to day.)
        """
        super(DatesInputSet, self)._set_input('Granularity', value)
    def set_MinCount(self, value):
        """
        Set the value of the MinCount input for this Choreo. ((optional, boolean) Only returns results where mentions are at or above the supplied threshold.)
        """
        super(DatesInputSet, self)._set_input('MinCount', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        super(DatesInputSet, self)._set_input('Party', value)
    def set_Percentages(self, value):
        """
        Set the value of the Percentages input for this Choreo. ((optional, string) Include the percentage of mentions versus total words in the result objects. Valid values: true, false. Defaults to false.)
        """
        super(DatesInputSet, self)._set_input('Percentages', value)
    def set_Phrase(self, value):
        """
        Set the value of the Phrase input for this Choreo. ((required, string) The phrase to search for.)
        """
        super(DatesInputSet, self)._set_input('Phrase', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        super(DatesInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        super(DatesInputSet, self)._set_input('StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        super(DatesInputSet, self)._set_input('State', value)

class DatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Dates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CapitolWords.)
        """
        return self._output.get('Response', None)

class DatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DatesResultSet(response, path)
