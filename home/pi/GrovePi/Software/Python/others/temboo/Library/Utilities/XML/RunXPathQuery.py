# -*- coding: utf-8 -*-

###############################################################################
#
# RunXPathQuery
# Executes an XPath query against a specified XML file and returns the result in CSV or JSON format.
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

class RunXPathQuery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunXPathQuery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RunXPathQuery, self).__init__(temboo_session, '/Library/Utilities/XML/RunXPathQuery')


    def new_input_set(self):
        return RunXPathQueryInputSet()

    def _make_result_set(self, result, path):
        return RunXPathQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunXPathQueryChoreographyExecution(session, exec_id, path)

class RunXPathQueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunXPathQuery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((conditional, string) Valid values are "select" (the default) or "recursive". Recursive mode will iterate using the provided XPath. Select mode will return the first match if there are multiple rows in the XML provided.)
        """
        super(RunXPathQueryInputSet, self)._set_input('Mode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json or csv.)
        """
        super(RunXPathQueryInputSet, self)._set_input('ResponseFormat', value)
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML that contains the elements or attributes you want to retrieve.)
        """
        super(RunXPathQueryInputSet, self)._set_input('XML', value)
    def set_XPath(self, value):
        """
        Set the value of the XPath input for this Choreo. ((required, string) The XPath query to run.)
        """
        super(RunXPathQueryInputSet, self)._set_input('XPath', value)

class RunXPathQueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunXPathQuery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. (The XPath query result.)
        """
        return self._output.get('Result', None)

class RunXPathQueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RunXPathQueryResultSet(response, path)
