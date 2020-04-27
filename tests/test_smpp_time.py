"""
Copyright 2009-2010 Mozes, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import unittest
import sys

sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")
from smpp.pdu import smpp_time
from datetime import datetime, timedelta

class SMPPTimeTest(unittest.TestCase):

    def test_parse_t(self):
        self.assertEqual(0, smpp_time.parse_t('0'))
        self.assertEqual('0', smpp_time.unparse_t(0))
        self.assertEqual(9, smpp_time.parse_t('9'))
        self.assertEqual('9', smpp_time.unparse_t(9))
        self.assertRaises(ValueError, smpp_time.parse_t, 'a')
        self.assertRaises(ValueError, smpp_time.parse_t, '03')

    def test_parse_nn(self):
        self.assertEqual(0, smpp_time.parse_nn('00'))
        self.assertEqual('00', smpp_time.unparse_nn(0))
        self.assertEqual(48, smpp_time.parse_nn('48'))
        self.assertEqual('48', smpp_time.unparse_nn(48))
        self.assertRaises(ValueError, smpp_time.parse_nn, '49')
        self.assertRaises(ValueError, smpp_time.parse_nn, '0')

    def test_parse_relative(self):
        tstr = b'020610233429000R'
        rel = smpp_time.parse(tstr)
        self.assertEqual(smpp_time.SMPPRelativeTime, rel.__class__)
        self.assertEqual(2, rel.years)
        self.assertEqual(6, rel.months)
        self.assertEqual(10, rel.days)
        self.assertEqual(23, rel.hours)
        self.assertEqual(34, rel.minutes)
        self.assertEqual(29, rel.seconds)
        self.assertEqual(tstr, smpp_time.unparse(rel))

    def test_parse_relative_mins_only(self):
        tstr = b'000000001000000R'
        rel = smpp_time.parse(tstr)
        self.assertEqual(smpp_time.SMPPRelativeTime, rel.__class__)
        self.assertEqual(0, rel.years)
        self.assertEqual(0, rel.months)
        self.assertEqual(0, rel.days)
        self.assertEqual(0, rel.hours)
        self.assertEqual(10, rel.minutes)
        self.assertEqual(0, rel.seconds)
        self.assertEqual(tstr, smpp_time.unparse(rel))

    def test_parse_absolute_no_offset(self):
        tstr = b'070927233429800+'
        dt = smpp_time.parse(tstr)
        self.assertEqual(2007, dt.year)
        self.assertEqual(9, dt.month)
        self.assertEqual(27, dt.day)
        self.assertEqual(23, dt.hour)
        self.assertEqual(34, dt.minute)
        self.assertEqual(29, dt.second)
        self.assertEqual(800000, dt.microsecond)
        self.assertEqual(None, dt.tzinfo)
        self.assertEqual(tstr, smpp_time.unparse(dt))

    def test_parse_absolute_positive_offset(self):
        tstr = b'070927233429848+'
        dt = smpp_time.parse(tstr)
        self.assertEqual(2007, dt.year)
        self.assertEqual(9, dt.month)
        self.assertEqual(27, dt.day)
        self.assertEqual(23, dt.hour)
        self.assertEqual(34, dt.minute)
        self.assertEqual(29, dt.second)
        self.assertEqual(800000, dt.microsecond)
        self.assertEqual(timedelta(hours=12), dt.tzinfo.utcoffset(None))
        self.assertEqual(tstr, smpp_time.unparse(dt))

    def test_parse_absolute_negative_offset(self):
        tstr = b'070927233429848-'
        dt = smpp_time.parse(tstr)
        self.assertEqual(2007, dt.year)
        self.assertEqual(9, dt.month)
        self.assertEqual(27, dt.day)
        self.assertEqual(23, dt.hour)
        self.assertEqual(34, dt.minute)
        self.assertEqual(29, dt.second)
        self.assertEqual(800000, dt.microsecond)
        self.assertEqual(timedelta(hours=-12), dt.tzinfo.utcoffset(None))
        self.assertEqual(tstr, smpp_time.unparse(dt))

