import argparse
import subprocess
import signal
import os

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        self.kill_now = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--develop', action='store_true', default=False,
        help="Develop mode -- server will reload automatically when you make changes. Is not secure to make publicly accessible.")
    args = parser.parse_args()

    killer = GracefulKiller()
    cmd = ""
    if args.develop:
        cmd += "export FLASK_DEBUG=1 && "
    cmd += "export FLASK_APP='main.py' && python -m flask run -p 5000 -h 0.0.0.0 --with-threads"
    p = subprocess.call(cmd, shell=True)
    subprocess.call("unset FLASK_APP && unset FLASK_DEBUG", shell=True)
    print "Server has stopped"
