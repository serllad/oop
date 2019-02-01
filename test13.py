import struct
import binascii
b=bytes('abc',encoding='utf-8')
values = (b'v',12,b'abcde',2.1,)
s = struct.Struct('ci5sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)

print('Original values:', values)
print('Format string :', s.format)
print('Uses :', s.size, 'bytes')
print('Packed Value :', binascii.hexlify(packed_data))
print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)