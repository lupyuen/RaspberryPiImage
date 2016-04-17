# -*- coding: utf-8 -*-

###############################################################################
#
# Person
# Returns members of Congress and U.S. Presidents since the founding of the nation.
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

class Person(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Person Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Person, self).__init__(temboo_session, '/Library/GovTrack/Person')


    def new_input_set(self):
        return PersonInputSet()

    def _make_result_set(self, result, path):
        return PersonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PersonChoreographyExecution(session, exec_id, path)

class PersonInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Person
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return in the response. Use double-underscores to span relationships (e.g. person__firstname).)
        """
        super(PersonInputSet, self)._set_input('Fields', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) The person's gender (male or female). For historical data, gender is sometimes not specified. Filter operators allowed. Sortable.)
        """
        super(PersonInputSet, self)._set_input('Gender', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The representative's last name. Filter operators allowed. Sortable.)
        """
        super(PersonInputSet, self)._set_input('LastName', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 100 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        super(PersonInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offset the results by the number given, useful for paging through results.)
        """
        super(PersonInputSet, self)._set_input('Offset', value)
    def set_PersonID(self, value):
        """
        Set the value of the PersonID input for this Choreo. ((optional, integer) The ID number for a person to retrieve. When using this input, all other filter parameters are ignored, and a single record is returned.)
        """
        super(PersonInputSet, self)._set_input('PersonID', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) Filters according to a full-text search on the object.)
        """
        super(PersonInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(PersonInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of the variables that is listed as 'Sortable' in the description. Ex: '-lastname')
        """
        super(PersonInputSet, self)._set_input('Sort', value)

class PersonResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Person Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from GovTrack.)
        """
        return self._output.get('Response', None)

class PersonChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PersonResultSet(response, path)
