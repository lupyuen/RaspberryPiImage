# -*- coding: utf-8 -*-

###############################################################################
#
# GetListByID
# Retrieves a list of NPR categories from a specified list type ID.
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

class GetListByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetListByID, self).__init__(temboo_session, '/Library/NPR/StoryFinder/GetListByID')


    def new_input_set(self):
        return GetListByIDInputSet()

    def _make_result_set(self, result, path):
        return GetListByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListByIDChoreographyExecution(session, exec_id, path)

class GetListByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChildrenOf(self, value):
        """
        Set the value of the ChildrenOf input for this Choreo. ((optional, integer) Returns only items which are assigned to the given topic ID. For example, if Id=3006 and ChildrenOf=1008 only recent series which are assigned to "Arts & Life" are returned.)
        """
        super(GetListByIDInputSet, self)._set_input('ChildrenOf', value)
    def set_HideChildren(self, value):
        """
        Set the value of the HideChildren input for this Choreo. ((optional, boolean) If set to "1", returns only topics which are not subtopics of another topic.)
        """
        super(GetListByIDInputSet, self)._set_input('HideChildren', value)
    def set_Id(self, value):
        """
        Set the value of the Id input for this Choreo. ((required, integer) The id of the list type you want to retrieve. For example, the list type id for Music Genres is 3218).)
        """
        super(GetListByIDInputSet, self)._set_input('Id', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are xml (the default), and json.)
        """
        super(GetListByIDInputSet, self)._set_input('ResponseFormat', value)
    def set_StoryCountAll(self, value):
        """
        Set the value of the StoryCountAll input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        super(GetListByIDInputSet, self)._set_input('StoryCountAll', value)
    def set_StoryCountMonth(self, value):
        """
        Set the value of the StoryCountMonth input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        super(GetListByIDInputSet, self)._set_input('StoryCountMonth', value)
    def set_StoryCountToday(self, value):
        """
        Set the value of the StoryCountToday input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        super(GetListByIDInputSet, self)._set_input('StoryCountToday', value)

class GetListByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class GetListByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListByIDResultSet(response, path)
