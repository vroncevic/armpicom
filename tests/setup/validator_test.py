# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
Info
    Unit tests for ARMPicomBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from armpicom.core.service.iservice import IService
from armpicom.core.service.isubprocessor import ISubProcessor
from armpicom.infrastructure.cli.icli import ICLI
from armpicom.setup.bundle import ARMPicomBundle
from armpicom.setup.validator import ARMPicomBundleValidator


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


class TestARMPicomBundleValidator(unittest.TestCase):
    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = ARMPicomBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        ARMPicomBundleValidator.validate(bundle)

    def test_validate_bundle_none(self) -> None:
        with self.assertRaises(Exception):
            ARMPicomBundleValidator.validate(None)

    def test_validate_bundle_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            ARMPicomBundleValidator.validate("invalid_bundle")

    def test_validate_missing_components(self) -> None:
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = ARMPicomBundle(
                base=None,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            ARMPicomBundleValidator.validate(bundle)

    def test_validate_invalid_component_types(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        # base is not BaseBundle
        with self.assertRaises(Exception):
            bundle = ARMPicomBundle(
                base="invalid",
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            ARMPicomBundleValidator.validate(bundle)

        # service is not IService
        with self.assertRaises(Exception):
            bundle = ARMPicomBundle(
                base=mock_base,
                service="invalid",
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            ARMPicomBundleValidator.validate(bundle)

        # subprocessor is not ISubProcessor
        with self.assertRaises(Exception):
            bundle = ARMPicomBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor="invalid",
                cli=dummy_cli
            )
            ARMPicomBundleValidator.validate(bundle)

        # cli is not ICLI
        with self.assertRaises(Exception):
            bundle = ARMPicomBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli="invalid"
            )
            ARMPicomBundleValidator.validate(bundle)
