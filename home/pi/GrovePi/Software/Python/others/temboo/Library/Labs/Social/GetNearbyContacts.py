# -*- coding: utf-8 -*-

###############################################################################
#
# GetNearbyContacts
# Searches Foursquare recent check-ins and the Facebook social graph with a given set of Geo coordinates
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

class GetNearbyContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNearbyContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNearbyContacts, self).__init__(temboo_session, '/Library/Labs/Social/GetNearbyContacts')


    def new_input_set(self):
        return GetNearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return GetNearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNearbyContactsChoreographyExecution(session, exec_id, path)

class GetNearbyContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNearbyContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary containing Facebook and Foursquare credentials.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('APICredentials', value)
    def set_AfterTimestamp(self, value):
        """
        Set the value of the AfterTimestamp input for this Choreo. ((optional, date) Seconds after which to look for checkins, e.g. for looking for new checkins since the last fetch.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('AfterTimestamp', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of the location to search for.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the API responses.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude coordinate of the location to search for.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('Longitude', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through Facebook results. Returns results starting from the specified number.)
        """
        super(GetNearbyContactsInputSet, self)._set_input('Offset', value)

class GetNearbyContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNearbyContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) A merged result of Foursquare and Facebook location based searches.)
        """
        return self._output.get('Response', None)

class GetNearbyContactsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNearbyContactsResultSet(response, path)
