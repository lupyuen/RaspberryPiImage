# -*- coding: utf-8 -*-

###############################################################################
#
# PostComment
# Posts a comment about a user's activity.
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

class PostComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PostComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PostComment, self).__init__(temboo_session, '/Library/RunKeeper/CommentThreads/PostComment')


    def new_input_set(self):
        return PostCommentInputSet()

    def _make_result_set(self, result, path):
        return PostCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PostCommentChoreographyExecution(session, exec_id, path)

class PostCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PostComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((required, string) The comment text.)
        """
        super(PostCommentInputSet, self)._set_input('Comment', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(PostCommentInputSet, self)._set_input('AccessToken', value)
    def set_URI(self, value):
        """
        Set the value of the URI input for this Choreo. ((required, string) The URI of the activity thread to post a comment to (e.g., /fitnessActivities/327844402).)
        """
        super(PostCommentInputSet, self)._set_input('URI', value)

class PostCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PostComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class PostCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PostCommentResultSet(response, path)
