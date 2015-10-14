# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Allows your application to submit free-form queries similar to the queries one might enter at the Wolfram|Alpha website.
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

class Query(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Query Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Query, self).__init__(temboo_session, '/Library/WolframAlpha/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

class QueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Query
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Wolfram|Alpha.)
        """
        super(QueryInputSet, self)._set_input('AppID', value)
    def set_Assumption(self, value):
        """
        Set the value of the Assumption input for this Choreo. ((optional, string) Up to 10 comma-seperated assumptions to narrow a query.  Wolfram|Alpha provides you with a list of assumptons in the response of a previous query.  Please consult the documentation for more details.)
        """
        super(QueryInputSet, self)._set_input('Assumption', value)
    def set_Async(self, value):
        """
        Set the value of the Async input for this Choreo. ((optional, boolean) Set to true to specify that asynchronous mode should be used. This allows partial results to come back before all the pods are computed.)
        """
        super(QueryInputSet, self)._set_input('Async', value)
    def set_ExcludePodID(self, value):
        """
        Set the value of the ExcludePodID input for this Choreo. ((optional, string) Specifies the IDs of the pod(s) to exlude from the response. All pod IDs are returned by default.)
        """
        super(QueryInputSet, self)._set_input('ExcludePodID', value)
    def set_FormatTimeout(self, value):
        """
        Set the value of the FormatTimeout input for this Choreo. ((optional, decimal) The number of seconds to allow Wolfram Alpha to spend in the "format" stage for the entire collection of pods. Default value is 8.0.)
        """
        super(QueryInputSet, self)._set_input('FormatTimeout', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The desired result formats separated by commas. Valid values are image, plaintext, minput, moutput, cell, mathml, imagemap, sound, wav. Defaults to "plaintext,image".)
        """
        super(QueryInputSet, self)._set_input('Format', value)
    def set_IgnoreCase(self, value):
        """
        Set the value of the IgnoreCase input for this Choreo. ((optional, boolean) Whether to force Wolfram Alpha to ignore case in queries. Defaults to false.)
        """
        super(QueryInputSet, self)._set_input('IgnoreCase', value)
    def set_IncludePodID(self, value):
        """
        Set the value of the IncludePodID input for this Choreo. ((optional, string) Specifies the IDs of the pod(s) to include in the response. All pod IDs are returned by default.)
        """
        super(QueryInputSet, self)._set_input('IncludePodID', value)
    def set_Input(self, value):
        """
        Set the value of the Input input for this Choreo. ((required, string) Specifies the input string (e.g., "5 largest countries").)
        """
        super(QueryInputSet, self)._set_input('Input', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) When query results depend on your location, use this parameter to specify a latitude point.)
        """
        super(QueryInputSet, self)._set_input('Latitude', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((optional, string) When query results depend on your location, use this parameter to specify a location such as "Los Angeles, CA", or "Madrid".)
        """
        super(QueryInputSet, self)._set_input('Location', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) When query results depend on your location, use this parameter to specify a longitude point.)
        """
        super(QueryInputSet, self)._set_input('Longitude', value)
    def set_Magnification(self, value):
        """
        Set the value of the Magnification input for this Choreo. ((optional, decimal) Controls the magnification of pod images. The default value is 1.0, indicating no magnification.)
        """
        super(QueryInputSet, self)._set_input('Magnification', value)
    def set_MaxWidth(self, value):
        """
        Set the value of the MaxWidth input for this Choreo. ((optional, integer) Used to change the default width of pod images. Width and MaxWidth apply to images of text and tables. This can be used to avoid undesirable line breaks if the value of Width is too small.)
        """
        super(QueryInputSet, self)._set_input('MaxWidth', value)
    def set_ParseTimeout(self, value):
        """
        Set the value of the ParseTimeout input for this Choreo. ((optional, decimal) The number of seconds to allow Wolfram Alpha to spend in the "parsing" stage of processing. Default value is 5.0.)
        """
        super(QueryInputSet, self)._set_input('ParseTimeout', value)
    def set_PlotWidth(self, value):
        """
        Set the value of the PlotWidth input for this Choreo. ((optional, integer) Controls the width at which plots and graphics are rendered. The default value is 200 pixels.)
        """
        super(QueryInputSet, self)._set_input('PlotWidth', value)
    def set_PodIndex(self, value):
        """
        Set the value of the PodIndex input for this Choreo. ((optional, string) Specifies the index of the pod(s) to return. This is an alternative to specifying pods by title or ID. You can give a single number or a sequence like "2,3,5".)
        """
        super(QueryInputSet, self)._set_input('PodIndex', value)
    def set_PodState(self, value):
        """
        Set the value of the PodState input for this Choreo. ((optional, string) Specifies a pod state change, which replaces a pod with a modified version, such as a switch from Imperial to metric units.)
        """
        super(QueryInputSet, self)._set_input('PodState', value)
    def set_PodTimeout(self, value):
        """
        Set the value of the PodTimeout input for this Choreo. ((optional, decimal) The number of seconds to allow Wolfram Alpha to spend in the "format" stage for any one pod. Default value is 4.0.)
        """
        super(QueryInputSet, self)._set_input('PodTimeout', value)
    def set_PodTitle(self, value):
        """
        Set the value of the PodTitle input for this Choreo. ((optional, string) Specifies the titles of the pod(s) to include in the response. All pod titles are returned by default. You can use * as a wildcard to match zero or more characters in pod titles.)
        """
        super(QueryInputSet, self)._set_input('PodTitle', value)
    def set_Reinterpret(self, value):
        """
        Set the value of the Reinterpret input for this Choreo. ((optional, boolean) Whether to allow Wolfram Alpha to reinterpret queries that would otherwise not be understood. Defaults to false.)
        """
        super(QueryInputSet, self)._set_input('Reinterpret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format for the response. Valid values are JSON and XML. This will be ignored when providng an XPath query because results are returned as a string or JSON depending on the Mode specified.)
        """
        super(QueryInputSet, self)._set_input('ResponseFormat', value)
    def set_ScanTimeout(self, value):
        """
        Set the value of the ScanTimeout input for this Choreo. ((optional, decimal) The number of seconds to allow Wolfram Alpha to compute results in the "scan" stage of processing. Default value is 3.0.)
        """
        super(QueryInputSet, self)._set_input('ScanTimeout', value)
    def set_Scanner(self, value):
        """
        Set the value of the Scanner input for this Choreo. ((optional, string) Specifies that only pods produced by the given scanner should be returned. (e.g. Numeric, Music).  Defaults to all pods.)
        """
        super(QueryInputSet, self)._set_input('Scanner', value)
    def set_Translation(self, value):
        """
        Set the value of the Translation input for this Choreo. ((optional, boolean) Whether to allow Wolfram Alpha to try to translate simple queries into English. Defaults to true.)
        """
        super(QueryInputSet, self)._set_input('Translation', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Lets you specify the preferred measurement system, either "metric" or "nonmetric" (U.S. customary units).)
        """
        super(QueryInputSet, self)._set_input('Units', value)
    def set_Width(self, value):
        """
        Set the value of the Width input for this Choreo. ((optional, integer) Used to change the default width of pod images. The default is 500 pixels. Width and MaxWidth apply to images of text and tables.)
        """
        super(QueryInputSet, self)._set_input('Width', value)
    def set_XPathMode(self, value):
        """
        Set the value of the XPathMode input for this Choreo. ((optional, string) Valid values are "select" (the default) or "recursive". Recursive mode will iterate using the provided XPath. Select mode will return the first match at the position indicated by the provided XPath.)
        """
        super(QueryInputSet, self)._set_input('XPathMode', value)
    def set_XPathRegex(self, value):
        """
        Set the value of the XPathRegex input for this Choreo. ((optional, string) A regular expression that can be applied to the result of the XPath query provided.)
        """
        super(QueryInputSet, self)._set_input('XPathRegex', value)
    def set_XPath(self, value):
        """
        Set the value of the XPath input for this Choreo. ((optional, string) An XPath query to apply to the API results.)
        """
        super(QueryInputSet, self)._set_input('XPath', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wolfram Alpha.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
