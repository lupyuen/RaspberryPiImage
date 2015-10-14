# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToXLS
# Converts an XML file to a Base64 encoded Excel file.
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

class XMLToXLS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToXLS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(XMLToXLS, self).__init__(temboo_session, '/Library/Utilities/DataConversions/XMLToXLS')


    def new_input_set(self):
        return XMLToXLSInputSet()

    def _make_result_set(self, result, path):
        return XMLToXLSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToXLSChoreographyExecution(session, exec_id, path)

class XMLToXLSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToXLS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file you want to convert to XLS format. See documentation for information on the required XML schema.)
        """
        super(XMLToXLSInputSet, self)._set_input('XML', value)

class XMLToXLSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToXLS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_XLS(self):
        """
        Retrieve the value for the "XLS" output from this Choreo execution. (The Base64 encoded Excel data .)
        """
        return self._output.get('XLS', None)

class XMLToXLSChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return XMLToXLSResultSet(response, path)
