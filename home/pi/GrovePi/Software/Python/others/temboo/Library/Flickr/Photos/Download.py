# -*- coding: utf-8 -*-

###############################################################################
#
# Download
# Retrieves a photo from a constructed source URL and returns the file content as Base64 encoded data.
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

class Download(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Download Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Download, self).__init__(temboo_session, '/Library/Flickr/Photos/Download')


    def new_input_set(self):
        return DownloadInputSet()

    def _make_result_set(self, result, path):
        return DownloadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadChoreographyExecution(session, exec_id, path)

class DownloadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Download
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FarmID(self, value):
        """
        Set the value of the FarmID input for this Choreo. ((conditional, integer) The farm id associated with the photo. Required unless providing the URL.)
        """
        super(DownloadInputSet, self)._set_input('FarmID', value)
    def set_ImageType(self, value):
        """
        Set the value of the ImageType input for this Choreo. ((optional, string) The image type. Valid values are: jpg, png, or gif. Defaults to "jpg".)
        """
        super(DownloadInputSet, self)._set_input('ImageType', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((conditional, integer) The id of the photo you to download.)
        """
        super(DownloadInputSet, self)._set_input('PhotoID', value)
    def set_Secret(self, value):
        """
        Set the value of the Secret input for this Choreo. ((conditional, string) The secret associated with the photo. Required unless providing the URL.)
        """
        super(DownloadInputSet, self)._set_input('Secret', value)
    def set_ServerID(self, value):
        """
        Set the value of the ServerID input for this Choreo. ((conditional, integer) The server id associated with the photo. Required unless providing the URL.)
        """
        super(DownloadInputSet, self)._set_input('ServerID', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) The url to download the photo from. Required unless providing the Secret, ServerID, and FarmID parameters.)
        """
        super(DownloadInputSet, self)._set_input('URL', value)

class DownloadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Download Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The Base64 encoded image content.)
        """
        return self._output.get('Response', None)

class DownloadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadResultSet(response, path)
