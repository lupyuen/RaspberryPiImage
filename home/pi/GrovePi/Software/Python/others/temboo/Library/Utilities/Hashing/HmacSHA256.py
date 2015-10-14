# -*- coding: utf-8 -*-

###############################################################################
#
# HmacSHA256
# Generates a SHA256-encrypted HMAC signature for the specified message text using the specified secret key.
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

class HmacSHA256(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HmacSHA256 Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(HmacSHA256, self).__init__(temboo_session, '/Library/Utilities/Hashing/HmacSHA256')


    def new_input_set(self):
        return HmacSHA256InputSet()

    def _make_result_set(self, result, path):
        return HmacSHA256ResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HmacSHA256ChoreographyExecution(session, exec_id, path)

class HmacSHA256InputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HmacSHA256
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The secret key used to generate the SHA256-encrypted HMAC signature.)
        """
        super(HmacSHA256InputSet, self)._set_input('Key', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be SHA256-encrypted.)
        """
        super(HmacSHA256InputSet, self)._set_input('Text', value)

class HmacSHA256ResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HmacSHA256 Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_HmacSignature(self):
        """
        Retrieve the value for the "HmacSignature" output from this Choreo execution. ((string) The HMAC Signature for the specified string.)
        """
        return self._output.get('HmacSignature', None)

class HmacSHA256ChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return HmacSHA256ResultSet(response, path)
