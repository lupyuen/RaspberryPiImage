# -*- coding: utf-8 -*-

###############################################################################
#
# Vote
# Returns roll call votes in the U.S. Congress since 1789.
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

class Vote(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Vote Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Vote, self).__init__(temboo_session, '/Library/GovTrack/Vote')


    def new_input_set(self):
        return VoteInputSet()

    def _make_result_set(self, result, path):
        return VoteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteChoreographyExecution(session, exec_id, path)

class VoteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Vote
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) The chamber in which the vote was held. Valid values are: house or senate. Filter operators allowed but only when filtering by Congress as well. Sortable.)
        """
        super(VoteInputSet, self)._set_input('Chamber', value)
    def set_Congress(self, value):
        """
        Set the value of the Congress input for this Choreo. ((optional, string) The number of the congress in which the vote took place. The current congress is 113. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('Congress', value)
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, string) The date (and in recent history also the time) on which the vote was held. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('Created', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(VoteInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(VoteInputSet, self)._set_input('Limit', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, string) The number of the vote, unique to a Congress and session pair. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('Number', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(VoteInputSet, self)._set_input('Offset', value)
    def set_RelatedAmendment(self, value):
        """
        Set the value of the RelatedAmendment input for this Choreo. ((optional, string) The ID of a related amendment. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('RelatedAmendment', value)
    def set_RelatedBill(self, value):
        """
        Set the value of the RelatedBill input for this Choreo. ((optional, string) A bill related to this vote. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('RelatedBill', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(VoteInputSet, self)._set_input('ResponseFormat', value)
    def set_Session(self, value):
        """
        Set the value of the Session input for this Choreo. ((optional, string) The session of congress. Filter operators allowed. Sortable.)
        """
        super(VoteInputSet, self)._set_input('Session', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using created (ascending) or -created (descending) for the dates that each vote was held.)
        """
        super(VoteInputSet, self)._set_input('Sort', value)
    def set_VoteID(self, value):
        """
        Set the value of the VoteID input for this Choreo. ((optional, integer) The ID of a vote object to retrieve. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(VoteInputSet, self)._set_input('VoteID', value)

class VoteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Vote Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class VoteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VoteResultSet(response, path)
