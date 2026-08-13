# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for ARMPicomBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from armpicom.setup.keys import ARMPicomBundleKeys


class TestARMPicomBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = ARMPicomBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(ARMPicomBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(ARMPicomBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(ARMPicomBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(ARMPicomBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = ARMPicomBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(ARMPicomBundleKeys.OPTION_INFO_FILE, opts)
