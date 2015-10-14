# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteItem
# Allows a user to delete an item from a list.

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

class DeleteItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteItem, self).__init__(temboo_session, '/Library/Foursquare/Lists/DeleteItem')


    def new_input_set(self):
        return DeleteItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteItemChoreographyExecution(session, exec_id, path)

class DeleteItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The id of the item to delete.)
        """
        super(DeleteItemInputSet, self)._set_input('ItemID', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) This can be a user-created list id or one of tips, todos, or dones.)
        """
        super(DeleteItemInputSet, self)._set_input('ListID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(DeleteItemInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DeleteItemInputSet, self)._set_input('ResponseFormat', value)

class DeleteItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class DeleteItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteItemResultSet(response, path)
