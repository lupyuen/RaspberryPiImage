# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTicket
# Updates an existing ticket.
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

class UpdateTicket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateTicket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateTicket, self).__init__(temboo_session, '/Library/Zendesk/Tickets/UpdateTicket')


    def new_input_set(self):
        return UpdateTicketInputSet()

    def _make_result_set(self, result, path):
        return UpdateTicketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTicketChoreographyExecution(session, exec_id, path)

class UpdateTicketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateTicket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) The text for a ticket comment.)
        """
        super(UpdateTicketInputSet, self)._set_input('Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(UpdateTicketInputSet, self)._set_input('Email', value)
    def set_Metadata(self, value):
        """
        Set the value of the Metadata input for this Choreo. ((optional, json) Ticket metadata formatted in JSON. See below for more information on the input format.)
        """
        super(UpdateTicketInputSet, self)._set_input('Metadata', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(UpdateTicketInputSet, self)._set_input('Password', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((optional, boolean) A flag indicating if this update is public or not. Defaults to "true")
        """
        super(UpdateTicketInputSet, self)._set_input('Public', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(UpdateTicketInputSet, self)._set_input('Server', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((conditional, string) The status of the ticket (i.e. solved, pending, open).)
        """
        super(UpdateTicketInputSet, self)._set_input('Status', value)
    def set_TicketData(self, value):
        """
        Set the value of the TicketData input for this Choreo. ((optional, json) A JSON-formatted string containing the ticket properties you wish to set. This can be used as an alternative to setting individual inputs representing ticket properties.)
        """
        super(UpdateTicketInputSet, self)._set_input('TicketData', value)
    def set_TicketID(self, value):
        """
        Set the value of the TicketID input for this Choreo. ((required, integer) The id of the ticket being updated.)
        """
        super(UpdateTicketInputSet, self)._set_input('TicketID', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        super(UpdateTicketInputSet, self)._set_input('Token', value)

class UpdateTicketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateTicket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateTicketChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateTicketResultSet(response, path)
