# -*- coding: utf-8 -*-

###############################################################################
#
# GetValuesFromXML
# Returns all element or attribute values with a specified name.
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

class GetValuesFromXML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetValuesFromXML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetValuesFromXML, self).__init__(temboo_session, '/Library/Utilities/XML/GetValuesFromXML')


    def new_input_set(self):
        return GetValuesFromXMLInputSet()

    def _make_result_set(self, result, path):
        return GetValuesFromXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetValuesFromXMLChoreographyExecution(session, exec_id, path)

class GetValuesFromXMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetValuesFromXML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Node(self, value):
        """
        Set the value of the Node input for this Choreo. ((required, string) The name of the element or attribute that contains the values you want to return. Note that attribute names should be preceded with an "@" sign (e.g. @name).)
        """
        super(GetValuesFromXMLInputSet, self)._set_input('Node', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json or csv.)
        """
        super(GetValuesFromXMLInputSet, self)._set_input('ResponseFormat', value)
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML that contains the elements or attributes you want to retrieve.)
        """
        super(GetValuesFromXMLInputSet, self)._set_input('XML', value)

class GetValuesFromXMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetValuesFromXML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. (The element or attribute values.)
        """
        return self._output.get('Result', None)

class GetValuesFromXMLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetValuesFromXMLResultSet(response, path)
