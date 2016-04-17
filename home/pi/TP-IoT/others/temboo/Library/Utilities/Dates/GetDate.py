# -*- coding: utf-8 -*-

###############################################################################
#
# GetDate
# Formats a specified timestamp, or generates the current date in a desired format.
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

class GetDate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDate, self).__init__(temboo_session, '/Library/Utilities/Dates/GetDate')


    def new_input_set(self):
        return GetDateInputSet()

    def _make_result_set(self, result, path):
        return GetDateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDateChoreographyExecution(session, exec_id, path)

class GetDateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AddDays(self, value):
        """
        Set the value of the AddDays input for this Choreo. ((optional, integer) Adds the specified number of days to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddDays', value)
    def set_AddHours(self, value):
        """
        Set the value of the AddHours input for this Choreo. ((optional, integer) Adds the specified number of hours to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddHours', value)
    def set_AddMinutes(self, value):
        """
        Set the value of the AddMinutes input for this Choreo. ((optional, integer) Adds the specified number of minutes to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddMinutes', value)
    def set_AddMonths(self, value):
        """
        Set the value of the AddMonths input for this Choreo. ((optional, integer) Adds the specified number of months to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddMonths', value)
    def set_AddSeconds(self, value):
        """
        Set the value of the AddSeconds input for this Choreo. ((optional, integer) Adds the specified number of seconds to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddSeconds', value)
    def set_AddYears(self, value):
        """
        Set the value of the AddYears input for this Choreo. ((optional, integer) Adds the specified number of years to the specified date serial number. A negative number will subtract.)
        """
        super(GetDateInputSet, self)._set_input('AddYears', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((conditional, string) The format that the timestamp should be in. Java SimpleDateFormat conventions are supported. Defaults to "yyyy-MM-dd HH:mm:ss".)
        """
        super(GetDateInputSet, self)._set_input('Format', value)
    def set_LocaleCountry(self, value):
        """
        Set the value of the LocaleCountry input for this Choreo. ((optional, string) An ISO country code to specify locale.)
        """
        super(GetDateInputSet, self)._set_input('LocaleCountry', value)
    def set_LocaleLanguage(self, value):
        """
        Set the value of the LocaleLanguage input for this Choreo. ((optional, string) An ISO language code to specify locale.)
        """
        super(GetDateInputSet, self)._set_input('LocaleLanguage', value)
    def set_LocaleVariant(self, value):
        """
        Set the value of the LocaleVariant input for this Choreo. ((optional, string) A local variant code such as "NY" to add additional context for a locale.)
        """
        super(GetDateInputSet, self)._set_input('LocaleVariant', value)
    def set_SetDay(self, value):
        """
        Set the value of the SetDay input for this Choreo. ((optional, integer) Sets the day of month (1-31) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetDay', value)
    def set_SetHour(self, value):
        """
        Set the value of the SetHour input for this Choreo. ((optional, integer) Sets the hours (0-23) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetHour', value)
    def set_SetMinute(self, value):
        """
        Set the value of the SetMinute input for this Choreo. ((optional, integer) Sets the minutes (0-59) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetMinute', value)
    def set_SetMonth(self, value):
        """
        Set the value of the SetMonth input for this Choreo. ((optional, integer) Sets the month (1-12) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetMonth', value)
    def set_SetSecond(self, value):
        """
        Set the value of the SetSecond input for this Choreo. ((optional, integer) Sets the seconds (0-59) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetSecond', value)
    def set_SetYear(self, value):
        """
        Set the value of the SetYear input for this Choreo. ((optional, integer) Sets the year (such as 1989) of the specified date serial number.)
        """
        super(GetDateInputSet, self)._set_input('SetYear', value)
    def set_TimeZone(self, value):
        """
        Set the value of the TimeZone input for this Choreo. ((optional, string) The timezone to use for the date formatting function. Defaults to UTC.)
        """
        super(GetDateInputSet, self)._set_input('TimeZone', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((conditional, date) A number representing the desired formatted date and time, expressed as the number of milliseconds since January 1, 1970 (epoch time). If not provided, this defaults to NOW().)
        """
        super(GetDateInputSet, self)._set_input('Timestamp', value)

class GetDateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_FormattedDate(self):
        """
        Retrieve the value for the "FormattedDate" output from this Choreo execution. ((date) The formatted version of the timestamp.)
        """
        return self._output.get('FormattedDate', None)

class GetDateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDateResultSet(response, path)
