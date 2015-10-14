# -*- coding: utf-8 -*-

###############################################################################
#
# InsertRecord
# Inserts a record into a datastore table.
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

class InsertRecord(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertRecord Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InsertRecord, self).__init__(temboo_session, '/Library/Dropbox/Datastore/InsertRecord')


    def new_input_set(self):
        return InsertRecordInputSet()

    def _make_result_set(self, result, path):
        return InsertRecordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertRecordChoreographyExecution(session, exec_id, path)

class InsertRecordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertRecord
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(InsertRecordInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(InsertRecordInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(InsertRecordInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(InsertRecordInputSet, self)._set_input('AppSecret', value)
    def set_Data(self, value):
        """
        Set the value of the Data input for this Choreo. ((required, json) A JSON-encoded list of name/value pairs to insert into the table.)
        """
        super(InsertRecordInputSet, self)._set_input('Data', value)
    def set_Handle(self, value):
        """
        Set the value of the Handle input for this Choreo. ((required, string) The handle of an existing datastore.)
        """
        super(InsertRecordInputSet, self)._set_input('Handle', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(InsertRecordInputSet, self)._set_input('ResponseFormat', value)
    def set_Revision(self, value):
        """
        Set the value of the Revision input for this Choreo. ((conditional, string) The revision to which to apply the delta. If not provided, the Choreo will perform a lookup for the latest revision number.)
        """
        super(InsertRecordInputSet, self)._set_input('Revision', value)
    def set_RowID(self, value):
        """
        Set the value of the RowID input for this Choreo. ((conditional, string) The row identifier. If not provided, a randomly generated GUID will be inserted for this value.)
        """
        super(InsertRecordInputSet, self)._set_input('RowID', value)
    def set_Table(self, value):
        """
        Set the value of the Table input for this Choreo. ((required, string) The name of the datastore table.)
        """
        super(InsertRecordInputSet, self)._set_input('Table', value)

class InsertRecordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertRecord Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class InsertRecordChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InsertRecordResultSet(response, path)
