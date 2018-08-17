# -*- coding: utf-8 -*-
from __future__ import unicode_literals

LINUX2 = """
eth0      Link encap:Ethernet  HWaddr 1a:2b:3c:4d:5e:6f
          inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::4240:36ff:fe38:a121/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:4041381 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3851783 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1123058554 (1.0 GiB)  TX bytes:737462074 (703.2 MiB)
          Interrupt:24

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:126491 errors:0 dropped:0 overruns:0 frame:0
          TX packets:126491 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:43170341 (41.1 MiB)  TX bytes:43170341 (41.1 MiB)
"""

LINUX3 = """
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::4240:36ff:fe38:a121  prefixlen 64  scopeid 0x20<link>
        ether 1a:2b:3c:4d:5e:6f  txqueuelen 1000  (Ethernet)
        RX packets 251031  bytes 146644544 (139.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 141266  bytes 28028187 (26.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 16436
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 1462  bytes 112866 (110.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1462  bytes 112866 (110.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

LINUX4 = """
br-339b29e0f3aa: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
        ether 02:42:64:80:dd:3e  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

LINUX = LINUX3


# Something out of order that we cannot parse
ILLEGAL_OUTPUT = """
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.1  netmask 255.255.255.0  broadcast 192.168.0.255
"""

MACOSX = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=2b<RXCSUM,TXCSUM,VLAN_HWTAGGING,TSO4>
	ether 1a:2b:3c:4d:5e:6f
	inet6 fe80::4240:36ff:fe38:a121%en0 prefixlen 64 scopeid 0x5
	inet 192.168.0.1 netmask 0xffffff00 broadcast 192.168.0.255
	media: autoselect (100baseTX <full-duplex>)
	status: active
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
"""  # noqa


ROUTE_OUTPUT = """
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    600    0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 eth0
"""

FREEBSD = """
iflan0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=9b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM>
        ether 00:50:56:80:7f:2a
        inet 192.168.0.1 netmask 0xfffffc00 broadcast 192.168.3.255
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet autoselect (1000baseT <full-duplex>)
        status: active
ifwan0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=60039b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,TSO4,TSO6,RXCSUM_IPV6,TXCSUM_IPV6>
        ether 00:50:56:80:56:57
        inet 10.0.0.6 netmask 0xfffffffc broadcast 10.0.0.7
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet autoselect
        status: active
ifcli715: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=60039b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,TSO4,TSO6,RXCSUM_IPV6,TXCSUM_IPV6>
        ether 00:50:56:80:14:68
        inet 10.0.106.254 netmask 0xffffff00 broadcast 10.0.106.255
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet autoselect
        status: active
pflog0: flags=141<UP,RUNNING,PROMISC> metric 0 mtu 33160
pfsync0: flags=0<> metric 0 mtu 1500
        syncpeer: 0.0.0.0 maxupd: 128 defer: off
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x6
        inet 127.0.0.1 netmask 0xff000000
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
""" # noqa
