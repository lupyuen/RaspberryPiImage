# -*- coding: utf-8 -*-

###############################################################################
#
# RenameTag
# Renames a specified tag.
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

class RenameTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RenameTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RenameTag, self).__init__(temboo_session, '/Library/Delicious/RenameTag')


    def new_input_set(self):
        return RenameTagInputSet()

    def _make_result_set(self, result, path):
        return RenameTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameTagChoreographyExecution(session, exec_id, path)

class RenameTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RenameTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NewTag(self, value):
        """
        Set the value of the NewTag input for this Choreo. ((required, string) The new tag name.)
        """
        super(RenameTagInputSet, self)._set_input('NewTag', value)
    def set_OldTag(self, value):
        """
        Set the value of the OldTag input for this Choreo. ((required, string) The existing tag to rename.)
        """
        super(RenameTagInputSet, self)._set_input('OldTag', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        super(RenameTagInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        super(RenameTagInputSet, self)._set_input('Username', value)

class RenameTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RenameTag Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class RenameTagChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RenameTagResultSet(response, path)
