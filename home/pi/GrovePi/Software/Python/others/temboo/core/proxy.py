###############################################################################
#
# temboo.core.proxy.TembooProxy
# temboo.core.proxy.TembooProxifiedChoreography
#
# Classes to proxy choreo execution requests made from the JavaScript SDK
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

import copy
import json
from temboo.core.exception import TembooError
from temboo.core.exception import TembooDisallowedInputError
from temboo.core.exception import TembooNotFoundError

class TembooProxy(object):

	def __init__(self):
		self._choreos = {}

	def _get_choreo(self, name):
		# Make sure we know about the specified choreo
		if not name in self._choreos:	
			raise TembooNotFoundError('Proxied Choreo not found: ' + name)
		return self._choreos[name]

	def add_choreo(self, name, choreo, defaultInputs={}, *allowedUserInputs):
		proxified = _TembooProxifiedChoreography(choreo)

		if(0 < len(defaultInputs)):
			# Grab a new input set
			inputs = choreo.new_input_set()
			# Add inputs
			for key in dict:
				inputs.set_input(key, dict[key])
			# Set on choreo
			proxified.set_default_inputs(inputs)

		if(0 < len(allowedUserInputs)):
			proxified.allow_user_inputs(list(allowedUserInputs))

		self._choreos[name] = proxified

	def allow_user_inputs(self, name, *allowedUserInputs):
		choreo = self._get_choreo(name)

		if(0 < len(allowedUserInputs)):
			if isinstance(allowedUserInputs[0], basestring):
				# one or more input names as strings
				allowedUserInputs = list(allowedUserInputs)
			else:
				# a list of input names
				allowedUserInputs = allowedUserInputs[0]
			
			choreo.allow_user_inputs(allowedUserInputs)

	def execute(self, request, asJson=True):
		try:
			if isinstance(request, basestring):
				request = json.loads(request);
			
			if not 'name' in request:
				raise TembooError('Missing choreo name')
			elif not 'version' in request:
				raise TembooError('Missing required JS SDK version')

			# Parse request
			choreo = self._get_choreo(request['name'])
			inputs = request['inputs'] if 'inputs' in request else {}
			outputFilters = request['outputFilters'] if 'outputFilters' in request else {}

			# Execute the proxified choreo
			result = choreo.execute(inputs, outputFilters, request['version'])
			# Build the formatted response
			response = {'success':'true', 'outputs':result.outputs}
			# Respond appropriately
			return json.dumps(response) if asJson else response
		except TembooDisallowedInputError as e:
			err = {'error':'true', 'type':e.type, 'message':e.args[0], 'inputName':e.input_name}
			return json.dumps(err) if asJson else err
		except TembooError as e:
			err = {'error':'true', 'type':e.type, 'message':e.args[0]}
			return json.dumps(err) if asJson else err
		except Exception as e:
			err = {'error':'true', 'type':'Server', 'nativeType':type(e).__name__, 'message':'An unknown error occurred'}
			return json.dumps(err) if asJson else err

	def set_default_inputs(self, name, defaultInputs):
		choreo = self._get_choreo(name)
		choreo._defaultInputs = defaultInputs


class _TembooProxifiedChoreography(object):

	def __init__(self, choreo):
		self._allowedUserInputs = []
		self._defaultInputs = choreo.new_input_set()
		self._choreo = choreo

	def allow_user_inputs(self, inputs):
		for name in inputs:
			if(not name in self._allowedUserInputs):
				self._allowedUserInputs.append(name)

	def execute(self, inputs, outputFilters, jsClientVersion):
		fullInputs = copy.deepcopy(self._defaultInputs)
		
		# verify specified inputs are allowed
		for name in inputs:
			if(not name in self._allowedUserInputs):
				raise TembooDisallowedInputError('Illegal input specified', name)
			
			fullInputs._set_input(name, inputs[name]);

		# add output filters
		for name in outputFilters:
			fullInputs.add_output_filter(name, outputFilters[name]['path'], outputFilters[name]['variable'])

		# set the client SDK version
		self._choreo._set_js_client_version(jsClientVersion)

		return self._choreo.execute_with_results(fullInputs)
