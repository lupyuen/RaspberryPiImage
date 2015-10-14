# -*- coding: utf-8 -*-

###############################################################################
#
# Listing
# Retrieves a list of transactions for the user associated with the authorized access token.
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

class Listing(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Listing Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Listing, self).__init__(temboo_session, '/Library/Dwolla/Transactions/Listing')


    def new_input_set(self):
        return ListingInputSet()

    def _make_result_set(self, result, path):
        return ListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListingChoreographyExecution(session, exec_id, path)

class ListingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Listing
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        super(ListingInputSet, self)._set_input('AccessToken', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Latest date and time for which to retrieve transactions.  (In ISO 8601 format.  e.g. 2012-07-22)  Defaults to current date and time in UTC.)
        """
        super(ListingInputSet, self)._set_input('EndDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of transactions to retrieve. Defaults to 10. Can be between 1 and 200 transactions.)
        """
        super(ListingInputSet, self)._set_input('Limit', value)
    def set_SinceDate(self, value):
        """
        Set the value of the SinceDate input for this Choreo. ((optional, string) Earliest date and time (in ISO 8601 format) for which to retrieve transactions. (e.g. 2012-07-20) Defaults to 7 days prior to current date and time in UTC.)
        """
        super(ListingInputSet, self)._set_input('SinceDate', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Number of transactions to skip. Defaults to 0.)
        """
        super(ListingInputSet, self)._set_input('Skip', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Transaction types to retrieve. Must be delimited by a '|'. Options are money_sent, money_received, deposit, withdrawal, and fee. Defaults to include all transaction types.)
        """
        super(ListingInputSet, self)._set_input('Types', value)

class ListingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Listing Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class ListingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListingResultSet(response, path)
