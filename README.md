# SSHPenetrationKit
SSHPenetrationKit is a penetration testing tool designed specifically to assess the security of SSH (Secure Shell) servers. This repository contains the source code and resources for SSHPenetrationKit, enabling users to contribute, enhance, and leverage its capabilities in securing SSH deployments.

If you encounter issues with firewalls or detection systems, you can try utilizing the following techniques:

## SSH Tunnels
### Installation
Ensure that you have the 'sshtunnel' library installed. If it is not already installed, run the following command in your terminal:
```shell
pip install sshtunnel
```
### Configuration
Open the Python script file in a text editor.
Import the SSHTunnelForwarder class from sshtunnel at the beginning of the script:
```python
from sshtunnel import SSHTunnelForwarder
```
### Code Modification
Locate the 'is_ssh_open' function in the script and make the following changes:
1. Create an instance of 'SSHTunnelForwarder' to configure the SSH tunnel:
```python
tunnel = SSHTunnelForwarder(
    (hostname, 22),  # Configure the SSH host and port
    ssh_username=username,
    ssh_password=password,
)
```
2. Start the SSH tunnel before establishing the SSH connection:
```python
tunnel.start()
```
3. Modify the 'client.connect(...)' line to establish the SSH connection through the tunnel:
```pyhton
client.connect(
    hostname='localhost',  # Connect to localhost through the SSH tunnel
    port=tunnel.local_bind_port,
    username=username,
    password=password,
    timeout=3
)
```
4. Ensure to close the SSH tunnel after use:
```python
tunnel.stop()
```

## Covert Protocols
### Configuration
Before using covert protocols, you need to configure and run the corresponding tools such as ptunnel or iodine on your system and the target server. Follow the specific instructions of each tool to configure the covert protocols.
### Code Modification
Locate the is_ssh_open function in the script and modify the SSH connection to redirect the traffic through the covert protocol instead of a direct connection to the host.

## Reverse Proxies
### Configuration
Configure and run a reverse proxy tool such as sshuttle or Proxychains on your system and the target server. Follow the specific instructions of each tool to configure and run the reverse proxy.
### Code Modification
Locate the is_ssh_open function in the script and modify the SSH connection to establish it through the reverse proxy instead of a direct connection to the host.

Remember that these additional techniques have specific requirements and configurations that need to be fulfilled before using the Python script. Ensure that you have explicit and legal permission to use these techniques in your testing environment, and always respect security policies and regulations.
