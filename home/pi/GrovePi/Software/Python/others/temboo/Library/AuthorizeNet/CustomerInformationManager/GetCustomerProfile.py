# -*- coding: utf-8 -*-

###############################################################################
#
# GetCustomerProfile
# Retrieves an existing customer profile by id with relevant payment profiles and shipping addresses.
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

class GetCustomerProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCustomerProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCustomerProfile, self).__init__(temboo_session, '/Library/AuthorizeNet/CustomerInformationManager/GetCustomerProfile')


    def new_input_set(self):
        return GetCustomerProfileInputSet()

    def _make_result_set(self, result, path):
        return GetCustomerProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCustomerProfileChoreographyExecution(session, exec_id, path)

class GetCustomerProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCustomerProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerProfileInputSet, self)._set_input('APILoginId', value)
    def set_CustomerProfileId(self, value):
        """
        Set the value of the CustomerProfileId input for this Choreo. ((required, integer) The id of the customer who's profile you want to return.)
        """
        super(GetCustomerProfileInputSet, self)._set_input('CustomerProfileId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        super(GetCustomerProfileInputSet, self)._set_input('Endpoint', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerProfileInputSet, self)._set_input('TransactionKey', value)

class GetCustomerProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCustomerProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetCustomerProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCustomerProfileResultSet(response, path)
