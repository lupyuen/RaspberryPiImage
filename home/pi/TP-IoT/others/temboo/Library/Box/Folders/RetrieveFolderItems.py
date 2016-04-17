# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveFolderItems
# Retrieves only the files and/or folders contained within the specified folder.
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

class RetrieveFolderItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveFolderItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveFolderItems, self).__init__(temboo_session, '/Library/Box/Folders/RetrieveFolderItems')


    def new_input_set(self):
        return RetrieveFolderItemsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveFolderItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveFolderItemsChoreographyExecution(session, exec_id, path)

class RetrieveFolderItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveFolderItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((conditional, string) The id of the folder that you want to retrieve items for. Defaults to 0 indicating the "root" folder.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('FolderID', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of items to return.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The item at which to begin the response.)
        """
        super(RetrieveFolderItemsInputSet, self)._set_input('Offset', value)


class RetrieveFolderItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveFolderItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class RetrieveFolderItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveFolderItemsResultSet(response, path)
