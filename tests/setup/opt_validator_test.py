# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for ARMPicomBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from armpicom.setup.opt_validator import ARMPicomBundleOptionsValidator


class TestARMPicomBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        ARMPicomBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            ARMPicomBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            ARMPicomBundleOptionsValidator.validate("not_a_mapping")

            options = {'info_file': 123}
            ARMPicomBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(ARMPicomBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(ARMPicomBundleOptionsValidator.is_valid(None))
        self.assertFalse(ARMPicomBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(ARMPicomBundleOptionsValidator.is_valid({'info_file': 123}))

