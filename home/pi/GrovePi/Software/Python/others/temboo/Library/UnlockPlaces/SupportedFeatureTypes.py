# -*- coding: utf-8 -*-

###############################################################################
#
# SupportedFeatureTypes
# Retrieves a list of supported feature types that can be used in searches.
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

class SupportedFeatureTypes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SupportedFeatureTypes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SupportedFeatureTypes, self).__init__(temboo_session, '/Library/UnlockPlaces/SupportedFeatureTypes')


    def new_input_set(self):
        return SupportedFeatureTypesInputSet()

    def _make_result_set(self, result, path):
        return SupportedFeatureTypesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SupportedFeatureTypesChoreographyExecution(session, exec_id, path)

class SupportedFeatureTypesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SupportedFeatureTypes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        super(SupportedFeatureTypesInputSet, self)._set_input('Format', value)
    def set_Gazetteer(self, value):
        """
        Set the value of the Gazetteer input for this Choreo. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        super(SupportedFeatureTypesInputSet, self)._set_input('Gazetteer', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        super(SupportedFeatureTypesInputSet, self)._set_input('MaxRows', value)
    def set_StartRow(self, value):
        """
        Set the value of the StartRow input for this Choreo. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        super(SupportedFeatureTypesInputSet, self)._set_input('StartRow', value)

class SupportedFeatureTypesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SupportedFeatureTypes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        return self._output.get('Response', None)

class SupportedFeatureTypesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SupportedFeatureTypesResultSet(response, path)
