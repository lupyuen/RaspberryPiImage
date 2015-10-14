# -*- coding: utf-8 -*-

###############################################################################
#
# CommitteeMember
# Returns records indicating the current membership of a Member of Congress on a committee or subcommittee.
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

class CommitteeMember(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CommitteeMember Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CommitteeMember, self).__init__(temboo_session, '/Library/GovTrack/CommitteeMember')


    def new_input_set(self):
        return CommitteeMemberInputSet()

    def _make_result_set(self, result, path):
        return CommitteeMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeMemberChoreographyExecution(session, exec_id, path)

class CommitteeMemberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CommitteeMember
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CommitteeMemberID(self, value):
        """
        Set the value of the CommitteeMemberID input for this Choreo. ((optional, integer) The ID of the committee member resource. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(CommitteeMemberInputSet, self)._set_input('CommitteeMemberID', value)
    def set_Committee(self, value):
        """
        Set the value of the Committee input for this Choreo. ((optional, string) The committee or subcommittee being served on. To filter by this field, you can pass the ID of the committee. Filter operators allowed. Sortable.)
        """
        super(CommitteeMemberInputSet, self)._set_input('Committee', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(CommitteeMemberInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(CommitteeMemberInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(CommitteeMemberInputSet, self)._set_input('Offset', value)
    def set_Person(self, value):
        """
        Set the value of the Person input for this Choreo. ((optional, string) The ID of the Member of Congress serving on a committee. Filter operators allowed. Sortable.)
        """
        super(CommitteeMemberInputSet, self)._set_input('Person', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(CommitteeMemberInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of the variables that is listed as 'Sortable' in the description. Ex: '-lastname')
        """
        super(CommitteeMemberInputSet, self)._set_input('Sort', value)

class CommitteeMemberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CommitteeMember Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class CommitteeMemberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CommitteeMemberResultSet(response, path)
