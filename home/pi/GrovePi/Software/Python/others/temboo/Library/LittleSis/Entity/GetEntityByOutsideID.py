# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntityByOutsideID
# Retrieves the record for an Entity in LittleSis using the ID of a number of third-party organizations such as the SEC or GovTrack.
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

class GetEntityByOutsideID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEntityByOutsideID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetEntityByOutsideID, self).__init__(temboo_session, '/Library/LittleSis/Entity/GetEntityByOutsideID')


    def new_input_set(self):
        return GetEntityByOutsideIDInputSet()

    def _make_result_set(self, result, path):
        return GetEntityByOutsideIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntityByOutsideIDChoreographyExecution(session, exec_id, path)

class GetEntityByOutsideIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEntityByOutsideID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        super(GetEntityByOutsideIDInputSet, self)._set_input('APIKey', value)
    def set_IDType(self, value):
        """
        Set the value of the IDType input for this Choreo. ((required, string) You can search for a record by the IDs of other third-party services. Acceptable inputs: ticker, sec_cik, fec_id, bioguide_id, govtrack_id, crp_id, watchdog_id. See documentation for more information.)
        """
        super(GetEntityByOutsideIDInputSet, self)._set_input('IDType', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the record to be returned.)
        """
        super(GetEntityByOutsideIDInputSet, self)._set_input('ID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        super(GetEntityByOutsideIDInputSet, self)._set_input('ResponseFormat', value)

class GetEntityByOutsideIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEntityByOutsideID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetEntityByOutsideIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetEntityByOutsideIDResultSet(response, path)
