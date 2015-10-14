# -*- coding: utf-8 -*-

###############################################################################
#
# Picture
# Retrieves a person's profile picture.
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

class Picture(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Picture Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Picture, self).__init__(temboo_session, '/Library/Facebook/Reading/Picture')


    def new_input_set(self):
        return PictureInputSet()

    def _make_result_set(self, result, path):
        return PictureResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PictureChoreographyExecution(session, exec_id, path)

class PictureInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Picture
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved from the final step of the OAuth process. This is not required when providing a ProfileID.)
        """
        super(PictureInputSet, self)._set_input('AccessToken', value)
    def set_Height(self, value):
        """
        Set the value of the Height input for this Choreo. ((optional, integer) Restricts the picture height to this size in pixels.)
        """
        super(PictureInputSet, self)._set_input('Height', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((conditional, string) The id of the profile to retrieve a profile picture for. Defaults to "me" indicating the authenticated user.)
        """
        super(PictureInputSet, self)._set_input('ProfileID', value)
    def set_Redirect(self, value):
        """
        Set the value of the Redirect input for this Choreo. ((optional, boolean) By default, the picture itself is returned as Base64 encoded data.and not a JSON. To return a JSON response, set Redirect to "false".)
        """
        super(PictureInputSet, self)._set_input('Redirect', value)
    def set_ReturnSSLResources(self, value):
        """
        Set the value of the ReturnSSLResources input for this Choreo. ((optional, boolean) Deprecated (retained for backward compatibility only).)
        """
        super(PictureInputSet, self)._set_input('ReturnSSLResources', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The size of the image to retrieve. Valid values: square (50x50), small (50 pixels wide, variable height), normal (100 pixels wide, variable height), and large (about 200 pixels wide, variable height))
        """
        super(PictureInputSet, self)._set_input('Type', value)
    def set_Width(self, value):
        """
        Set the value of the Width input for this Choreo. ((optional, integer) Restricts the picture width to this size in pixels. When Height and Width are both used, the image will be scaled as close to the dimensions as possible and then cropped down.)
        """
        super(PictureInputSet, self)._set_input('Width', value)

class PictureResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Picture Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Contains the Base64 encoded value of the image retrieved from Facebook by default. When setting Redirect to "false", the response is a JSON string containing the image URL.)
        """
        return self._output.get('Response', None)

class PictureChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PictureResultSet(response, path)
