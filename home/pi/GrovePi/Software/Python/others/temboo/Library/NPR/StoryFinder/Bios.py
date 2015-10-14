# -*- coding: utf-8 -*-

###############################################################################
#
# Bios
# Retrieves a list of NPR personalities and corresponding IDs. Also used to look up the IDs of specific NPR personalities by specifying them as an optional parameter.
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

class Bios(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Bios Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Bios, self).__init__(temboo_session, '/Library/NPR/StoryFinder/Bios')


    def new_input_set(self):
        return BiosInputSet()

    def _make_result_set(self, result, path):
        return BiosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BiosChoreographyExecution(session, exec_id, path)

class BiosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Bios
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Personality(self, value):
        """
        Set the value of the Personality input for this Choreo. ((optional, string) The specific name or an NPR personality to return. Multiple names can be specified separated by commas (i.e. Andrei Codrescu,Allison Keyes). Personality IDs are returned when this input is used.)
        """
        super(BiosInputSet, self)._set_input('Personality', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are xml (the default), and json.)
        """
        super(BiosInputSet, self)._set_input('ResponseFormat', value)
    def set_StoryCountAll(self, value):
        """
        Set the value of the StoryCountAll input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        super(BiosInputSet, self)._set_input('StoryCountAll', value)
    def set_StoryCountMonth(self, value):
        """
        Set the value of the StoryCountMonth input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        super(BiosInputSet, self)._set_input('StoryCountMonth', value)
    def set_StoryCountToday(self, value):
        """
        Set the value of the StoryCountToday input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        super(BiosInputSet, self)._set_input('StoryCountToday', value)

class BiosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Bios Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the personality specified. This is only returned when the Personality input is specified. When personalities are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)

class BiosChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BiosResultSet(response, path)
