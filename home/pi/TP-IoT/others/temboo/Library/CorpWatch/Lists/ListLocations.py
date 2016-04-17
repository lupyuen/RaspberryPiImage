# -*- coding: utf-8 -*-

###############################################################################
#
# ListLocations
# Returns a list of locations of companies matching the given query.
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

class ListLocations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListLocations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListLocations, self).__init__(temboo_session, '/Library/CorpWatch/Lists/ListLocations')


    def new_input_set(self):
        return ListLocationsInputSet()

    def _make_result_set(self, result, path):
        return ListLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListLocationsChoreographyExecution(session, exec_id, path)

class ListLocationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListLocations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(ListLocationsInputSet, self)._set_input('APIKey', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) Enter an address fragment to search for. This can be either a street address, city, or state/subregion.)
        """
        super(ListLocationsInputSet, self)._set_input('Address', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) Enter an ISO-3166 formatted country code. )
        """
        super(ListLocationsInputSet, self)._set_input('CountryCode', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(ListLocationsInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(ListLocationsInputSet, self)._set_input('Limit', value)
    def set_MaxYear(self, value):
        """
        Set the value of the MaxYear input for this Choreo. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        super(ListLocationsInputSet, self)._set_input('MaxYear', value)
    def set_MinYear(self, value):
        """
        Set the value of the MinYear input for this Choreo. ((optional, integer) Indicate desired year of the earliest appearance in SEC filing data (e.g. indicating 2004 will search for companies that started filing in 2004).)
        """
        super(ListLocationsInputSet, self)._set_input('MinYear', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((optional, integer) Enter a postal code to be searched.)
        """
        super(ListLocationsInputSet, self)._set_input('PostalCode', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(ListLocationsInputSet, self)._set_input('ResponseType', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Indicates the origin of the location information found. Acceptable values: relation_loc, business, mailing, state_of_incorp. See documentation for more info.)
        """
        super(ListLocationsInputSet, self)._set_input('Type', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        super(ListLocationsInputSet, self)._set_input('Year', value)

class ListLocationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListLocations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class ListLocationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListLocationsResultSet(response, path)
