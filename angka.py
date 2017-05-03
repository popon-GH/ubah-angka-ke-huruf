angka = raw_input("Masukan Angka:")
#angka = 1234567890


angka_str = str(angka)
angka_len = len(angka_str)
angka_list = list(angka_str)
satuan_list = ["", "ribu", "juta", "miliar", "triliun"]
angka_dict = {"0":"", "1":"se", "2":"dua ", "3":"tiga ", "4":"empat ", "5":"lima ", "6":"enam ", "7":"tujuh ", "8":"delapan ", "9":"sembilan "}
list_ratus_max = (angka_len // 3) -1
False = "Angka Salah"



#FUNGSI UNTUK PRINT JIKA INPUT SATU ANGKA
def fungsi_satu_angka():
#  print "fungsi_satu_angka"
  if angka_dict[str(angka)] == "se" :
    return "satu"
  elif angka == 0 :
    return "Nol"
  else :
    return angka_dict[str(angka)]

#FUNGSI UNTUK PRINT DUA ANGKA TERAKHIR
def fungsi_dua_angka(a,b):
#  print "fungsi_dua_angka dipanggil.."
  if angka_list[-b] == "1" and angka_list[-a] == "0":
    return "sepuluh "
  elif angka_list[-b] == "1" and angka_list[-a] > "0" :
    return angka_dict[angka_list[-a]] + "belas "
  elif angka_list[-a] == "1" and angka_list[-b] != "0":
    return angka_dict[angka_list[-b]] + "puluh satu "
  elif angka_list[-b] == "0" and angka_list[-a] == "1" :
    return "satu"
  elif angka_list[-b] == "0" :
    return angka_dict[angka_list[-a]]
  else :
    return angka_dict[angka_list[-b]] + "puluh " + angka_dict[angka_list[-a]]

#INI FUNGSI UNTUK PRINT TIGA ANGKA TERAKHIR
def fungsi_tiga_angka(a, b, c):
#  print "fungsi_tiga_angka dipanggil.."
  if angka_list[-c] == "0" :
    return fungsi_dua_angka(a,b)
  else :
    return angka_dict[angka_list[-c]] + "ratus " + fungsi_dua_angka(a,b)





#INI FUNGSI UNTUK PRINT LEBIH DARI 3 ANGKA
def fungsi_ratus(a):
#  print "fungsi_ratus dipanggil.."
  ax = angka_len - (angka_len - a)
  bx = ax + 1
  cx = ax + 2
  if fungsi_tiga_angka(ax,bx,cx) == "" :
    return ''
  else :
    return fungsi_tiga_angka(ax,bx,cx) + satuan_list[(a)//3]

#fungsi list pendukung fungsi ratus
def list_ratus(a):
  if a > (len(range(angka_len-3, 0 ,-3)) - 1) :
    #print a
    #print "False"
    return False
  elif angka_len % 3 == 1 :
    #print "modulus 1"
    return range(angka_len-3, 0 ,-3)[a]
  elif angka_len % 3 == 2 :
    #print "modulus 2"
    return range(angka_len-4, 0 ,-3)[a]


#fungsi angka depan yang ga 3
def fungsi_angka_depan():
#  print "fungsi_angka_depan dipanggil.."
  if angka_len % 3 == 1:
    if angka_list[0] == '1' and angka_len == 4 :
      return "se" + satuan_list[angka_len//3]
    elif angka_list[0] == '1':
      return "satu " + satuan_list[angka_len//3]
    else :
      return angka_dict[angka_list[0]] + satuan_list[angka_len//3]
  elif angka_len % 3 == 2:
    return fungsi_dua_angka(-1,0) + satuan_list[angka_len//3]
  else:
    return "jumlah angka dapat dibagi tiga"



#combo sebelum tamat
def angka_ga_abis_dibagi_tiga():
  print fungsi_angka_depan(),
  for i in range(list_ratus_max + 1):
    print fungsi_ratus(list_ratus(i)),
  return ""

def angka_abis_dibagi_tiga():
  for i in range(angka_len - 2 , 0, -3):
    print fungsi_ratus(i),
  return ""

def angka_kurang_dari_tiga():
  if angka_len == 1:
    return fungsi_satu_angka()
  elif angka_len == 2:
    return fungsi_dua_angka(angka_len - 1, angka_len)
  elif angka_len == 3 :
    return fungsi_tiga_angka(1,2,3)


def selesai():
  if angka_len < 3 :
    #print "angka_kurang_dari_tiga"
    return angka_kurang_dari_tiga()
  elif angka_len % 3 == 0 :
    #print "angka_abis_dibagi_tiga"
    return angka_abis_dibagi_tiga()
  elif angka_len % 3 != 0 :
    #print "angka_ga_abis_dibagi_tiga"
    return angka_ga_abis_dibagi_tiga()
  else :
    False


print "\nAngka: " + angka_str + " diproses.."
print "\nJumlah angka:"
print angka_len
print "\nlist angka:"
print angka_list
print "\nTerbilang:"
print selesai()
