# -*- coding: utf-8 -*-

###############################################################################
#
# Checksum
# Returns a checksum of the specified text calculated using the specified algorithm. 
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

class Checksum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Checksum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Checksum, self).__init__(temboo_session, '/Library/Utilities/Hashing/Checksum')


    def new_input_set(self):
        return ChecksumInputSet()

    def _make_result_set(self, result, path):
        return ChecksumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChecksumChoreographyExecution(session, exec_id, path)

class ChecksumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Checksum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Algorithm(self, value):
        """
        Set the value of the Algorithm input for this Choreo. ((required, string) Algorithm used to calculate the checksum. Valid values are: FIX44,  MD5+BASE64, or MD5+HEX (the default). MD5+BASE64 and MD5+HEX return the result in Base64 and hexadecimal encoding, respectively.)
        """
        super(ChecksumInputSet, self)._set_input('Algorithm', value)
    def set_Base64DecodeValue(self, value):
        """
        Set the value of the Base64DecodeValue input for this Choreo. ((optional, boolean) Setting this parameter to 1 indicates that the Text is Base64 encoded, and that the choreo should decode the value before calculating the checksum. Defaults to 0.)
        """
        super(ChecksumInputSet, self)._set_input('Base64DecodeValue', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text to return a checksum for.)
        """
        super(ChecksumInputSet, self)._set_input('Text', value)

class ChecksumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Checksum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Checksum(self):
        """
        Retrieve the value for the "Checksum" output from this Choreo execution. ((string) The checksum result.)
        """
        return self._output.get('Checksum', None)

class ChecksumChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ChecksumResultSet(response, path)
