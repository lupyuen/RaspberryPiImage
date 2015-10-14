# -*- coding: utf-8 -*-

###############################################################################
#
# ListFolderContents
# Retrieves metadata (including folder contents) for a folder or file in Dropbox.
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

class ListFolderContents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListFolderContents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListFolderContents, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/ListFolderContents')


    def new_input_set(self):
        return ListFolderContentsInputSet()

    def _make_result_set(self, result, path):
        return ListFolderContentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFolderContentsChoreographyExecution(session, exec_id, path)

class ListFolderContentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListFolderContents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ListFolderContentsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ListFolderContentsInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(ListFolderContentsInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(ListFolderContentsInputSet, self)._set_input('AppSecret', value)
    def set_FileLimit(self, value):
        """
        Set the value of the FileLimit input for this Choreo. ((optional, integer) Dropbox will not return a list that exceeds this specified limit. Defaults to 10,000.)
        """
        super(ListFolderContentsInputSet, self)._set_input('FileLimit', value)
    def set_Folder(self, value):
        """
        Set the value of the Folder input for this Choreo. ((optional, string) The path to a folder for which to retrieve metadata (i.e. /RootFolder/SubFolder). Note that a path to file can also be passed.)
        """
        super(ListFolderContentsInputSet, self)._set_input('Folder', value)
    def set_Hash(self, value):
        """
        Set the value of the Hash input for this Choreo. ((optional, string) The value of a hash field from a previous request to get metadata on a folder. When provided, a 304 (not Modified) status code is returned instead of a folder listing if no changes have been made.)
        """
        super(ListFolderContentsInputSet, self)._set_input('Hash', value)
    def set_IncludeDeleted(self, value):
        """
        Set the value of the IncludeDeleted input for this Choreo. ((optional, boolean) Only applicable when List is set. If this parameter is set to true, contents will include the metadata of deleted children.)
        """
        super(ListFolderContentsInputSet, self)._set_input('IncludeDeleted', value)
    def set_List(self, value):
        """
        Set the value of the List input for this Choreo. ((optional, boolean) If true (the default), the folder's metadata will include a contents field with a list of metadata entries for the contents of the folder.)
        """
        super(ListFolderContentsInputSet, self)._set_input('List', value)
    def set_Locale(self, value):
        """
        Set the value of the Locale input for this Choreo. ((optional, string) If your app supports any language other than English, insert the appropriate IETF language tag, and the metadata returned will have its size field translated based on the given locale (e.g., pt-BR).)
        """
        super(ListFolderContentsInputSet, self)._set_input('Locale', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(ListFolderContentsInputSet, self)._set_input('ResponseFormat', value)
    def set_Revision(self, value):
        """
        Set the value of the Revision input for this Choreo. ((optional, string) When including a particular revision number, only the metadata for that revision will be returned.)
        """
        super(ListFolderContentsInputSet, self)._set_input('Revision', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((optional, string) Defaults to "auto" which automatically determines the root folder using your app's permission level. Other options are "sandbox" (App Folder) and "dropbox" (Full Dropbox).)
        """
        super(ListFolderContentsInputSet, self)._set_input('Root', value)

class ListFolderContentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListFolderContents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Dropbox.)
        """
        return self._output.get('ResponseStatusCode', None)

class ListFolderContentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListFolderContentsResultSet(response, path)
