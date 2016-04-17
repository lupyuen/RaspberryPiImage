# -*- coding: utf-8 -*-

###############################################################################
#
# Role
# Returns terms held in office by Members of Congress and U.S. Presidents.
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

class Role(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Role Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Role, self).__init__(temboo_session, '/Library/GovTrack/Role')


    def new_input_set(self):
        return RoleInputSet()

    def _make_result_set(self, result, path):
        return RoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RoleChoreographyExecution(session, exec_id, path)

class RoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Role
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Current(self, value):
        """
        Set the value of the Current input for this Choreo. ((optional, string) Whether the role is currently held, or it is archival information. Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('Current', value)
    def set_District(self, value):
        """
        Set the value of the District input for this Choreo. ((optional, string) For representatives, the number of their congressional district. 0 for at-large districts, -1 in historical data if the district is not known. Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('District', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The date the role ended - when the person resigned, died, etc. (in YYYY-MM-DD format). Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('EndDate', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(RoleInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(RoleInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(RoleInputSet, self)._set_input('Offset', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) The political party of the person. If the person changes party, it is usually the most recent party during this role. Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('Party', value)
    def set_Person(self, value):
        """
        Set the value of the Person input for this Choreo. ((optional, string) The person associated with this role. When using this filter, provide the id of the person which is returned when requesting a single role object.)
        """
        super(RoleInputSet, self)._set_input('Person', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(RoleInputSet, self)._set_input('ResponseFormat', value)
    def set_RoleID(self, value):
        """
        Set the value of the RoleID input for this Choreo. ((optional, string) Specify the ID number of a role object to retrieve the record for only that role. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(RoleInputSet, self)._set_input('RoleID', value)
    def set_RoleType(self, value):
        """
        Set the value of the RoleType input for this Choreo. ((optional, string) The type of role (e.g. senator, representative, or president). Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('RoleType', value)
    def set_SenatorClass(self, value):
        """
        Set the value of the SenatorClass input for this Choreo. ((optional, integer) For senators, their election class, which determines which years they are up for election. Acceptable values: class1, class2, class3. Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('SenatorClass', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        super(RoleInputSet, self)._set_input('Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The date the role began  - when the person took office (in YYYY-MM-DD format). Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) For senators and representatives, the two-letter USPS abbreviation for the state or territory they are serving. Filter operators allowed. Sortable.)
        """
        super(RoleInputSet, self)._set_input('State', value)

class RoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Role Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class RoleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RoleResultSet(response, path)
