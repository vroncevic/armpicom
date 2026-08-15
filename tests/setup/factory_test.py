# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for ARMPicomBundleFactory class.
'''

from __future__ import annotations

import unittest

from armpicom.setup.bundle import ARMPicomBundle
from armpicom.setup.factory import ARMPicomBundleFactory


class TestARMPicomBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = ARMPicomBundleFactory.create_bundle()
        self.assertIsInstance(bundle, ARMPicomBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'armpicom/infrastructure/config/armpicom.cfg'}
        bundle = ARMPicomBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, ARMPicomBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            ARMPicomBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(ARMPicomBundleFactory.get_version(), '2.0.3')

