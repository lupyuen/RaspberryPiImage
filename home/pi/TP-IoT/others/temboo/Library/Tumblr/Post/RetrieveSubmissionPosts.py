# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveSubmissionPosts
# Retrieves a list of submission posts for a specified Tumblr blog.
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

class RetrieveSubmissionPosts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveSubmissionPosts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveSubmissionPosts, self).__init__(temboo_session, '/Library/Tumblr/Post/RetrieveSubmissionPosts')


    def new_input_set(self):
        return RetrieveSubmissionPostsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSubmissionPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSubmissionPostsChoreographyExecution(session, exec_id, path)

class RetrieveSubmissionPostsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveSubmissionPosts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('BaseHostname', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        super(RetrieveSubmissionPostsInputSet, self)._set_input('SecretKey', value)

class RetrieveSubmissionPostsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveSubmissionPosts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrieveSubmissionPostsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveSubmissionPostsResultSet(response, path)
