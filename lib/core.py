class Payload:

    DEFAULT_TAG = "w00t"

    def generate_egghunter_ntaccess(self):
        pass
    
    def generate_egghunter_seh(self):
        pass

class Util:
    def tag_to_hex(tag):
        return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"
    
    def ipv4_addr_to_hex(ip_addr):
        li = ["{:>02}".format(hex(int(i)).split('x')[1]) for i in ip_addr.split('.')]
        li.reverse()
        return ''.join(li)

    def port_to_hex(port_no):
        port_dec = "{:>04}".format(hex(int(port_no)).split('x')[1])
        port_hex = [port_dec[i:i+2] for i in range(0, len(port_dec), 2)]
        port_hex.reverse()
        return ''.join(port_hex)