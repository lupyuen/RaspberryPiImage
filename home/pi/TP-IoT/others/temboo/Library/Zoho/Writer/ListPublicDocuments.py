# -*- coding: utf-8 -*-

###############################################################################
#
# ListPublicDocuments
# Lists all the documents that have been made "public" from a user's Zoho Writer Account.
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

class ListPublicDocuments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPublicDocuments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListPublicDocuments, self).__init__(temboo_session, '/Library/Zoho/Writer/ListPublicDocuments')


    def new_input_set(self):
        return ListPublicDocumentsInputSet()

    def _make_result_set(self, result, path):
        return ListPublicDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPublicDocumentsChoreographyExecution(session, exec_id, path)

class ListPublicDocumentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPublicDocuments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Sets the number of documents to be listed.)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('Limit', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        super(ListPublicDocumentsInputSet, self)._set_input('LoginID', value)
    def set_OrderBy(self, value):
        """
        Set the value of the OrderBy input for this Choreo. ((optional, string) Order documents by createdTime, lastModifiedTime or name.)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('OrderBy', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to xml.)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('ResponseFormat', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('SortOrder', value)
    def set_StartFrom(self, value):
        """
        Set the value of the StartFrom input for this Choreo. ((optional, integer) Sets the initial document number from which the documents will be listed.)
        """
        super(ListPublicDocumentsInputSet, self)._set_input('StartFrom', value)

class ListPublicDocumentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPublicDocuments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        return self._output.get('Response', None)

class ListPublicDocumentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListPublicDocumentsResultSet(response, path)
