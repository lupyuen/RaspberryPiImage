# -*- coding: utf-8 -*-

###############################################################################
#
# ExportIncrementalTickets
# Returns a lightweight representation of what changed in the ticket "since you last asked".
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

class ExportIncrementalTickets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ExportIncrementalTickets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ExportIncrementalTickets, self).__init__(temboo_session, '/Library/Zendesk/IncrementalTickets/ExportIncrementalTickets')


    def new_input_set(self):
        return ExportIncrementalTicketsInputSet()

    def _make_result_set(self, result, path):
        return ExportIncrementalTicketsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExportIncrementalTicketsChoreographyExecution(session, exec_id, path)

class ExportIncrementalTicketsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ExportIncrementalTickets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(ExportIncrementalTicketsInputSet, self)._set_input('Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(ExportIncrementalTicketsInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(ExportIncrementalTicketsInputSet, self)._set_input('Server', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((required, string) Return a list of tickets created after this timestamp (in seconds since Epoch UTC).  Tickets less than 5 minutes old are not included in the response.)
        """
        super(ExportIncrementalTicketsInputSet, self)._set_input('StartTime', value)

class ExportIncrementalTicketsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ExportIncrementalTickets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class ExportIncrementalTicketsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ExportIncrementalTicketsResultSet(response, path)
