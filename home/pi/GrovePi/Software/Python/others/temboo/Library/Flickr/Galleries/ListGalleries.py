# -*- coding: utf-8 -*-

###############################################################################
#
# ListGalleries
# Get a gallery list for a specfied user.
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

class ListGalleries(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListGalleries Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListGalleries, self).__init__(temboo_session, '/Library/Flickr/Galleries/ListGalleries')


    def new_input_set(self):
        return ListGalleriesInputSet()

    def _make_result_set(self, result, path):
        return ListGalleriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListGalleriesChoreographyExecution(session, exec_id, path)

class ListGalleriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListGalleries
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ListGalleriesInputSet, self)._set_input('APIKey', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Enter the number of results pages to be returned.  Default is: 1.)
        """
        super(ListGalleriesInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Specify the number of galleries that are to be returned per page.  If null, defaults to 100 galleries returned.  Maximum is 500.)
        """
        super(ListGalleriesInputSet, self)._set_input('PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ListGalleriesInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) Provide the NSID for the user whose gallery list(s) are to be retreived.)
        """
        super(ListGalleriesInputSet, self)._set_input('UserID', value)

class ListGalleriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListGalleries Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListGalleriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListGalleriesResultSet(response, path)
