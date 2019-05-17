text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

old = list(text)
#ord('z') = 122, ord(' ') = 32 , ord('a') = 97

for pos,ch in enumerate(old):
  if ord(ch) < 97 or ord(ch) > 122:
    continue
  elif ord(ch) <= 120:
    old[pos] = chr(ord(ch) +2)
  else:
    old[pos] = chr(ord(ch) - 24)

new = ''.join(old)
print(new)
	