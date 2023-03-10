import socket

def detect_reverse_shell():
    shell_strings = [
        b"/bin/bash", b"/bin/sh", b"/bin/zsh", b"/usr/local/bin/bash", b"/usr/local/bin/sh", b"/usr/local/bin/zsh",
        b"powershell.exe", b"powershell", b"perl", b"ruby", b"python", b"nc", b"netcat"
    ]

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.110', 8080)) # Write your local IP address.
    server_socket.listen(1)
    print("[+] Listening for incoming connections on port 8080...")
    connection, address = server_socket.accept()
    print("[+] Connection established with: ", address)
    
    while True:
        data = connection.recv(1024)
        if not data:
            break
        for shell_string in shell_strings:
            if shell_string in data:
                print("[!] Reverse Shell detected!")
                connection.sendall(b"[+] Reverse Shell detected!\n")
                break
        else:
            connection.sendall(b"[+] No Reverse Shell detected.\n")

        
    connection.close()
    server_socket.close()

if __name__ == "__main__":
	detect_reverse_shell()
