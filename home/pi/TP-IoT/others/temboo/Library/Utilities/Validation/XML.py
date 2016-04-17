# -*- coding: utf-8 -*-

###############################################################################
#
# XML
# Validates XML for basic well-formedness and allows you to check XML against a specified XSD schema file.
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

class XML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(XML, self).__init__(temboo_session, '/Library/Utilities/Validation/XML')


    def new_input_set(self):
        return XMLInputSet()

    def _make_result_set(self, result, path):
        return XMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLChoreographyExecution(session, exec_id, path)

class XMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XMLFile(self, value):
        """
        Set the value of the XMLFile input for this Choreo. ((required, xml) The XML file you want to validate.)
        """
        super(XMLInputSet, self)._set_input('XMLFile', value)
    def set_XSDFile(self, value):
        """
        Set the value of the XSDFile input for this Choreo. ((optional, xml) The XSD file to validate an XML file against.)
        """
        super(XMLInputSet, self)._set_input('XSDFile', value)

class XMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Error(self):
        """
        Retrieve the value for the "Error" output from this Choreo execution. ((string) The error description that is generated if a validation error occurs.)
        """
        return self._output.get('Error', None)
    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. ((string) The result of the validation. Returns the string "valid" or "invalid".)
        """
        return self._output.get('Result', None)

class XMLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return XMLResultSet(response, path)
