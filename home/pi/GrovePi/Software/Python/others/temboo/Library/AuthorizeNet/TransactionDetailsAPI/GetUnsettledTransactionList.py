# -*- coding: utf-8 -*-

###############################################################################
#
# GetUnsettledTransactionList
# Returns limited details for unsettled transactions.
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

class GetUnsettledTransactionList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUnsettledTransactionList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUnsettledTransactionList, self).__init__(temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetUnsettledTransactionList')


    def new_input_set(self):
        return GetUnsettledTransactionListInputSet()

    def _make_result_set(self, result, path):
        return GetUnsettledTransactionListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUnsettledTransactionListChoreographyExecution(session, exec_id, path)

class GetUnsettledTransactionListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUnsettledTransactionList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        super(GetUnsettledTransactionListInputSet, self)._set_input('APILoginId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        super(GetUnsettledTransactionListInputSet, self)._set_input('Endpoint', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        super(GetUnsettledTransactionListInputSet, self)._set_input('TransactionKey', value)

class GetUnsettledTransactionListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUnsettledTransactionList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetUnsettledTransactionListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUnsettledTransactionListResultSet(response, path)
