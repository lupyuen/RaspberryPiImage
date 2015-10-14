# -*- coding: utf-8 -*-

###############################################################################
#
# CSVToXLS
# Converts a CSV formatted file to Base64 encoded Excel data.
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

class CSVToXLS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CSVToXLS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CSVToXLS, self).__init__(temboo_session, '/Library/Utilities/DataConversions/CSVToXLS')


    def new_input_set(self):
        return CSVToXLSInputSet()

    def _make_result_set(self, result, path):
        return CSVToXLSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CSVToXLSChoreographyExecution(session, exec_id, path)

class CSVToXLSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CSVToXLS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSV(self, value):
        """
        Set the value of the CSV input for this Choreo. ((conditional, multiline) The CSV data you want to convert to XLS format. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        super(CSVToXLSInputSet, self)._set_input('CSV', value)


class CSVToXLSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CSVToXLS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_XLS(self):
        """
        Retrieve the value for the "XLS" output from this Choreo execution. ((string) The Base64 encoded Excel data.)
        """
        return self._output.get('XLS', None)

class CSVToXLSChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CSVToXLSResultSet(response, path)
