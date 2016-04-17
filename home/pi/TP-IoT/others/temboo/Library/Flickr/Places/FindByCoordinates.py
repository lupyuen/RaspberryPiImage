# -*- coding: utf-8 -*-

###############################################################################
#
# FindByCoordinates
# Returns a place ID for a given latitude, longitude and accuracy.
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

class FindByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindByCoordinates, self).__init__(temboo_session, '/Library/Flickr/Places/FindByCoordinates')


    def new_input_set(self):
        return FindByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByCoordinatesChoreographyExecution(session, exec_id, path)

class FindByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(FindByCoordinatesInputSet, self)._set_input('APIKey', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) Recorded accuracy level of the location information. Valid range is 1-16. The default is 16.)
        """
        super(FindByCoordinatesInputSet, self)._set_input('Accuracy', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 4 decimal places will be truncated.)
        """
        super(FindByCoordinatesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 4 decimal places will be truncated.)
        """
        super(FindByCoordinatesInputSet, self)._set_input('Longitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) )
        """
        super(FindByCoordinatesInputSet, self)._set_input('ResponseFormat', value)

class FindByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class FindByCoordinatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindByCoordinatesResultSet(response, path)
