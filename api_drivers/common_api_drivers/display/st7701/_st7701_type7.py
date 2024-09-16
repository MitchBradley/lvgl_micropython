import time


def init(self):
    param_buf = bytearray(16)
    param_mv = memoryview(param_buf)
    
    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x10])
    self.set_params(0xFF, param_mv[:5])

    param_buf[:2] = bytearray([0x3B, 0x00])
    self.set_params(0xC0, param_mv[:2])

    param_buf[:2] = bytearray([0x0B, 0x02])
    self.set_params(0xC1, param_mv[:2])

    param_buf[:2] = bytearray([0x07, 0x02])
    self.set_params(0xC2, param_mv[:2])

    param_buf[0] = 0x10
    self.set_params(0xCC, param_mv[:1])

    param_buf[0] = 0x08
    self.set_params(0xCD, param_mv[:1])

    # Positive Voltage Gamma Control
    param_buf[:16] = bytearray([
        0x00, 0x11, 0x16, 0x0E, 0x11, 0x06, 0x05, 0x09, 
        0x08, 0x21, 0x06, 0x13, 0x10, 0x29, 0x31, 0x18])
    self.set_params(0xB0, param_mv[:16])

    # Negative Voltage Gamma Control
    param_buf[:16] = bytearray([
        0x00, 0x11, 0x16, 0x0E, 0x11, 0x07, 0x05, 0x09, 
        0x09, 0x21, 0x05, 0x13, 0x11, 0x2A, 0x31, 0x18])
    self.set_params(0xB1, param_mv[:16])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x11])
    self.set_params(0xFF, param_mv[:5])

    param_buf[0] = 0x6D
    self.set_params(0xB0, param_mv[:1])

    param_buf[0] = 0x37
    self.set_params(0xB1, param_mv[:1])

    param_buf[0] = 0x81
    self.set_params(0xB2, param_mv[:1])

    param_buf[0] = 0x80
    self.set_params(0xB3, param_mv[:1])

    param_buf[0] = 0x43
    self.set_params(0xB5, param_mv[:1])

    param_buf[0] = 0x85
    self.set_params(0xB7, param_mv[:1])

    param_buf[0] = 0x20
    self.set_params(0xB8, param_mv[:1])

    param_buf[0] = 0x78
    self.set_params(0xC1, param_mv[:1])

    param_buf[0] = 0x78
    self.set_params(0xC2, param_mv[:1])

    param_buf[0] = 0x88
    self.set_params(0xD0, param_mv[:1])

    param_buf[:3] = bytearray([0x00, 0x00, 0x02])
    self.set_params(0xE0, param_mv[:3])

    param_buf[:11] = bytearray([
        0x03, 0xA0, 0x00, 0x00, 0x04, 0xA0, 
        0x00, 0x00, 0x00, 0x20, 0x20])
    self.set_params(0xE1, param_mv[:11])

    param_buf[:13] = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    self.set_params(0xE2, param_mv[:13])

    param_buf[:4] = bytearray([0x00, 0x00, 0x11, 0x00])
    self.set_params(0xE3, param_mv[:4])

    param_buf[:2] = bytearray([0x22, 0x00])
    self.set_params(0xE4, param_mv[:2])

    param_buf[:16] = bytearray([
        0x05, 0xEC, 0xA0, 0xA0, 0x07, 0xEE, 0xA0, 0xA0, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    self.set_params(0xE5, param_mv[:16])

    param_buf[:4] = bytearray([0x00, 0x00, 0x11, 0x00])
    self.set_params(0xE6, param_mv[:4])

    param_buf[:2] = bytearray([0x22, 0x00])
    self.set_params(0xE7, param_mv[:2])

    param_buf[:16] = bytearray([
        0x06, 0xED, 0xA0, 0xA0, 0x08, 0xEF, 0xA0, 0xA0, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    self.set_params(0xE8, param_mv[:16])

    param_buf[:7] = bytearray([0x00, 0x00, 0x40, 0x40, 0x00, 0x00, 0x00])
    self.set_params(0xEB, param_mv[:7])

    param_buf[:16] = bytearray([
        0xff, 0xff, 0xff, 0xBA, 0x0A, 0xBF, 0x45, 0xff, 
        0xff, 0x54, 0xFB, 0xA0, 0xAB, 0xff, 0xff, 0xff])
    self.set_params(0xED, param_mv[:16])

    param_buf[:6] = bytearray([0x10, 0x0D, 0x04, 0x08, 0x3F, 0x1F])
    self.set_params(0xEF, param_mv[:6])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x13])
    self.set_params(0xff, param_mv[:5])

    param_buf[0] = 0x08
    self.set_params(0xEF, param_mv[:1])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x00])
    self.set_params(0xff, param_mv[:5])

    param_buf[0] = 0x00
    self.set_params(0x36, param_mv[:1])

    param_buf[0] = 0x66
    self.set_params(0x3A, param_mv[:1])

    param_buf[0] = 0x00
    self.set_params(0x11, param_mv[:1])

    # Sleep Out
    self.set_params(0x11)

    time.sleep_ms(120)  # NOQA

    # Display On
    self.set_params(0x29)
