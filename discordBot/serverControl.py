import subprocess

class Server:
    def __init__(self, server_start_bat, dir):
        self.server_start_bat = server_start_bat
        self.dir = dir

    def start_server(self):
        self.server = subprocess.Popen(self.server_start_bat, cwd=self.dir, shell=True, stdin=subprocess.PIPE, text=True)

    def stop_server(self):
        self.command('stop')
        self.server.communicate()

    def command(self, command):
        self.server.stdin.write(f'{command}\n')

