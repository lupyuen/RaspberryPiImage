###############################################################################
#
# temboo.core.exception.TembooError
# temboo.core.exception.TembooHTTPError
# temboo.core.exception.TembooCredentialError
# temboo.core.exception.TembooObjectNotAccessibleError
#
# Classes for handling Temboo-related exceptions.
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
###############################################################################


class TembooError(Exception):

    def __init__(self, msg):
        super(TembooError, self).__init__(msg)
        self.type = 'Temboo'

class TembooObjectNotAccessibleError(TembooError):
    def __init__(self, msg, uri):
        super(TembooObjectNotAccessibleError, self).__init__(msg)
        self.uri = uri

class TembooCredentialError(TembooError):
    pass

class TembooHTTPError(TembooError):
    def __init__(self, msg, status, reason, response_body):
        super(TembooHTTPError, self).__init__(msg)
        self.args = (msg, status, reason, response_body)

class TembooDisallowedInputError(TembooError):
	def __init__(self, msg, input_name):
		super(TembooDisallowedInputError, self).__init__(msg)
		self.type = 'DisallowedInput'
		self.input_name = input_name

class TembooNotFoundError(TembooError):
    def __init__(self, msg):
        super(TembooNotFoundError, self).__init__(msg)
        self.type = 'NotFound'
