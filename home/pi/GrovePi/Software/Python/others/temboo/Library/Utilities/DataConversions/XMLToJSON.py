# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToJSON
# Converts data from XML format to JSON format.
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

class XMLToJSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToJSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(XMLToJSON, self).__init__(temboo_session, '/Library/Utilities/DataConversions/XMLToJSON')


    def new_input_set(self):
        return XMLToJSONInputSet()

    def _make_result_set(self, result, path):
        return XMLToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToJSONChoreographyExecution(session, exec_id, path)

class XMLToJSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToJSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file that you want to convert to JSON format.)
        """
        super(XMLToJSONInputSet, self)._set_input('XML', value)

class XMLToJSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToJSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_JSON(self):
        """
        Retrieve the value for the "JSON" output from this Choreo execution. ((json) The converted data in JSON format.)
        """
        return self._output.get('JSON', None)

class XMLToJSONChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return XMLToJSONResultSet(response, path)
