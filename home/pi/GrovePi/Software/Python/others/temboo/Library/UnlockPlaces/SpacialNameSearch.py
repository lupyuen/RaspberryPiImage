# -*- coding: utf-8 -*-

###############################################################################
#
# SpacialNameSearch
# Searches for names of places within a specified bounding box.
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

class SpacialNameSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SpacialNameSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SpacialNameSearch, self).__init__(temboo_session, '/Library/UnlockPlaces/SpacialNameSearch')


    def new_input_set(self):
        return SpacialNameSearchInputSet()

    def _make_result_set(self, result, path):
        return SpacialNameSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SpacialNameSearchChoreographyExecution(session, exec_id, path)

class SpacialNameSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SpacialNameSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        super(SpacialNameSearchInputSet, self)._set_input('Format', value)
    def set_Gazetteer(self, value):
        """
        Set the value of the Gazetteer input for this Choreo. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        super(SpacialNameSearchInputSet, self)._set_input('Gazetteer', value)
    def set_MaxLatitude(self, value):
        """
        Set the value of the MaxLatitude input for this Choreo. ((required, decimal) The maximum latitude point of a bounding box.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('MaxLatitude', value)
    def set_MaxLongitude(self, value):
        """
        Set the value of the MaxLongitude input for this Choreo. ((required, decimal) The maximum longitude point of a bounding box.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('MaxLongitude', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('MaxRows', value)
    def set_MinLatitude(self, value):
        """
        Set the value of the MinLatitude input for this Choreo. ((required, decimal) The minimum latitude point of a bounding box.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('MinLatitude', value)
    def set_MinLongitude(self, value):
        """
        Set the value of the MinLongitude input for this Choreo. ((required, decimal) The minimum longitude point of a bounding box.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('MinLongitude', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) One or more names of places to search for (separated by commas).)
        """
        super(SpacialNameSearchInputSet, self)._set_input('Name', value)
    def set_Operator(self, value):
        """
        Set the value of the Operator input for this Choreo. ((optional, any) Valid values are: "within" and "intersect". The results will therefore be entirely within, or overlapping with (intersecting), the bounding box. Defaults to "within".)
        """
        super(SpacialNameSearchInputSet, self)._set_input('Operator', value)
    def set_StartRow(self, value):
        """
        Set the value of the StartRow input for this Choreo. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        super(SpacialNameSearchInputSet, self)._set_input('StartRow', value)

class SpacialNameSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SpacialNameSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        return self._output.get('Response', None)

class SpacialNameSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SpacialNameSearchResultSet(response, path)
