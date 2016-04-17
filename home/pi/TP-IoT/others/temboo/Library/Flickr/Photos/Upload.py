# -*- coding: utf-8 -*-

###############################################################################
#
# Upload
# Uploads a photo to Flickr.
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

class Upload(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Upload Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Upload, self).__init__(temboo_session, '/Library/Flickr/Photos/Upload')


    def new_input_set(self):
        return UploadInputSet()

    def _make_result_set(self, result, path):
        return UploadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadChoreographyExecution(session, exec_id, path)

class UploadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Upload
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ImageFileContents(self, value):
        """
        Set the value of the ImageFileContents input for this Choreo. ((conditional, string) The base-64 encoded file contents to upload. Required unless using the URL input.)
        """
        super(UploadInputSet, self)._set_input('ImageFileContents', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(UploadInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(UploadInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(UploadInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(UploadInputSet, self)._set_input('AccessToken', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, integer) The type of content you are uploading. Set to 1 for Photo, 2 for Screenshot, or 3 for Other. Defaults to 1.)
        """
        super(UploadInputSet, self)._set_input('ContentType', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the photo.)
        """
        super(UploadInputSet, self)._set_input('Description', value)
    def set_Hidden(self, value):
        """
        Set the value of the Hidden input for this Choreo. ((optional, integer) Set to 1 to allow photos to appear in global search results, 2 to be hidden from public searches. Defaults to 2.)
        """
        super(UploadInputSet, self)._set_input('Hidden', value)
    def set_IsFamily(self, value):
        """
        Set the value of the IsFamily input for this Choreo. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        super(UploadInputSet, self)._set_input('IsFamily', value)
    def set_IsFriend(self, value):
        """
        Set the value of the IsFriend input for this Choreo. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        super(UploadInputSet, self)._set_input('IsFriend', value)
    def set_IsPublic(self, value):
        """
        Set the value of the IsPublic input for this Choreo. ((optional, boolean) Set to 0 for no, 1 for yes. Specifies who can view the photo. Defaults to 0.)
        """
        super(UploadInputSet, self)._set_input('IsPublic', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(UploadInputSet, self)._set_input('ResponseFormat', value)
    def set_SafetyLevel(self, value):
        """
        Set the value of the SafetyLevel input for this Choreo. ((optional, integer) Set value to 1 for Safe, 2 for Moderate, or 3 for Restricted. Defaults to 1.)
        """
        super(UploadInputSet, self)._set_input('SafetyLevel', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A list of tags to apply to the photo. Separate multiple tags with spaces.)
        """
        super(UploadInputSet, self)._set_input('Tags', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title of the photo you're uploading.)
        """
        super(UploadInputSet, self)._set_input('Title', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) A url for a photo to upload to Flickr. Required unless specifying the ImageFileContents.)
        """
        super(UploadInputSet, self)._set_input('URL', value)


class UploadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Upload Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class UploadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadResultSet(response, path)
