import libvirt
from xml.etree import ElementTree
import argparse

parser = argparse.ArgumentParser(
	description='Backup libvirt/qemu virtual machines'
)
parser.add_argument("-d", "--domain", required=True, type=str, help="Domain to backup")
args = parser.parse_args()

libvirtConn = libvirt.open('qemu:///system')
tree=ElementTree.fromstring(libvirtConn.lookupByName('%s' % args.domain).XMLDesc(0))
devices=[]

for target in tree.findall("devices/disk"):
    for src in target.findall("target"):
        dev=src.get("dev")
        devices.append(dev)
print ('\n'.join(devices))

