# -*- coding: utf-8 -*-

###############################################################################
#
# ByFoursquare
# Retrieves information from multiple APIs about places near a set of coordinates retrieved from Foursquare.
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

class ByFoursquare(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByFoursquare Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ByFoursquare, self).__init__(temboo_session, '/Library/Labs/GetPlaces/ByFoursquare')


    def new_input_set(self):
        return ByFoursquareInputSet()

    def _make_result_set(self, result, path):
        return ByFoursquareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByFoursquareChoreographyExecution(session, exec_id, path)

class ByFoursquareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByFoursquare
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        super(ByFoursquareInputSet, self)._set_input('APICredentials', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of Foursquare venues returned.)
        """
        super(ByFoursquareInputSet, self)._set_input('Limit', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) This keyword input can be used to narrow search results for Google Places and Foursquare.)
        """
        super(ByFoursquareInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are json (the default) and xml.)
        """
        super(ByFoursquareInputSet, self)._set_input('ResponseFormat', value)
    def set_Shout(self, value):
        """
        Set the value of the Shout input for this Choreo. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        super(ByFoursquareInputSet, self)._set_input('Shout', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Filters results by type of place, such as: bar, dentist, etc. This is used to filter results for Google Places and Yelp.)
        """
        super(ByFoursquareInputSet, self)._set_input('Type', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((optional, string) The venue where the user is checking in. Required if creating a Foursquare checkin.)
        """
        super(ByFoursquareInputSet, self)._set_input('VenueID', value)

class ByFoursquareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByFoursquare Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains weather information based on the coordinates returned from the Foursquare checkin.)
        """
        return self._output.get('Response', None)

class ByFoursquareChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ByFoursquareResultSet(response, path)
