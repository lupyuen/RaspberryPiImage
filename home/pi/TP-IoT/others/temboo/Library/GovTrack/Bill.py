# -*- coding: utf-8 -*-

###############################################################################
#
# Bill
# Retrieves bills and resolutions in the U.S. Congress since 1973 (the 93rd Congress).
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

class Bill(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Bill Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Bill, self).__init__(temboo_session, '/Library/GovTrack/Bill')


    def new_input_set(self):
        return BillInputSet()

    def _make_result_set(self, result, path):
        return BillResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BillChoreographyExecution(session, exec_id, path)

class BillInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Bill
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BillID(self, value):
        """
        Set the value of the BillID input for this Choreo. ((optional, integer) The ID number of the bill to retrieve. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(BillInputSet, self)._set_input('BillID', value)
    def set_BillType(self, value):
        """
        Set the value of the BillType input for this Choreo. ((optional, string) The bill's type (e.g. house_resolution, senate_bill, house_bill, etc). Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('BillType', value)
    def set_CoSponsors(self, value):
        """
        Set the value of the CoSponsors input for this Choreo. ((optional, string) The bill's cosponsors. When using this filter, provide the id of the cosponsor which is returned when requesting a single bill object. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('CoSponsors', value)
    def set_Committees(self, value):
        """
        Set the value of the Committees input for this Choreo. ((optional, string) Committees to which the bill has been referred. When using this filter, provide the id of the committee which is returned when requesting a single bill object. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('Committees', value)
    def set_Congress(self, value):
        """
        Set the value of the Congress input for this Choreo. ((optional, string) The number of the congress in which the bill was introduced. The current congress is 113. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('Congress', value)
    def set_CurrentStatusDate(self, value):
        """
        Set the value of the CurrentStatusDate input for this Choreo. ((optional, string) The date of the last major action on the bill corresponding to the CurrentStatus (in YYYY-MM-DD format). Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('CurrentStatusDate', value)
    def set_CurrentStatus(self, value):
        """
        Set the value of the CurrentStatus input for this Choreo. ((optional, string) The current status of the bill (e.g. passed_bill, prov_kill_veto, introduced, etc). Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('CurrentStatus', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(BillInputSet, self)._set_input('Fields', value)
    def set_IntroducedDate(self, value):
        """
        Set the value of the IntroducedDate input for this Choreo. ((optional, string) The date the bill was introduced (in YYYY-MM-DD format). Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('IntroducedDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(BillInputSet, self)._set_input('Limit', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, string) The bill's number. This is different from the BillID. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('Number', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(BillInputSet, self)._set_input('Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) Filters according to a full-text search on the object.)
        """
        super(BillInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(BillInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of the variables that is listed as 'Sortable' in the description. Ex: '-congress')
        """
        super(BillInputSet, self)._set_input('Sort', value)
    def set_Sponsor(self, value):
        """
        Set the value of the Sponsor input for this Choreo. ((optional, string) The ID of the sponsor of the bill. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('Sponsor', value)
    def set_Terms(self, value):
        """
        Set the value of the Terms input for this Choreo. ((optional, string) Subject areas associated with the bill. When using this filter, provide the id of the term which is returned when requesting a single bill object. Filter operators allowed. Sortable.)
        """
        super(BillInputSet, self)._set_input('Terms', value)

class BillResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Bill Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class BillChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BillResultSet(response, path)
