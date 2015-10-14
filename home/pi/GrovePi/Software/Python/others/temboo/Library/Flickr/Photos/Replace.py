# -*- coding: utf-8 -*-

###############################################################################
#
# Replace
#  Replaces a photo that has already been uploaded to Flickr.
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

class Replace(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Replace Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Replace, self).__init__(temboo_session, '/Library/Flickr/Photos/Replace')


    def new_input_set(self):
        return ReplaceInputSet()

    def _make_result_set(self, result, path):
        return ReplaceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReplaceChoreographyExecution(session, exec_id, path)

class ReplaceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Replace
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ImageFileContents(self, value):
        """
        Set the value of the ImageFileContents input for this Choreo. ((conditional, string) The base-64 encoded file contents to replace. Required unless using the URL input.)
        """
        super(ReplaceInputSet, self)._set_input('ImageFileContents', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ReplaceInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(ReplaceInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ReplaceInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ReplaceInputSet, self)._set_input('AccessToken', value)
    def set_Async(self, value):
        """
        Set the value of the Async input for this Choreo. ((optional, boolean) Set to 1 to replace photos in async mode. This can be used if you don't want to wait around for an upload to complete.)
        """
        super(ReplaceInputSet, self)._set_input('Async', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, string) The ID of the photo to replace.)
        """
        super(ReplaceInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ReplaceInputSet, self)._set_input('ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) A url for a photo to use as the replacement. Required unless specifying the ImageFileContents.)
        """
        super(ReplaceInputSet, self)._set_input('URL', value)


class ReplaceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Replace Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ReplaceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReplaceResultSet(response, path)
