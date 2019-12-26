# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#               _____      _                 _          _  ____             __ _       ____
#   _ __  _   _| ____|_  _| |_ ___ _ __   __| | ___  __| |/ ___|___  _ __  / _(_) __ _|  _ \ __ _ _ __ ___  ___ _ __
#  | '_ \| | | |  _| \ \/ / __/ _ \ '_ \ / _` |/ _ \/ _` | |   / _ \| '_ \| |_| |/ _` | |_) / _` | '__/ __|/ _ \ '__|
#  | |_) | |_| | |___ >  <| ||  __/ | | | (_| |  __/ (_| | |__| (_) | | | |  _| | (_| |  __/ (_| | |  \__ \  __/ |
#  | .__/ \__, |_____/_/\_\\__\___|_| |_|\__,_|\___|\__,_|\____\___/|_| |_|_| |_|\__, |_|   \__,_|_|  |___/\___|_|
#  |_|    |___/                                                                  |___/
#
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python Test:        Derived and extended ConfigParser from Python standard library
#
# Description:
# ------------------------------------
# Undocumented
#
# License:
# ==============================================================================
# Copyright 2017-2019 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ==============================================================================
#
from pathlib import Path

from pyExtendedConfigParser import ExtendedConfigParser

from test.test_1.Test import Test as Test_1
from test.test_2.Test import Test as Test_2
from test.test_3.Test import Test as Test_3
from test.test_4.Test import Test as Test_4
from test.test_5.Test import Test as Test_5
from test.test_6.Test import Test as Test_6

tests = [
	Test_1,
	Test_2,
	Test_3,
	Test_4,
	Test_5,
	Test_6
]

workingDirectoryPath =  Path.cwd()

errors = 0
for test in tests:
	t = test()
	testName = t.GetName()
	print("Running test: {test}".format(test=testName))
	
	testDirectoryPath = workingDirectoryPath / "test" / testName
	
	config = ExtendedConfigParser()
	config.optionxform = str
	
	for file in t.GetFiles():
		filePath = testDirectoryPath / file
		if (not filePath.exists()):
			print("File '{file!s}' not found.".format(file=filePath))
			continue
		
		config.read(str(filePath))
	
	for section,values in t.GetExpected().items():
		for option,expected in values.items():
			try:
				value = config[section][option]
			except KeyError as ex:
				print("  KeyError: for {ex!s}".format(ex=ex))
				errors += 1
				continue
			
			if (value != expected):
				errors += 1
				print("  {section}:{option} = {value}    expected: {expected}".format(section=section, option=option, value=value, expected=expected))
	
print("="*80)
print("Errors: {errors}".format(errors=errors))

exit(errors)
