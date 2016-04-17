# -*- coding: utf-8 -*-

###############################################################################
#
# RequestReport
# Creates a report request and submits the request to Amazon MWS.
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

class RequestReport(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RequestReport Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RequestReport, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/RequestReport')


    def new_input_set(self):
        return RequestReportInputSet()

    def _make_result_set(self, result, path):
        return RequestReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RequestReportChoreographyExecution(session, exec_id, path)

class RequestReportInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RequestReport
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(RequestReportInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(RequestReportInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(RequestReportInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(RequestReportInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) The end of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(RequestReportInputSet, self)._set_input('EndDate', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(RequestReportInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(RequestReportInputSet, self)._set_input('MWSAuthToken', value)
    def set_ReportOptions(self, value):
        """
        Set the value of the ReportOptions input for this Choreo. ((optional, string) A Boolean value that shows or hides an additional column of information on several order reports. When set to ShowSalesChannel=true, an additional column is added showing the sales channel.)
        """
        super(RequestReportInputSet, self)._set_input('ReportOptions', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value. Defaults to _GET_FLAT_FILE_OPEN_LISTINGS_DATA_.)
        """
        super(RequestReportInputSet, self)._set_input('ReportType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(RequestReportInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) The start of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(RequestReportInputSet, self)._set_input('StartDate', value)

class RequestReportResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RequestReport Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        return self._output.get('ReportRequestId', None)

class RequestReportChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RequestReportResultSet(response, path)
