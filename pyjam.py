#!/usr/bin/env python3

import argparse as ap, requests as rq, os, subprocess

def down_tunnel():
    try:
        proc_down = subprocess.Popen(['wg-quick', 'down', './tunnel.conf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc_down.communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())
    except Exception as e:
        print(f"Error : {e}\n")

def up_tunnel():
    try:
        proc_down = subprocess.Popen(['wg-quick', 'up', './tunnel.conf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc_down.communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())
    except Exception as e:
        print(f"Error : {e}\n")

def remove_conf_file():
    try:
        os.remove('tunnel.conf')
        print("File removed successfully.")
    except Exception as e:
        print(f"Error : {e}")

def download_file(port):
    try:
        with open('tunnel.conf', 'w') as conf:
            try:
                url = "https://tunnel.pyjam.as/" + str(port)
                resp = rq.get(url)
                conf.writelines(str(resp.content.decode()))
                os.chown('tunnel.conf', 0, 0)
                os.chmod('tunnel.conf', 0o000)
            except Exception as e:
                print(f"Error : {e}")
                exit(1)
        conf.close()
    except Exception as e:
        print(f"Error : {e}")
        exit(1)

if __name__ == "__main__":
    if os.getuid() != 0:
        print("The program must be run with superadmin privilege.")
        exit(1)
    parser = ap.ArgumentParser(description="A python program to automate the creation of a pyjam.as tunnel.", formatter_class=ap.RawTextHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--port", type=int, help='The port to bind to. If a tunnel already exists, it will be deleted.')
    group.add_argument("-d", "--down", action='store_true', help="Down the tunnel")
    group.add_argument("-u", "--up", action='store_true', help="Up the tunnel")
    args = parser.parse_args()
    if args.port:
        down_tunnel()
        remove_conf_file()
        download_file(args.port)
        up_tunnel()
    elif args.down:
        down_tunnel()
    elif args.up:
        up_tunnel()



