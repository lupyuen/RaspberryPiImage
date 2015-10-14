# -*- coding: utf-8 -*-

###############################################################################
#
# RetrievePostsWithTag
# Retrieves posts that have a given tag.
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

class RetrievePostsWithTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrievePostsWithTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrievePostsWithTag, self).__init__(temboo_session, '/Library/Tumblr/Tagged/RetrievePostsWithTag')


    def new_input_set(self):
        return RetrievePostsWithTagInputSet()

    def _make_result_set(self, result, path):
        return RetrievePostsWithTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrievePostsWithTagChoreographyExecution(session, exec_id, path)

class RetrievePostsWithTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrievePostsWithTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('APIKey', value)
    def set_Before(self, value):
        """
        Set the value of the Before input for this Choreo. ((optional, string) The timestamp of when you'd like to see posts before (e.g. 1363716547).)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('Before', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Specifies the post format to return. Valid values are: text (plain text, no html) or raw (as entered by the user).)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('Filter', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of posts to return: 1- 20. Defaults to 20.)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The post number to start at. Defaults to 0.)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('ResponseFormat', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) The tag on the posts you'd like to retrieve.)
        """
        super(RetrievePostsWithTagInputSet, self)._set_input('Tag', value)

class RetrievePostsWithTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrievePostsWithTag Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrievePostsWithTagChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrievePostsWithTagResultSet(response, path)
