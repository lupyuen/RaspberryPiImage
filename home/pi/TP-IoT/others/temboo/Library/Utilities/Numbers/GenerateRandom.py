# -*- coding: utf-8 -*-

###############################################################################
#
# GenerateRandom
# This choreo generates a random number in a variety of ranges. 
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

class GenerateRandom(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GenerateRandom Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GenerateRandom, self).__init__(temboo_session, '/Library/Utilities/Numbers/GenerateRandom')


    def new_input_set(self):
        return GenerateRandomInputSet()

    def _make_result_set(self, result, path):
        return GenerateRandomResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GenerateRandomChoreographyExecution(session, exec_id, path)

class GenerateRandomInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GenerateRandom
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    pass

class GenerateRandomResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GenerateRandom Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_SignedDecimal(self):
        """
        Retrieve the value for the "SignedDecimal" output from this Choreo execution. ((decimal) Signed Decimal in the range of  -0.5 to +0.5.)
        """
        return self._output.get('SignedDecimal', None)
    def get_SignedInteger(self):
        """
        Retrieve the value for the "SignedInteger" output from this Choreo execution. ((integer) SIgned Integer in the range of -2147483648 through 2147483647.)
        """
        return self._output.get('SignedInteger', None)
    def get_UnsignedDecimal(self):
        """
        Retrieve the value for the "UnsignedDecimal" output from this Choreo execution. ((decimal) Unsigned Decimal in the range of 0.0 to 1.0.)
        """
        return self._output.get('UnsignedDecimal', None)
    def get_UnsignedInteger(self):
        """
        Retrieve the value for the "UnsignedInteger" output from this Choreo execution. ((integer) Unsigned integer in the range of 0 through 4294967295.)
        """
        return self._output.get('UnsignedInteger', None)

class GenerateRandomChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GenerateRandomResultSet(response, path)
