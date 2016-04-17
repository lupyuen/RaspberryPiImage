# -*- coding: utf-8 -*-

###############################################################################
#
# CSVToJSON
# Converts a CSV formatted file to JSON.
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

class CSVToJSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CSVToJSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CSVToJSON, self).__init__(temboo_session, '/Library/Utilities/DataConversions/CSVToJSON')


    def new_input_set(self):
        return CSVToJSONInputSet()

    def _make_result_set(self, result, path):
        return CSVToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CSVToJSONChoreographyExecution(session, exec_id, path)

class CSVToJSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CSVToJSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSV(self, value):
        """
        Set the value of the CSV input for this Choreo. ((required, multiline) The CSV file to convert to JSON. Your CSV data must contain column names.)
        """
        super(CSVToJSONInputSet, self)._set_input('CSV', value)

class CSVToJSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CSVToJSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_JSON(self):
        """
        Retrieve the value for the "JSON" output from this Choreo execution. ((json) The JSON formatted data.)
        """
        return self._output.get('JSON', None)

class CSVToJSONChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CSVToJSONResultSet(response, path)
