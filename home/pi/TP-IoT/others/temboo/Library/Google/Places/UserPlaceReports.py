# -*- coding: utf-8 -*-

###############################################################################
#
# UserPlaceReports
# Add a new Place to Google Places.
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

class UserPlaceReports(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserPlaceReports Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserPlaceReports, self).__init__(temboo_session, '/Library/Google/Places/UserPlaceReports')


    def new_input_set(self):
        return UserPlaceReportsInputSet()

    def _make_result_set(self, result, path):
        return UserPlaceReportsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserPlaceReportsChoreographyExecution(session, exec_id, path)

class UserPlaceReportsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserPlaceReports
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_POSTForm(self, value):
        """
        Set the value of the POSTForm input for this Choreo. ((optional, json) A JSON request body containing the information about the place. This can be specified as an alternative to specifying individual place properties. See Choreo notes for details about formatting.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('POSTForm', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((conditional, decimal) The accuracy of the location signal on which this request is based, expressed in meters.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Accuracy', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((optional, string) The address of the place you wish to add.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Address', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The API Key provided by Google.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Key', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((conditional, string) The language in which the place's name is being reported.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point for the place you wish to add (e.g., 38.898717).)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate for the place you wish to add (e.g., -77.035974).)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Longitude', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The full text name of the place)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Name', value)
    def set_PhoneNumber(self, value):
        """
        Set the value of the PhoneNumber input for this Choreo. ((optional, string) The phone number associated with the place.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('PhoneNumber', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Sensor', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((required, json) A JSON array of categories in which this place belongs.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Types', value)
    def set_Website(self, value):
        """
        Set the value of the Website input for this Choreo. ((optional, string) A URL pointing to the authoritative website for this Place, such as a business home page.)
        """
        super(UserPlaceReportsInputSet, self)._set_input('Website', value)

class UserPlaceReportsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserPlaceReports Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class UserPlaceReportsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserPlaceReportsResultSet(response, path)
