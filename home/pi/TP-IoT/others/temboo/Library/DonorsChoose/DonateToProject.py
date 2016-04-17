# -*- coding: utf-8 -*-

###############################################################################
#
# DonateToProject
# Makes a donation to a specified DonorsChoose.org project.
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

class DonateToProject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DonateToProject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DonateToProject, self).__init__(temboo_session, '/Library/DonorsChoose/DonateToProject')


    def new_input_set(self):
        return DonateToProjectInputSet()

    def _make_result_set(self, result, path):
        return DonateToProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DonateToProjectChoreographyExecution(session, exec_id, path)

class DonateToProjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DonateToProject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The APIKey provided by DonorsChoose.org.)
        """
        super(DonateToProjectInputSet, self)._set_input('APIKey', value)
    def set_APIPassword(self, value):
        """
        Set the value of the APIPassword input for this Choreo. ((required, string) Your DonorsChoose.org API password. This is only required when performing transactions.)
        """
        super(DonateToProjectInputSet, self)._set_input('APIPassword', value)
    def set_Address1(self, value):
        """
        Set the value of the Address1 input for this Choreo. ((optional, string) Line one of the donor's address.)
        """
        super(DonateToProjectInputSet, self)._set_input('Address1', value)
    def set_Address2(self, value):
        """
        Set the value of the Address2 input for this Choreo. ((optional, string) Line two of the donor's address.)
        """
        super(DonateToProjectInputSet, self)._set_input('Address2', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, integer) The donation amount. Must be a whole number.)
        """
        super(DonateToProjectInputSet, self)._set_input('Amount', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) To wrap the response in a callback function, include the name in this input.)
        """
        super(DonateToProjectInputSet, self)._set_input('Callback', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The donor's city.)
        """
        super(DonateToProjectInputSet, self)._set_input('City', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address of the person who is making the donation.)
        """
        super(DonateToProjectInputSet, self)._set_input('Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of the donor.)
        """
        super(DonateToProjectInputSet, self)._set_input('FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the donor.)
        """
        super(DonateToProjectInputSet, self)._set_input('LastName', value)
    def set_ProposalId(self, value):
        """
        Set the value of the ProposalId input for this Choreo. ((required, integer) The ID of the project that will receive the donation.)
        """
        super(DonateToProjectInputSet, self)._set_input('ProposalId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        super(DonateToProjectInputSet, self)._set_input('ResponseFormat', value)
    def set_Salutation(self, value):
        """
        Set the value of the Salutation input for this Choreo. ((optional, string) Hwo the donor wants to be acknowledged on donorschoose.org.)
        """
        super(DonateToProjectInputSet, self)._set_input('Salutation', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The donor's state.)
        """
        super(DonateToProjectInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) The donor's five-digit zip code.)
        """
        super(DonateToProjectInputSet, self)._set_input('Zip', value)

class DonateToProjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DonateToProject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DonorsChoose.org.)
        """
        return self._output.get('Response', None)

class DonateToProjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DonateToProjectResultSet(response, path)
