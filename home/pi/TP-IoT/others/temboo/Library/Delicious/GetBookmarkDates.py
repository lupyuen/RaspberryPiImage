# -*- coding: utf-8 -*-

###############################################################################
#
# GetBookmarkDates
# Retrieve a list of dates, with the number of bookmarks posted for each date.
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

class GetBookmarkDates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBookmarkDates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBookmarkDates, self).__init__(temboo_session, '/Library/Delicious/GetBookmarkDates')


    def new_input_set(self):
        return GetBookmarkDatesInputSet()

    def _make_result_set(self, result, path):
        return GetBookmarkDatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBookmarkDatesChoreographyExecution(session, exec_id, path)

class GetBookmarkDatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBookmarkDates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        super(GetBookmarkDatesInputSet, self)._set_input('Password', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Return only items tagged with the specified keyword.)
        """
        super(GetBookmarkDatesInputSet, self)._set_input('Tags', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        super(GetBookmarkDatesInputSet, self)._set_input('Username', value)

class GetBookmarkDatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBookmarkDates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetBookmarkDatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBookmarkDatesResultSet(response, path)
