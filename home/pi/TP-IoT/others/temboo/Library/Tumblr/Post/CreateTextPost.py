# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTextPost
# Creates a new text post for a specified Tumblr blog.
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

class CreateTextPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTextPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTextPost, self).__init__(temboo_session, '/Library/Tumblr/Post/CreateTextPost')


    def new_input_set(self):
        return CreateTextPostInputSet()

    def _make_result_set(self, result, path):
        return CreateTextPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTextPostChoreographyExecution(session, exec_id, path)

class CreateTextPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTextPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The full post body, HTML allowed.)
        """
        super(CreateTextPostInputSet, self)._set_input('Body', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(CreateTextPostInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CreateTextPostInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateTextPostInputSet, self)._set_input('AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        super(CreateTextPostInputSet, self)._set_input('BaseHostname', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        super(CreateTextPostInputSet, self)._set_input('Date', value)
    def set_Markdown(self, value):
        """
        Set the value of the Markdown input for this Choreo. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        super(CreateTextPostInputSet, self)._set_input('Markdown', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateTextPostInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        super(CreateTextPostInputSet, self)._set_input('SecretKey', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) Adds a short text summary to the end of the post URL.)
        """
        super(CreateTextPostInputSet, self)._set_input('Slug', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        super(CreateTextPostInputSet, self)._set_input('State', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated tags for this post.)
        """
        super(CreateTextPostInputSet, self)._set_input('Tags', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The optional title of the post. HTML entities must be escaped.)
        """
        super(CreateTextPostInputSet, self)._set_input('Title', value)
    def set_Tweet(self, value):
        """
        Set the value of the Tweet input for this Choreo. ((optional, string) Manages the autotweet (if enabled) for this post. Set to "off" for no tweet. Enter text to override the default tweet.)
        """
        super(CreateTextPostInputSet, self)._set_input('Tweet', value)

class CreateTextPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTextPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        return self._output.get('Response', None)

class CreateTextPostChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTextPostResultSet(response, path)
