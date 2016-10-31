# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
#
# ==============================================================================
# Authors:          Patrick Lehmann
#
# Python Test:      Derived and extended ConfigParser from Python standard library
#
# Description:
# ------------------------------------
# Undocumented
#
# License:
# ==============================================================================
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
# ==============================================================================
#
from pathlib import Path

from ExtendedConfigParser import ExtendedConfigParser

from test.test_1.Test import Test as Test_1
from test.test_2.Test import Test as Test_2
from test.test_3.Test import Test as Test_3
from test.test_4.Test import Test as Test_4

tests = [
	Test_1,
	Test_2,
	Test_3,
	Test_4
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
			value = config[section][option]
			if (value != expected):
				errors += 1
				print("  {section}:{option} = {value}    expected: {expected}".format(section=section, option=option, value=value, expected=expected))

print("Errors: {errors}".format(errors=errors))


exit(errors)
