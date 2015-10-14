# -*- coding: utf-8 -*-

###############################################################################
#
# GetComponents
# Returns imprint data associated with a given National Drug Code (NDC) in the DailyMed database.
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

class GetComponents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetComponents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetComponents, self).__init__(temboo_session, '/Library/DailyMed/GetComponents')


    def new_input_set(self):
        return GetComponentsInputSet()

    def _make_result_set(self, result, path):
        return GetComponentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetComponentsChoreographyExecution(session, exec_id, path)

class GetComponentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetComponents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_SetID(self, value):
        """
        Set the value of the SetID input for this Choreo. ((required, string) The unique ID assigned by DailyMed to each drug. You can find the SetID of a drug by first running the SearchByName or SearchByNDC Choreos.)
        """
        super(GetComponentsInputSet, self)._set_input('SetID', value)

class GetComponentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetComponents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from DailyMed.)
        """
        return self._output.get('Response', None)

class GetComponentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetComponentsResultSet(response, path)
