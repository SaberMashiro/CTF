##一道base64隐写的题，看完对base64的理解更进了一步。
###代码是网上找的一个大佬的。原理懂了就好
####base64会将3*8的位转成4*6位。不够的添=补。因此，有几个=就有len*2位可以利用