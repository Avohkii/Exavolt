# gecko code for extended heap
HEAP_SIZE = 0x0218bbbb # update if we extend heap further
EXTENDED_HEAP = [
  0x04218060, 0x3c600220, # double heap from 17.5 mb to 34 mb
  0x04218070, 0x39430000, # remove trailing zeroes for chillin
  0x0421807c, 0x3cc000a0, # double fast mem to 10 MB from 5
]

DISABLE_HUD_CREATE = [
  0x0419836c, 0x60000000,
  0x04198370, 0x60000000,
  0x04198374, 0x60000000
]

HACKS = {
  "extended_heap" : EXTENDED_HEAP,
}
