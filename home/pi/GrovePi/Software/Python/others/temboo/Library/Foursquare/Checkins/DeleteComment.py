# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteComment
# Removes a comment to a specified check-in.
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

class DeleteComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteComment, self).__init__(temboo_session, '/Library/Foursquare/Checkins/DeleteComment')


    def new_input_set(self):
        return DeleteCommentInputSet()

    def _make_result_set(self, result, path):
        return DeleteCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCommentChoreographyExecution(session, exec_id, path)

class DeleteCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in associated with the comment you want to remove.)
        """
        super(DeleteCommentInputSet, self)._set_input('CheckinID', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The id of the comment to remove.)
        """
        super(DeleteCommentInputSet, self)._set_input('CommentID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(DeleteCommentInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DeleteCommentInputSet, self)._set_input('ResponseFormat', value)

class DeleteCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class DeleteCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteCommentResultSet(response, path)
