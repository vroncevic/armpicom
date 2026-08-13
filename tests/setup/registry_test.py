# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
Info
    Unit tests for ARMPicomBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from armpicom.core.service.iservice import IService
from armpicom.core.service.isubprocessor import ISubProcessor
from armpicom.infrastructure.cli.icli import ICLI
from armpicom.setup.bundle import ARMPicomBundle
from armpicom.setup.registry import ARMPicomBundleRegistry


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestARMPicomBundleRegistry(unittest.TestCase):

    def test_create_bundle_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        
        bundle = ARMPicomBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, ARMPicomBundle)
        self.assertEqual(bundle.base, mock_base)

    def test_create_bundle_invalid_dependencies(self) -> None:
        with self.assertRaises(Exception):
            ARMPicomBundleRegistry.create_bundle(None)

    def test_get_version(self) -> None:
        self.assertEqual(ARMPicomBundleRegistry.get_version(), '1.9.8')

