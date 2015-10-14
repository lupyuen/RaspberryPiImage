# -*- coding: utf-8 -*-

###############################################################################
#
# VoteAndVoter
# Retrieves how people voted on roll call votes in the U.S. Congress since 1789. 
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

class VoteAndVoter(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VoteAndVoter Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VoteAndVoter, self).__init__(temboo_session, '/Library/GovTrack/VoteAndVoter')


    def new_input_set(self):
        return VoteAndVoterInputSet()

    def _make_result_set(self, result, path):
        return VoteAndVoterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteAndVoterChoreographyExecution(session, exec_id, path)

class VoteAndVoterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VoteAndVoter
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, string) The date (and in recent history also the time) on which the vote was held (in YYYY-MM-DD format). Filter operators allowed. Sortable.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Created', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(VoteAndVoterInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Limit', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((optional, integer) The ID of the resource to retrieve. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(VoteAndVoterInputSet, self)._set_input('ObjectID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Offset', value)
    def set_Option(self, value):
        """
        Set the value of the Option input for this Choreo. ((optional, string) The way a particular person voted. The value corresponds to the key of an option returned on the Vote Choreo. Filter operators allowed. Sortable.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Option', value)
    def set_Person(self, value):
        """
        Set the value of the Person input for this Choreo. ((optional, string) The person making this vote. This is an ID number. Filter operators allowed. Sortable.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Person', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(VoteAndVoterInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Sort', value)
    def set_Vote(self, value):
        """
        Set the value of the Vote input for this Choreo. ((optional, string) The ID number of the vote that this was part of. This is in the form of an ID number. Filter operators allowed. Sortable.)
        """
        super(VoteAndVoterInputSet, self)._set_input('Vote', value)

class VoteAndVoterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VoteAndVoter Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class VoteAndVoterChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VoteAndVoterResultSet(response, path)
