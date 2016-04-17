# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllDevices
# Returns a paged list of devices belonging to a specific product.
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

class ListAllDevices(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllDevices Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListAllDevices, self).__init__(temboo_session, '/Library/Xively/Devices/ListAllDevices')


    def new_input_set(self):
        return ListAllDevicesInputSet()

    def _make_result_set(self, result, path):
        return ListAllDevicesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllDevicesChoreographyExecution(session, exec_id, path)

class ListAllDevicesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllDevices
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(ListAllDevicesInputSet, self)._set_input('APIKey', value)
    def set_Activated(self, value):
        """
        Set the value of the Activated input for this Choreo. ((optional, string) Filter for returning device serial numbers in the requested activation state. Valid values: "all" (default), "true" or "false".)
        """
        super(ListAllDevicesInputSet, self)._set_input('Activated', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates which page of results you are requesting. Starts from 1.)
        """
        super(ListAllDevicesInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Defines how many results to return per page (1 to 1000, default is 30).)
        """
        super(ListAllDevicesInputSet, self)._set_input('PerPage', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The ID for the product you would like to retrieve the list of devices for.)
        """
        super(ListAllDevicesInputSet, self)._set_input('ProductID', value)
    def set_SerialNumber(self, value):
        """
        Set the value of the SerialNumber input for this Choreo. ((optional, string) Filter by providing an exact or partial serial number string. Letters are case-insensitive. Ex: inputting 'abc' will return serials that contain 'Abc',  'aBc' and 'abc', but not 'ab-c'.)
        """
        super(ListAllDevicesInputSet, self)._set_input('SerialNumber', value)

class ListAllDevicesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllDevices Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively.)
        """
        return self._output.get('Response', None)

class ListAllDevicesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListAllDevicesResultSet(response, path)
