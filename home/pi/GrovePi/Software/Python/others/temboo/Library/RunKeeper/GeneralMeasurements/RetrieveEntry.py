# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveEntry
# Retrieves a body measurement entry from a user's feed.
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

class RetrieveEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveEntry, self).__init__(temboo_session, '/Library/RunKeeper/GeneralMeasurements/RetrieveEntry')


    def new_input_set(self):
        return RetrieveEntryInputSet()

    def _make_result_set(self, result, path):
        return RetrieveEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveEntryChoreographyExecution(session, exec_id, path)

class RetrieveEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(RetrieveEntryInputSet, self)._set_input('AccessToken', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, string) This can be the individual id of the body measurement entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /generalMeasurements/24220709).)
        """
        super(RetrieveEntryInputSet, self)._set_input('EntryID', value)

class RetrieveEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveEntryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveEntryResultSet(response, path)
