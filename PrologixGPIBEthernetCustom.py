import socket
from time import sleep

class PrologixGPIBEthernetCustom():
    '''
    A class similar to PrologixGPIBEthernet in the prologix-gpib-ethernet
    library by nelsond for setting up custom communication with the MI-WAVE
    511 series attenuator.
    Manual at https://www.miwv.com/wp-content/uploads/2018/09/511_InstructionManual_v03.pdf

    BEWARE: the device probably sets at the first instance, but it answers with
    duplicated packages, ask at least twice ...

    TODO: read of the set value.

    USAGE: init, connect, set attenuation(value, channel)

    Last modified: 21/10/2020 by Eugenio Senes
    '''
    PORT = 1234

    def __init__(self, host, timeout=3):
        self.host = host
        self.timeout = timeout

    def connect(self):
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM,
                                    socket.IPPROTO_TCP)
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.PORT))
        
        self._setup()

    def close(self):
        self.socket.close()

    def set_gpib_address(self, addr):
        self._send('++addr %i' % int(addr))

    def get_gpib_address(self):
        return int(self.query('++addr'))

    def set_attenuation(self, value, channel):
        if value <= 60 and value >=0:
            self.set_gpib_address(channel)
            self._send(value)
        else:
            raise ValueError('Attenuation out of range')

    def query(self, comm):
        self._send(comm)
        return self._recv()

    def _send(self, value):
        encoded_value = ('%s\r\n' % value).encode('ascii')
        self.socket.send(encoded_value)

    def _recv(self, byte_num=2**16):
        value = self.socket.recv(byte_num)
        return value.decode('ascii')

    def _setup(self):
        self._send('++mode 1')
        sleep(0.1)
        self._send('++eos 0')
        sleep(0.1)
        self._send('++read_tmo_ms 13')
        sleep(0.1)
        self._send('++eoi 1')
        sleep(0.1)
