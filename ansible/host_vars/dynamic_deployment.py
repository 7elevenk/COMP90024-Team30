import argparse

# we can create n instances for one time
def common_vars(file):
    file.writeline('# Common vars')
    file.writeline('availability_zone: melbourne-qh2-uom')
    file.writeline('instance_image: 356ff1ed-5960-4ac2-96a1-0c0198e6a999')
    file.writeline('instance_flavor: uom.mse.2c9g')
    file.writeline('instance_key_name: team30')
    file.writeline('')

def create_volumes(i, file):
    file.writeline('# Volume')
    file.writeline('volumes:')
    file.writeline('# volume for main storage')
    file.writeline('  - vol_name: server{}-01'.format(i))
    file.writeline('    vol_size: 40')
    file.writeline('# volume for docker')
    file.writeline('  - vol_name: server{}-02'.format(i))
    file.writeline('    vol_size: 10')

def security_group_ssh(file):
    file.writeline('  - name: ssh')
    file.writeline('    protocol: tcp')
    file.writeline('    port_range_min: 22')
    file.writeline('    port_range_max: 22')
    file.writeline('    remote_ip_prefix: 0.0.0.0/0')

def security_group_http(file):
    file.writeline('  - name: http')
    file.writeline('    protocol: tcp')
    file.writeline('    port_range_min: 80')
    file.writeline('    port_range_max: 80')
    file.writeline('    remote_ip_prefix: 0.0.0.0/0')


def security_group_https(file):
    file.writeline('  - name: https')
    file.writeline('    protocol: tcp')
    file.writeline('    port_range_min: 443')
    file.writeline('    port_range_max: 443')
    file.writeline('    remote_ip_prefix: 0.0.0.0/0')

def security_group_self_defined(file, name, protocol, port_range_min, port_range_max):
    file.writeline('  - name: '+name)
    file.writeline('    protocol: '+protocol)
    file.writeline('    port_range_min: '+port_range_min)
    file.writeline('    port_range_max: '+port_range_max)
    file.writeline('    remote_ip_prefix: 0.0.0.0/0')

def define_instances(i, file):
    file.writeline('  - name: instance{}'.format(i))
    file.writeline("    volumes: ['server{}-01', 'server{}-02']".format(i,i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='n instances to be created')
    args = parser.parse_args()

    with open('new_instance.yaml', 'w') as file:
        common_vars(file)
        file.writeline()
        for i in range(args.n):
            create_volumes(i, file)
        file.writeline()
        security_group_https(file)
        security_group_http(file)
        security_group_ssh(file)
        file.writeline()
        for i in range(args.n):
            define_instances(i,file)


