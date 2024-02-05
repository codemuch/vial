class Payload:

    DEFAULT_TAG = "w00t"
    EGG_NTACCESS_PAYLOAD_PATH = "./vials/egghunter/ntaccesscheck.nasm"
    EGG_SEH_PAYLOAD_PATH ="./vials/egghunter/seh.nasm"

    @staticmethod
    def generate_egghunter_ntaccess(tag):
        mapping = {"tag": tag}
        return Util.read_nasm(Payload.EGG_NTACCESS_PAYLOAD_PATH).format(**mapping)
    
    @staticmethod
    def generate_egghunter_seh(tag):
        mapping = {"tag": tag}
        return Util.read_nasm(Payload.EGG_SEH_PAYLOAD_PATH).format(**mapping)

    @staticmethod
    def generate_payload_tcp_bind():
        pass

    @staticmethod
    def generate_payload_tcp_reverse():
        pass

class Util:
    @staticmethod
    def read_nasm(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.rstrip('\n').split('#')[0] for line in file]
                file_contents = ''.join(lines)
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            return file_contents

    @staticmethod
    def tag_to_hex(tag):
        return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"
    
    @staticmethod
    def ipv4_addr_to_hex(ip_addr):
        li = ["{:>02}".format(hex(int(i)).split('x')[1]) for i in ip_addr.split('.')]
        li.reverse()
        return ''.join(li)

    @staticmethod
    def port_to_hex(port_no):
        port_dec = "{:>04}".format(hex(int(port_no)).split('x')[1])
        port_hex = [port_dec[i:i+2] for i in range(0, len(port_dec), 2)]
        port_hex.reverse()
        return ''.join(port_hex)