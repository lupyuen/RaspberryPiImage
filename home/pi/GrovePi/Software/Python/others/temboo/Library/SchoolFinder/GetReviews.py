# -*- coding: utf-8 -*-

###############################################################################
#
# GetReviews
# Returns a list of the most recent school reviews and parent rating for a single school.
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

class GetReviews(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReviews Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReviews, self).__init__(temboo_session, '/Library/SchoolFinder/GetReviews')


    def new_input_set(self):
        return GetReviewsInputSet()

    def _make_result_set(self, result, path):
        return GetReviewsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReviewsChoreographyExecution(session, exec_id, path)

class GetReviewsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReviews
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        super(GetReviewsInputSet, self)._set_input('APIKey', value)
    def set_NCES(self, value):
        """
        Set the value of the NCES input for this Choreo. ((conditional, string) The National Center for Education Statistics (NCES) id of the school. NCES or SchoolID are required.)
        """
        super(GetReviewsInputSet, self)._set_input('NCES', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        super(GetReviewsInputSet, self)._set_input('ResponseFormat', value)
    def set_SchoolID(self, value):
        """
        Set the value of the SchoolID input for this Choreo. ((conditional, string) The Education.com id of the school you want to find. NCES or SchoolID are required.)
        """
        super(GetReviewsInputSet, self)._set_input('SchoolID', value)

class GetReviewsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReviews Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class GetReviewsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReviewsResultSet(response, path)
