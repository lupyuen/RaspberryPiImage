# -*- coding: utf-8 -*-

###############################################################################
#
# ChemActivityByFacility
# Retrieves a list of the type of manufacturing activity of toxic chemicals at any EPA-regulated facility.
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

class ChemActivityByFacility(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChemActivityByFacility Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ChemActivityByFacility, self).__init__(temboo_session, '/Library/EnviroFacts/Toxins/ChemActivityByFacility')


    def new_input_set(self):
        return ChemActivityByFacilityInputSet()

    def _make_result_set(self, result, path):
        return ChemActivityByFacilityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChemActivityByFacilityChoreographyExecution(session, exec_id, path)

class ChemActivityByFacilityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChemActivityByFacility
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FacilityID(self, value):
        """
        Set the value of the FacilityID input for this Choreo. ((required, string) FacilityID for which a toxin release report is to be generated. Found by first running the FacilitiesSearch Choreo.)
        """
        super(ChemActivityByFacilityInputSet, self)._set_input('FacilityID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the desired response format. Valid formats are: xml (the default) and csv.)
        """
        super(ChemActivityByFacilityInputSet, self)._set_input('ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        super(ChemActivityByFacilityInputSet, self)._set_input('RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        super(ChemActivityByFacilityInputSet, self)._set_input('RowStart', value)

class ChemActivityByFacilityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChemActivityByFacility Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class ChemActivityByFacilityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ChemActivityByFacilityResultSet(response, path)
