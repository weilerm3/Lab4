#1
import idautils
import idaapi
import idc

addr1 = idc.FindBinary(MinEA(), SEARCH_DOWN, "C7 45 EC 78 A4 6A D7", 16)
addr2 = idc.FindBinary(MinEA(), SEARCH_DOWN, "C7 45 F0 56 B7 C7 E8", 16)
addr3 = idc.FindBinary(MinEA(), SEARCH_DOWN, "C7 45 F4 DB 70 20 24", 16)
addr4 = idc.FindBinary(MinEA(), SEARCH_DOWN, "C7 45 F8 EE CE BD C1", 16)

foundBinary = [addr1, addr2, addr3, addr4]
flag = True
for f in foundBinary:
    if f != BADADDR and flag:
        print "MD5 Constants Present"
        flag = False
