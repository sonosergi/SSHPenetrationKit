# SSHPenetrationKit
SSHPenetrationKit is a penetration testing tool designed specifically to assess the security of SSH (Secure Shell) servers. This repository contains the source code and resources for SSHPenetrationKit, enabling users to contribute, enhance, and leverage its capabilities in securing SSH deployments.

## SSH Brute Force Script
This Python script is designed for SSH brute force attacks, allowing you to test the security of SSH servers by attempting to authenticate with a list of passwords.
### Prerequisites
* Python 3.x installed on your system.
*  The Paramiko library installed. You can install it using:
```shell
pip install paramiko
```
* The Colorama library installed. You can install it using:
```shell
pip install colorama
```
### Usage
1. Open a terminal or command prompt and navigate to the directory where you saved the script.
2. Run the script using the following command:
```python
python3 ssh_brute_force.py <hostname> [-P <passlist>] [-u <username>] [-f <fuzz_length>]
```
* <hostname>: Replace it with the hostname or IP address of the target SSH server.
* -P <passlist> (optional): Specify the path to a password wordlist file in .txt format. If not provided, a randomly generated password will be used for fuzzing.
* -u <username> (optional): Specify the username to attempt authentication. If not provided, the script will use a default username.
* -f <fuzz_length> (optional): Specify the length of the randomly generated password for fuzzing. If not provided, the script will not perform password fuzzing.
3. The script will start attempting SSH connections using the provided parameters. If valid credentials are found, they will be saved in a file named credentials.txt in the same directory as the script.

If you encounter issues with firewalls or detection systems, you can try utilizing the following techniques:

## SSH Tunnels
### Installation
Ensure that you have the `sshtunnel` library installed. If it is not already installed, run the following command in your terminal:
```shell
pip install sshtunnel
```
### Configuration
Open the Python script file in a text editor.
Import the `SSHTunnelForwarder` class from `sshtunnel` at the beginning of the script:
```python
from sshtunnel import SSHTunnelForwarder
```
### Code Modification
Locate the `is_ssh_open` function in the script and make the following changes:
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
3. Modify the `client.connect(...)` line to establish the SSH connection through the tunnel:
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
Before using covert protocols, you need to configure and run the corresponding tools such as `ptunnel` or `iodine` on your system and the target server. Follow the specific instructions of each tool to configure the covert protocols.
### Code Modification
Locate the `is_ssh_open` function in the script and modify the SSH connection to redirect the traffic through the covert protocol instead of a direct connection to the host.

## Reverse Proxies
### Configuration
Configure and run a reverse proxy tool such as `sshuttle` or `Proxychains` on your system and the target server. Follow the specific instructions of each tool to configure and run the reverse proxy.
### Code Modification
Locate the `is_ssh_open` function in the script and modify the SSH connection to establish it through the reverse proxy instead of a direct connection to the host.

## Important Notes

* Use this script responsibly and only on systems you have explicit permission to test.
* Brute force attacks are generally considered malicious and illegal without proper authorization.
* Respect all applicable laws, regulations, and ethical guidelines when conducting penetration testing or security assessments.

Please ensure that you have explicit permission and adhere to legal and ethical standards before using this script.
