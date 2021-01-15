from ncclient import manager
import xml.dom.minidom

HOST = 'sandbox-iosxe-latest-1.cisco.com'
PORT = 830
USERNAME = 'developer'
PASSWORD = 'C1sco12345'
DEVICE_PARMAMS = {'name': 'csr'}
INTERFACE = 'GigabitEthernet2'


def edit_interface_configuration(interface_name):
    m = manager.connect(host=HOST, port=PORT, username=USERNAME,
                        password=PASSWORD, device_params=DEVICE_PARMAMS)
    interface_filter = '''
                        <config>
                            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                                <interface>
                                    <name>{interface_xml}</name>
                                    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                            <ip>44.0.0.1</ip>
                                            <netmask>255.255.255.0</netmask>
                                        </address>
                                    </ipv4>
                                </interface>
                            </interfaces>
                        </config>'''


    netconf_payload = interface_filter.format(interface_xml=interface_name)
    print (netconf_payload)

    ios_edit_interface_configuration = m.edit_config(netconf_payload,target='running')
    return xml.dom.minidom.parseString(str(ios_edit_interface_configuration))
    m.close_session()


def main():
    edit_interface = edit_interface_configuration(INTERFACE)
    print (edit_interface.toprettyxml(indent= ' '))
    
if __name__ == "__main__":
    main()
