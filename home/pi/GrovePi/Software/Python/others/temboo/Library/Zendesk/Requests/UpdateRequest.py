# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRequest
# Updates an existing request.
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

class UpdateRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateRequest, self).__init__(temboo_session, '/Library/Zendesk/Requests/UpdateRequest')


    def new_input_set(self):
        return UpdateRequestInputSet()

    def _make_result_set(self, result, path):
        return UpdateRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRequestChoreographyExecution(session, exec_id, path)

class UpdateRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestData(self, value):
        """
        Set the value of the RequestData input for this Choreo. ((optional, json) A JSON-formatted string containing the request properties you wish to set. This can be used as an alternative to setting individual inputs representing request properties.)
        """
        super(UpdateRequestInputSet, self)._set_input('RequestData', value)
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) A comment associated with the request.)
        """
        super(UpdateRequestInputSet, self)._set_input('Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(UpdateRequestInputSet, self)._set_input('Email', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((conditional, string) The ID of the request to update.)
        """
        super(UpdateRequestInputSet, self)._set_input('ID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(UpdateRequestInputSet, self)._set_input('Password', value)
    def set_Priority(self, value):
        """
        Set the value of the Priority input for this Choreo. ((conditional, string) Priority (e.g. low, normal, high, urgent). Defaults to normal.)
        """
        super(UpdateRequestInputSet, self)._set_input('Priority', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(UpdateRequestInputSet, self)._set_input('Server', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((conditional, string) The subject of the request.)
        """
        super(UpdateRequestInputSet, self)._set_input('Subject', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((conditional, string) Type of request (e.g.question, incident, problem, task). Defaults to incident.)
        """
        super(UpdateRequestInputSet, self)._set_input('Type', value)

class UpdateRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateRequestResultSet(response, path)
