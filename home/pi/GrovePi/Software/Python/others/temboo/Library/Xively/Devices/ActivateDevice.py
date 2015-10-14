# -*- coding: utf-8 -*-

###############################################################################
#
# ActivateDevice
# Activates (or reactivates) a device given an authorization code. Returns the device API Key and Feed ID. 
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

class ActivateDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ActivateDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ActivateDevice, self).__init__(temboo_session, '/Library/Xively/Devices/ActivateDevice')


    def new_input_set(self):
        return ActivateDeviceInputSet()

    def _make_result_set(self, result, path):
        return ActivateDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ActivateDeviceChoreographyExecution(session, exec_id, path)

class ActivateDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ActivateDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) Not required for first activation. If re-activating a device, either the original device APIKey returned from the first activation or the master APIKey is required.)
        """
        super(ActivateDeviceInputSet, self)._set_input('APIKey', value)
    def set_ActivationCode(self, value):
        """
        Set the value of the ActivationCode input for this Choreo. ((required, string) Activation code provided when pre-registering a device with a serial number.)
        """
        super(ActivateDeviceInputSet, self)._set_input('ActivationCode', value)

class ActivateDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ActivateDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively. Upon successful activation, it returns a JSON array containing the device APIKey, FeedID and Datastreams.)
        """
        return self._output.get('Response', None)

class ActivateDeviceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ActivateDeviceResultSet(response, path)
