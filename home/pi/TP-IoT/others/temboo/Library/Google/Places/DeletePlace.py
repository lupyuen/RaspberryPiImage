# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePlace
# Delete a new Place from Google Places.
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

class DeletePlace(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePlace Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeletePlace, self).__init__(temboo_session, '/Library/Google/Places/DeletePlace')


    def new_input_set(self):
        return DeletePlaceInputSet()

    def _make_result_set(self, result, path):
        return DeletePlaceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePlaceChoreographyExecution(session, exec_id, path)

class DeletePlaceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePlace
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The API Key provided by Google.)
        """
        super(DeletePlaceInputSet, self)._set_input('Key', value)
    def set_PlaceID(self, value):
        """
        Set the value of the PlaceID input for this Choreo. ((conditional, string) A textual identifier that uniquely identifies a place.)
        """
        super(DeletePlaceInputSet, self)._set_input('PlaceID', value)
    def set_PlaceReference(self, value):
        """
        Set the value of the PlaceReference input for this Choreo. ((optional, string) A textual identifier that uniquely identifies a place. Note, this parameter is deprecated as of June 24, 2014. Use PlaceID instead.)
        """
        super(DeletePlaceInputSet, self)._set_input('PlaceReference', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DeletePlaceInputSet, self)._set_input('ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(DeletePlaceInputSet, self)._set_input('Sensor', value)

class DeletePlaceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePlace Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class DeletePlaceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeletePlaceResultSet(response, path)
