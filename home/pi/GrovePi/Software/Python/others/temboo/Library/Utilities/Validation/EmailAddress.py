# -*- coding: utf-8 -*-

###############################################################################
#
# EmailAddress
# Verifies that a given email address matches an expected standard pattern.
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

class EmailAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EmailAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EmailAddress, self).__init__(temboo_session, '/Library/Utilities/Validation/EmailAddress')


    def new_input_set(self):
        return EmailAddressInputSet()

    def _make_result_set(self, result, path):
        return EmailAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EmailAddressChoreographyExecution(session, exec_id, path)

class EmailAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EmailAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address to validate.)
        """
        super(EmailAddressInputSet, self)._set_input('EmailAddress', value)

class EmailAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EmailAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Match(self):
        """
        Retrieve the value for the "Match" output from this Choreo execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        return self._output.get('Match', None)

class EmailAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EmailAddressResultSet(response, path)
