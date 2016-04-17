# -*- coding: utf-8 -*-

###############################################################################
#
# TSVToXML
# Converts a TSV formatted file to XML.
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

class TSVToXML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TSVToXML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TSVToXML, self).__init__(temboo_session, '/Library/Utilities/DataConversions/TSVToXML')


    def new_input_set(self):
        return TSVToXMLInputSet()

    def _make_result_set(self, result, path):
        return TSVToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TSVToXMLChoreographyExecution(session, exec_id, path)

class TSVToXMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TSVToXML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_TSV(self, value):
        """
        Set the value of the TSV input for this Choreo. ((required, multiline) The TSV file to convert to XML. Your TSV data must contain column names.)
        """
        super(TSVToXMLInputSet, self)._set_input('TSV', value)

class TSVToXMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TSVToXML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_XML(self):
        """
        Retrieve the value for the "XML" output from this Choreo execution. ((xml) The XML formatted data.)
        """
        return self._output.get('XML', None)

class TSVToXMLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TSVToXMLResultSet(response, path)
