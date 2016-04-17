# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAudioPostWithURL
# Creates a new audio post using a specified external URL.
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

class CreateAudioPostWithURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAudioPostWithURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateAudioPostWithURL, self).__init__(temboo_session, '/Library/Tumblr/Post/CreateAudioPostWithURL')


    def new_input_set(self):
        return CreateAudioPostWithURLInputSet()

    def _make_result_set(self, result, path):
        return CreateAudioPostWithURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAudioPostWithURLChoreographyExecution(session, exec_id, path)

class CreateAudioPostWithURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAudioPostWithURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ExternalURL(self, value):
        """
        Set the value of the ExternalURL input for this Choreo. ((required, string) The URL of the site that hosts the audio file (not Tumblr).)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('ExternalURL', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('BaseHostname', value)
    def set_Caption(self, value):
        """
        Set the value of the Caption input for this Choreo. ((optional, string) The user-supplied caption. HTML is allowed.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Caption', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Date', value)
    def set_Markdown(self, value):
        """
        Set the value of the Markdown input for this Choreo. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Markdown', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('SecretKey', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) Adds a short text summary to the end of the post URL.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Slug', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('State', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated tags for this post.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Tags', value)
    def set_Tweet(self, value):
        """
        Set the value of the Tweet input for this Choreo. ((optional, string) Manages the autotweet (if enabled) for this post. Set to "off" for no tweet. Enter text to override the default tweet.)
        """
        super(CreateAudioPostWithURLInputSet, self)._set_input('Tweet', value)

class CreateAudioPostWithURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAudioPostWithURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class CreateAudioPostWithURLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateAudioPostWithURLResultSet(response, path)
