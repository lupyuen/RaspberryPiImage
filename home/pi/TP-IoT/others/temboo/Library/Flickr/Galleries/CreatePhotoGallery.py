# -*- coding: utf-8 -*-

###############################################################################
#
# CreatePhotoGallery
# Creates a new photo gallery.
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

class CreatePhotoGallery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreatePhotoGallery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreatePhotoGallery, self).__init__(temboo_session, '/Library/Flickr/Galleries/CreatePhotoGallery')


    def new_input_set(self):
        return CreatePhotoGalleryInputSet()

    def _make_result_set(self, result, path):
        return CreatePhotoGalleryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePhotoGalleryChoreographyExecution(session, exec_id, path)

class CreatePhotoGalleryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreatePhotoGallery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((required, string) A short description for the gallery.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('Description', value)
    def set_PrimaryPhotoID(self, value):
        """
        Set the value of the PrimaryPhotoID input for this Choreo. ((optional, integer) The first photo to add to your gallery.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('PrimaryPhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('ResponseFormat', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The name of the gallery.)
        """
        super(CreatePhotoGalleryInputSet, self)._set_input('Title', value)

class CreatePhotoGalleryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreatePhotoGallery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class CreatePhotoGalleryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreatePhotoGalleryResultSet(response, path)
