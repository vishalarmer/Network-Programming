from netmiko import Netmiko

connection_object= Netmiko(host='192.168.1.254',username='vishu',password='cisco',device_type='cisco_asa', secret="cisco")
#calling netmiko function, it has usual attributes and plust device_type attribute which tell on whcich vendor we would connect to.
output=connection_object.send_command('show version')
print(output)
promt_object =  connection_object.find_prompt()
print(promt_object)
connection_object.config_mode()
promt_object =  connection_object.find_prompt()
print(promt_object)
connection_object.send_command('username test1 password test privilege 15')
output=connection_object.send_command("show run user")
print(output)
connection_object.disconnect()


