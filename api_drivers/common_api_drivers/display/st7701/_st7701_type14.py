import time


# TL028WVC01 2.8" round display
def init(self):
    param_buf = bytearray(16)
    param_mv = memoryview(param_buf)
    
    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x13])
    self.set_params(0xFF, param_mv[:5])

    param_buf[0] = 0x08
    self.set_params(0xEF, param_mv[:1])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x10])
    self.set_params(0xFF, param_mv[:5])

    param_buf[:2] = bytearray([0x3B, 0x00])
    self.set_params(0xC0, param_mv[:2])

    param_buf[:2] = bytearray([0x10, 0x0C])
    self.set_params(0xC1, param_mv[:2])

    param_buf[:2] = bytearray([0x07, 0x0A])
    self.set_params(0xC2, param_mv[:2])

    param_buf[0] = 0x00
    self.set_params(0xC7, param_mv[:1])

    param_buf[0] = 0x10
    self.set_params(0xCC, param_mv[:1])

    param_buf[0] = 0x08
    self.set_params(0xCD, param_mv[:1])

    param_buf[:16] = bytearray([
        0x05, 0x12, 0x98, 0x0E, 0x0F, 0x07, 0x07, 0x09, 
        0x09, 0x23, 0x05, 0x52, 0x0F, 0x67, 0x2C, 0x11])
    self.set_params(0xB0, param_mv[:16])

    param_buf[:16] = bytearray([
        0x0B, 0x11, 0x97, 0x0C, 0x12, 0x06, 0x06, 0x08, 
        0x08, 0x22, 0x03, 0x51, 0x11, 0x66, 0x2B, 0x0F])
    self.set_params(0xB1, param_mv[:16])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x11])
    self.set_params(0xFF, param_mv[:5])

    param_buf[0] = 0x5D
    self.set_params(0xB0, param_mv[:1])

    param_buf[0] = 0x2D
    self.set_params(0xB1, param_mv[:1])

    param_buf[0] = 0x81
    self.set_params(0xB2, param_mv[:1])

    param_buf[0] = 0x80
    self.set_params(0xB3, param_mv[:1])

    param_buf[0] = 0x4E
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
        0x06, 0x30, 0x08, 0x30, 0x05, 0x30, 
        0x07, 0x30, 0x00, 0x33, 0x33])
    self.set_params(0xE1, param_mv[:11])

    param_buf[:12] = bytearray([
        0x11, 0x11, 0x33, 0x33, 0xF4, 0x00, 
        0x00, 0x00, 0xF4, 0x00, 0x00, 0x00])
    self.set_params(0xE2, param_mv[:12])

    param_buf[:4] = bytearray([0x00, 0x00, 0x11, 0x11])
    self.set_params(0xE3, param_mv[:4])

    param_buf[:2] = bytearray([0x44, 0x44])
    self.set_params(0xE4, param_mv[:2])

    param_buf[:16] = bytearray([
        0x0D, 0xF5, 0x30, 0xF0, 0x0F, 0xF7, 0x30, 0xF0, 
        0x09, 0xF1, 0x30, 0xF0, 0x0B, 0xF3, 0x30, 0xF0])
    self.set_params(0xE5, param_mv[:16])

    param_buf[:4] = bytearray([0x00, 0x00, 0x11, 0x11])
    self.set_params(0xE6, param_mv[:4])

    param_buf[:2] = bytearray([0x44, 0x44])
    self.set_params(0xE7, param_mv[:2])

    param_buf[:16] = bytearray([
        0x0C, 0xF4, 0x30, 0xF0, 0x0E, 0xF6, 0x30, 0xF0, 
        0x08, 0xF0, 0x30, 0xF0, 0x0A, 0xF2, 0x30, 0xF0])
    self.set_params(0xE8, param_mv[:16])

    param_buf[:2] = bytearray([0x36, 0x01])
    self.set_params(0xE9, param_mv[:2])

    param_buf[:7] = bytearray([0x00, 0x01, 0xE4, 0xE4, 0x44, 0x88, 0x40])
    self.set_params(0xEB, param_mv[:7])

    param_buf[:16] = bytearray([
        0xFF, 0x10, 0xAF, 0x76, 0x54, 0x2B, 0xCF, 0xFF, 
        0xFF, 0xFC, 0xB2, 0x45, 0x67, 0xFA, 0x01, 0xFF])
    self.set_params(0xED, param_mv[:16])

    param_buf[:6] = bytearray([0x08, 0x08, 0x08, 0x45, 0x3F, 0x54])
    self.set_params(0xEF, param_mv[:6])

    param_buf[:5] = bytearray([0x77, 0x01, 0x00, 0x00, 0x00])
    self.set_params(0xFF, param_mv[:5])

    self.set_params(0x11)

    time.sleep_ms(120)  # NOQA

    param_buf[0] = 0x66
    self.set_params(0x3A, param_mv[:1])

    param_buf[0] = 0x00
    self.set_params(0x36, param_mv[:1])

    param_buf[0] = 0x00
    self.set_params(0x35, param_mv[:1])

    self.set_params(0x29)

    time.sleep_ms(50)  # NOQA
