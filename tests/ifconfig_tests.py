# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ifcfg
from ifcfg.parser import NullParser
from nose.tools import eq_, ok_, raises

from . import ifconfig_out
from .base import IfcfgTestCase


class IfcfgTestCase(IfcfgTestCase):

    def test_ifcfg(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        interfaces = ifcfg.interfaces(ifconfig=ifconfig_out.LINUX)
        res = len(interfaces) > 0
        ok_(res)

    def test_unknown(self):
        ifcfg.distro = 'Bogus'
        ifcfg.Parser = ifcfg.get_parser_class()
        self.assertTrue(issubclass(ifcfg.Parser, NullParser))

    @raises(RuntimeError)
    def test_illegal(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        ifcfg.get_parser(ifconfig=ifconfig_out.ILLEGAL_OUTPUT)

    def test_linux(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux2(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX2)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux3(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX3)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['eth0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['eth0']['inet'], '192.168.0.1')
        eq_(interfaces['eth0']['broadcast'], '192.168.0.255')
        eq_(interfaces['eth0']['netmask'], '255.255.255.0')

    def test_linux4(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.LINUX4)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 1)
        eq_(interfaces['br-339b29e0f3aa']['ether'], '02:42:64:80:dd:3e')
        eq_(interfaces['br-339b29e0f3aa']['inet'], '192.168.0.1')
        eq_(interfaces['br-339b29e0f3aa']['broadcast'], '192.168.0.255')
        eq_(interfaces['br-339b29e0f3aa']['netmask'], '255.255.255.0')

    def test_macosx(self):
        ifcfg.distro = 'MacOSX'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.MACOSX)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 2)
        eq_(interfaces['en0']['ether'], '1a:2b:3c:4d:5e:6f')
        eq_(interfaces['en0']['inet'], '192.168.0.1')
        eq_(interfaces['en0']['broadcast'], '192.168.0.255')
        eq_(interfaces['en0']['netmask'], '255.255.255.0')

    def test_FreeBSD(self):
        ifcfg.distro = 'FreeBSD'
        ifcfg.Parser = ifcfg.get_parser_class()
        parser = ifcfg.get_parser(ifconfig=ifconfig_out.FREEBSD)
        interfaces = parser.interfaces
        self.assertEqual(len(interfaces.keys()), 5)
        # iflan0
        eq_(interfaces['iflan0']['ether'], '00:50:56:80:7f:2a')
        eq_(interfaces['iflan0']['inet'], '192.168.0.1')
        eq_(interfaces['iflan0']['broadcast'], '192.168.3.255')
        eq_(interfaces['iflan0']['netmask'], 22)
        # ifwan0
        eq_(interfaces['ifwan0']['ether'], '00:50:56:80:56:57')
        eq_(interfaces['ifwan0']['inet'], '10.0.0.6')
        eq_(interfaces['ifwan0']['broadcast'], '10.0.0.7')
        eq_(interfaces['ifwan0']['netmask'], 30)
        # ifcli715
        eq_(interfaces['ifcli715']['ether'], '00:50:56:80:14:68')
        eq_(interfaces['ifcli715']['inet'], '10.0.106.254')
        eq_(interfaces['ifcli715']['broadcast'], '10.0.106.255')
        eq_(interfaces['ifcli715']['netmask'], 24)

    def test_default_interface(self):
        ifcfg.distro = 'Linux'
        ifcfg.Parser = ifcfg.get_parser_class()
        route_output = ifconfig_out.ROUTE_OUTPUT
        res = ifcfg.default_interface(
            ifconfig=ifconfig_out.LINUX3, route_output=route_output
        )
        ok_(res)
