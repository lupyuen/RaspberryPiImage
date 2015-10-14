# -*- coding: utf-8 -*-

###############################################################################
#
# ZipFile
# Creates a zipped version of the specified Dropbox file and returns a shareable link to the new compressed file.
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

class ZipFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ZipFile, self).__init__(temboo_session, '/Library/Dropbox/FileOperations/ZipFile')


    def new_input_set(self):
        return ZipFileInputSet()

    def _make_result_set(self, result, path):
        return ZipFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipFileChoreographyExecution(session, exec_id, path)

class ZipFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ZipFileInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ZipFileInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(ZipFileInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(ZipFileInputSet, self)._set_input('AppSecret', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the Dropbox file you want to zip.)
        """
        super(ZipFileInputSet, self)._set_input('FileName', value)
    def set_Folder(self, value):
        """
        Set the value of the Folder input for this Choreo. ((conditional, string) The name of the folder that contains the file you want to zip. A path to a sub-folder is also valid (i.e. RootFolder/SubFolder). Not required if the file is at the root level.)
        """
        super(ZipFileInputSet, self)._set_input('Folder', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((optional, string) Defaults to "auto" which automatically determines the root folder using your app's permission level. Other options are "sandbox" (App Folder) and "dropbox" (Full Dropbox).)
        """
        super(ZipFileInputSet, self)._set_input('Root', value)
    def set_ZipFileLocation(self, value):
        """
        Set the value of the ZipFileLocation input for this Choreo. ((optional, string) The name of the folder to put the new zip file in.A path to a sub-folder is also valid (i.e. RootFolder/SubFolder).  When not specified, the zip file will be put in the root folder.)
        """
        super(ZipFileInputSet, self)._set_input('ZipFileLocation', value)
    def set_ZipFileName(self, value):
        """
        Set the value of the ZipFileName input for this Choreo. ((optional, string) The name of the zip file that will be created. If not specified, the original file name will be used with a .zip extension.)
        """
        super(ZipFileInputSet, self)._set_input('ZipFileName', value)

class ZipFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The shared link for the new zip file.)
        """
        return self._output.get('URL', None)

class ZipFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ZipFileResultSet(response, path)
