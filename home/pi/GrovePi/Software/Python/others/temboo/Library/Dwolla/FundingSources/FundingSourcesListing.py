# -*- coding: utf-8 -*-

###############################################################################
#
# FundingSourcesListing
# Retrieves a list of verified funding sources for the user associated with the authorized access token.
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

class FundingSourcesListing(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FundingSourcesListing Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FundingSourcesListing, self).__init__(temboo_session, '/Library/Dwolla/FundingSources/FundingSourcesListing')


    def new_input_set(self):
        return FundingSourcesListingInputSet()

    def _make_result_set(self, result, path):
        return FundingSourcesListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FundingSourcesListingChoreographyExecution(session, exec_id, path)

class FundingSourcesListingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FundingSourcesListing
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        super(FundingSourcesListingInputSet, self)._set_input('AccessToken', value)

class FundingSourcesListingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FundingSourcesListing Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class FundingSourcesListingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FundingSourcesListingResultSet(response, path)
