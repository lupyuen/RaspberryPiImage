# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountProfile
# Update a SendGrid account profile.
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

class UpdateAccountProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateAccountProfile, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Profile/UpdateAccountProfile')


    def new_input_set(self):
        return UpdateAccountProfileInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountProfileChoreographyExecution(session, exec_id, path)

class UpdateAccountProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('APIUser', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) The company address.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city where this address is located in.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('City', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of the profile being updated.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the profile being updated.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('LastName', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((optional, string) The phone number, where you can be reached.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('Phone', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state where this company is located in.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('State', value)
    def set_Website(self, value):
        """
        Set the value of the Website input for this Choreo. ((optional, string) The company's website.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('Website', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) The zipcode where this company is located.)
        """
        super(UpdateAccountProfileInputSet, self)._set_input('Zip', value)


class UpdateAccountProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class UpdateAccountProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateAccountProfileResultSet(response, path)
