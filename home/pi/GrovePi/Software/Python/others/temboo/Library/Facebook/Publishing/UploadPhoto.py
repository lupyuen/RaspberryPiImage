# -*- coding: utf-8 -*-

###############################################################################
#
# UploadPhoto
# Uploads a photo to a given album.
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

class UploadPhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadPhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UploadPhoto, self).__init__(temboo_session, '/Library/Facebook/Publishing/UploadPhoto')


    def new_input_set(self):
        return UploadPhotoInputSet()

    def _make_result_set(self, result, path):
        return UploadPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadPhotoChoreographyExecution(session, exec_id, path)

class UploadPhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadPhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(UploadPhotoInputSet, self)._set_input('AccessToken', value)
    def set_AlbumID(self, value):
        """
        Set the value of the AlbumID input for this Choreo. ((optional, string) The id of the album to upload the photo to.)
        """
        super(UploadPhotoInputSet, self)._set_input('AlbumID', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message to attach to the photo.)
        """
        super(UploadPhotoInputSet, self)._set_input('Message', value)
    def set_Photo(self, value):
        """
        Set the value of the Photo input for this Choreo. ((conditional, string) The Base64 encoded image to upload. This is required unless using the URL input to publish the photo.)
        """
        super(UploadPhotoInputSet, self)._set_input('Photo', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The ID of a location where the photo was taken.)
        """
        super(UploadPhotoInputSet, self)._set_input('Place', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UploadPhotoInputSet, self)._set_input('ResponseFormat', value)
    def set_Source(self, value):
        """
        Set the value of the Source input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(UploadPhotoInputSet, self)._set_input('Source', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) A URL to a hosted photo that should be uploaded. This is required unless providing a Base64 encoded image for the Photo input.)
        """
        super(UploadPhotoInputSet, self)._set_input('URL', value)


class UploadPhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadPhoto Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UploadPhotoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadPhotoResultSet(response, path)
