# -*- coding: utf-8 -*-

###############################################################################
#
# GetReportById
# Returns the contents of a report with a given report id.
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

class GetReportById(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReportById Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReportById, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportById')


    def new_input_set(self):
        return GetReportByIdInputSet()

    def _make_result_set(self, result, path):
        return GetReportByIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportByIdChoreographyExecution(session, exec_id, path)

class GetReportByIdInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReportById
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetReportByIdInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetReportByIdInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetReportByIdInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetReportByIdInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetReportByIdInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(GetReportByIdInputSet, self)._set_input('MWSAuthToken', value)
    def set_ReportId(self, value):
        """
        Set the value of the ReportId input for this Choreo. ((required, integer) The id of the report to retrieve.)
        """
        super(GetReportByIdInputSet, self)._set_input('ReportId', value)

class GetReportByIdResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReportById Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon which contains the contents of the report requested. This is typically a flat file or XML information.)
        """
        return self._output.get('Response', None)
    def get_ContentMD5Header(self):
        """
        Retrieve the value for the "ContentMD5Header" output from this Choreo execution. ((string) )
        """
        return self._output.get('ContentMD5Header', None)

class GetReportByIdChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReportByIdResultSet(response, path)
