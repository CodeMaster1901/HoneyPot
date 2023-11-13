import logging
from socket import socket
import threading

bind_ip = '0.0.0.0'

class HP(object):
    def __init__(self,ports,log_filepath):
        self.ports = ports
        self.log_filepath = log_filepath
        self.listener_threads = {}
        
        if len(ports) < 1 : 
            raise Exception("no ports provided to scan")
            
        # for port in ports:
        #     print("goint to listen on the ports:",port )
        
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=self.log_filepath,
                    filemode='w')
        self.logger = logging.getLogger(__name__)
        self.logger.info("HonePot initializing...")
        self.logger.info("Ports : %s", self.ports)
        self.logger.info("log filepath : %s", self.log_filepath)

        
    def handle_connection(self,client_socket,remote_port,ip):
        req = self.client_socket.recv(32)
        self.logger.info("Connection from" , ip , ":" , remote_port , "-", req)
        # client_socket.send("ACK\n")
        client_socket.send("Access Denied\n")
        client_socket.close()
    
    def start_new_listener_thread(self,port):
            #creates a new listener for every port separately
            listener = socket() #defaulst to SOCK_STREAM and   AF.INET format itself
            listener.bind((bind_ip, int(port)))
            listener.listen(5)
            while True:
                client,addr = listener.accept()
                # print("Accepted connection from %s : %d - %s",addr[0],addr[1])
                client_handler = threading.Thread(target=self.handle_connection, args=(client,addr[0],addr[1]))
                client_handler.start()

    def start_listening(self):
        for port in self.ports:
            self.listener_threads[port] = threading.Thread(target=self.start_new_listener_thread,args=(port,))
            self.listener_threads[port].start()
            
    def run(self):
        self.start_listening()
        # while True:
        #     pass