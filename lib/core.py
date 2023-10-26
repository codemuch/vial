class Payload:

    DEFAULT_TAG = "w00t"

    def generate_egghunter_ntaccess(self):
        pass
    
    def generate_egghunter_seh(self):
        pass
    
    def tag_to_hex(tag):
        return f"0x{''.join([hex(ord(ch)).split('x')[1] for ch in tag][::-1])}"