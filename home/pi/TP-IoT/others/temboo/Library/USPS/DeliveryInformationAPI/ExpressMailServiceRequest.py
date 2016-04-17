# -*- coding: utf-8 -*-

###############################################################################
#
# ExpressMailServiceRequest
# Request USPS Express Mail shipping information for a given origin and destination.
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

class ExpressMailServiceRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ExpressMailServiceRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ExpressMailServiceRequest, self).__init__(temboo_session, '/Library/USPS/DeliveryInformationAPI/ExpressMailServiceRequest')


    def new_input_set(self):
        return ExpressMailServiceRequestInputSet()

    def _make_result_set(self, result, path):
        return ExpressMailServiceRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExpressMailServiceRequestChoreographyExecution(session, exec_id, path)

class ExpressMailServiceRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ExpressMailServiceRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) Date the package is to be shipped. Must take the form 'MM/DD/YYYY'.)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('Date', value)
    def set_DestinationZip(self, value):
        """
        Set the value of the DestinationZip input for this Choreo. ((required, integer) Five digit zip code.)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('DestinationZip', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('Endpoint', value)
    def set_OriginZip(self, value):
        """
        Set the value of the OriginZip input for this Choreo. ((required, integer) Three or five digit zip code.)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('OriginZip', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('Password', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        super(ExpressMailServiceRequestInputSet, self)._set_input('UserId', value)

class ExpressMailServiceRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ExpressMailServiceRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class ExpressMailServiceRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ExpressMailServiceRequestResultSet(response, path)
