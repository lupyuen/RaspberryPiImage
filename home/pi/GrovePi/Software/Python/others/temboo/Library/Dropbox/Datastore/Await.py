# -*- coding: utf-8 -*-

###############################################################################
#
# Await
# Allows your application to perform a "long poll" request that blocks up to a minute or until a change is detected.
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

class Await(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Await Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Await, self).__init__(temboo_session, '/Library/Dropbox/Datastore/Await')


    def new_input_set(self):
        return AwaitInputSet()

    def _make_result_set(self, result, path):
        return AwaitResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AwaitChoreographyExecution(session, exec_id, path)

class AwaitInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Await
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(AwaitInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(AwaitInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(AwaitInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(AwaitInputSet, self)._set_input('AppSecret', value)
    def set_Cursors(self, value):
        """
        Set the value of the Cursors input for this Choreo. ((required, json) A JSON-encoded list of key/value pairs where the key is a datastore handle, and the value is a particular revision. This is required unless specifying Token.)
        """
        super(AwaitInputSet, self)._set_input('Cursors', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(AwaitInputSet, self)._set_input('ResponseFormat', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) A dbase64 string which represents a hash of the datastores list. Token values are returned by the ListDatastores choreo. This is required unless specifying Cursors.)
        """
        super(AwaitInputSet, self)._set_input('Token', value)

class AwaitResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Await Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class AwaitChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AwaitResultSet(response, path)
