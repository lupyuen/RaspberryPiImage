# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateItem
# Allows you to add or remove photos and tips from items on user-created lists.
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

class UpdateItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateItem, self).__init__(temboo_session, '/Library/Foursquare/Lists/UpdateItem')


    def new_input_set(self):
        return UpdateItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateItemChoreographyExecution(session, exec_id, path)

class UpdateItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The id of an item on a list that you wish to update.)
        """
        super(UpdateItemInputSet, self)._set_input('ItemID', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The ID of a user-created list to update)
        """
        super(UpdateItemInputSet, self)._set_input('ListID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(UpdateItemInputSet, self)._set_input('OauthToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((optional, string) If present and non-empty, adds a photo to this item. If present and empty, will remove the photo on this item. If the photo was a private checkin photo, it will be promoted to a public venue photo.)
        """
        super(UpdateItemInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UpdateItemInputSet, self)._set_input('ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((optional, string) If present, this creates a public tip on the venue and replaces any existing tip on the item. Cannot be used in conjuction with TipID or PhotoID.)
        """
        super(UpdateItemInputSet, self)._set_input('Text', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((optional, string) The id of a tip to add to the list. Cannot be used in conjunction with the Text and URL inputs. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        super(UpdateItemInputSet, self)._set_input('TipID', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) If adding a new tip using the Text input, this can associate a url with the tip.)
        """
        super(UpdateItemInputSet, self)._set_input('URL', value)

class UpdateItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UpdateItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateItemResultSet(response, path)
