# -*- coding: utf-8 -*-

###############################################################################
#
# GetDateDifference
# Returns the difference between two specified dates, expressed as the number of milliseconds since January 1, 1970 (epoch time).
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

class GetDateDifference(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDateDifference Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDateDifference, self).__init__(temboo_session, '/Library/Utilities/Dates/GetDateDifference')


    def new_input_set(self):
        return GetDateDifferenceInputSet()

    def _make_result_set(self, result, path):
        return GetDateDifferenceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDateDifferenceChoreographyExecution(session, exec_id, path)

class GetDateDifferenceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDateDifference
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EarlierDate(self, value):
        """
        Set the value of the EarlierDate input for this Choreo. ((required, date) The earlier date to use for the date comparision (e.g., March 2, 2014).)
        """
        super(GetDateDifferenceInputSet, self)._set_input('EarlierDate', value)
    def set_LaterDate(self, value):
        """
        Set the value of the LaterDate input for this Choreo. ((required, date) The later date to use for the date comparision (e.g., March 3, 2014).)
        """
        super(GetDateDifferenceInputSet, self)._set_input('LaterDate', value)

class GetDateDifferenceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDateDifference Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Difference(self):
        """
        Retrieve the value for the "Difference" output from this Choreo execution. ((integer) The difference between two specified dates, expressed as the number of milliseconds since January 1, 1970 (epoch time). )
        """
        return self._output.get('Difference', None)

class GetDateDifferenceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDateDifferenceResultSet(response, path)
