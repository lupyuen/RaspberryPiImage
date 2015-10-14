# -*- coding: utf-8 -*-

###############################################################################
#
# FacilitiesSearchByZip
# Retrieves a list of EPA-regulated facilities in the Toxics Release Inventory (TRI) database within a given area code.
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

class FacilitiesSearchByZip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FacilitiesSearchByZip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FacilitiesSearchByZip, self).__init__(temboo_session, '/Library/EnviroFacts/Toxins/FacilitiesSearchByZip')


    def new_input_set(self):
        return FacilitiesSearchByZipInputSet()

    def _make_result_set(self, result, path):
        return FacilitiesSearchByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FacilitiesSearchByZipChoreographyExecution(session, exec_id, path)

class FacilitiesSearchByZipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FacilitiesSearchByZip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the desired response format. Valid formats are: xml (the default) and csv.)
        """
        super(FacilitiesSearchByZipInputSet, self)._set_input('ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        super(FacilitiesSearchByZipInputSet, self)._set_input('RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        super(FacilitiesSearchByZipInputSet, self)._set_input('RowStart', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) Zip code to be searched.)
        """
        super(FacilitiesSearchByZipInputSet, self)._set_input('Zip', value)

class FacilitiesSearchByZipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FacilitiesSearchByZip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class FacilitiesSearchByZipChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FacilitiesSearchByZipResultSet(response, path)
