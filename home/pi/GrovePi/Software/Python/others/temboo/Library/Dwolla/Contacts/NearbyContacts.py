# -*- coding: utf-8 -*-

###############################################################################
#
# NearbyContacts
# Retrieves nearby Dwolla spots within the range of the provided latitude and longitude.
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

class NearbyContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the NearbyContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(NearbyContacts, self).__init__(temboo_session, '/Library/Dwolla/Contacts/NearbyContacts')


    def new_input_set(self):
        return NearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return NearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NearbyContactsChoreographyExecution(session, exec_id, path)

class NearbyContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the NearbyContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Dwolla (AKA the Consumer Key).)
        """
        super(NearbyContactsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by Dwolla (AKA the Consumer Secret).)
        """
        super(NearbyContactsInputSet, self)._set_input('ClientSecret', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Current latitude.)
        """
        super(NearbyContactsInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of spots to retrieve. Defaults to 10.)
        """
        super(NearbyContactsInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Current longitude.)
        """
        super(NearbyContactsInputSet, self)._set_input('Longitude', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((optional, integer) Range to retrieve spots for in miles.)
        """
        super(NearbyContactsInputSet, self)._set_input('Range', value)

class NearbyContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the NearbyContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class NearbyContactsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return NearbyContactsResultSet(response, path)
