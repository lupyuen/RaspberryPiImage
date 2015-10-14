# -*- coding: utf-8 -*-

###############################################################################
#
# ListPublicPhotos
# Obtain a list of public photos for a given user.
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

class ListPublicPhotos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPublicPhotos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListPublicPhotos, self).__init__(temboo_session, '/Library/Flickr/Photos/ListPublicPhotos')


    def new_input_set(self):
        return ListPublicPhotosInputSet()

    def _make_result_set(self, result, path):
        return ListPublicPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPublicPhotosChoreographyExecution(session, exec_id, path)

class ListPublicPhotosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPublicPhotos
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ListPublicPhotosInputSet, self)._set_input('APIKey', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-separated list returning additional photo information such as: license, description, date_upload, date_taken.  Additional options are listed on this method's API doc page.)
        """
        super(ListPublicPhotosInputSet, self)._set_input('Extras', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specify the page of photos that is to be returned.  If unspecified, the first page is returned.)
        """
        super(ListPublicPhotosInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Specify how many photos to display per page. Default is set to: 100. The mamimum allowed value is: 500.)
        """
        super(ListPublicPhotosInputSet, self)._set_input('PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ListPublicPhotosInputSet, self)._set_input('ResponseFormat', value)
    def set_SafeSearch(self, value):
        """
        Set the value of the SafeSearch input for this Choreo. ((optional, integer) Specify a safe search setting by entering: 1 (for safe), 2 (moderate), 3 (restricted).  Default is set to: 1 (safe).)
        """
        super(ListPublicPhotosInputSet, self)._set_input('SafeSearch', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) Enter the NSID of the user whose public photos are being retrieved.)
        """
        super(ListPublicPhotosInputSet, self)._set_input('UserID', value)

class ListPublicPhotosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPublicPhotos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPublicPhotosChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListPublicPhotosResultSet(response, path)
