# -*- coding: utf-8 -*-

###############################################################################
#
# PresidentialDonorInformation
# Retrieve details about individual donors, or a summary of donors from a particular location to a presidential election campaign.
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

class PresidentialDonorInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PresidentialDonorInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PresidentialDonorInformation, self).__init__(temboo_session, '/Library/NYTimes/CampaignFinance/PresidentialCampaigns/PresidentialDonorInformation')


    def new_input_set(self):
        return PresidentialDonorInformationInputSet()

    def _make_result_set(self, result, path):
        return PresidentialDonorInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PresidentialDonorInformationChoreographyExecution(session, exec_id, path)

class PresidentialDonorInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PresidentialDonorInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('CampaignCycle', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) Enter the first name of a donor.  This parameter can be used together with LastName and/or Zip)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) Enter the last name of an individual donor to be retrieved.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('LastName', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Specify the starting point of the retrieved results, in multiples of 20.  By default, the first 20 results are returned.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('ResponseFormat', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) Enter a zipcode for which donor information wil be retrieved.)
        """
        super(PresidentialDonorInformationInputSet, self)._set_input('Zip', value)

class PresidentialDonorInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PresidentialDonorInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class PresidentialDonorInformationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PresidentialDonorInformationResultSet(response, path)
