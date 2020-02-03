import hashlib
from time import ctime,sleep
from os import get_terminal_size,system
r1 = "\x1b[31;1;7m"
r2 = "\x1b[32;1;7m"
r3 = "\x1b[33;1;7m"
r4 = "\x1b[34;1;7m"
r5 = "\x1b[35;1;7m"
r6 = "\x1b[36;1;7m"
o = "\x1b[0m"
def encode ():
    mes = str (input (r2+"masukan pesan :"+o+" \x1b[33;1m")).strip ();print ("\x1b[36;1;3mmethod\x1b[0m:\n\t\x1b[34;1m[\x1b[36;1m01\x1b[34;1m] \x1b[32;1mmd5\n\t\x1b[34;1m[\x1b[36;1m02\x1b[34;1m] \x1b[32;1msha-1\n\t\x1b[34;1m[\x1b[36;1m03\x1b[34;1m] \x1b[32;1msha-224\n\t\x1b[34;1m[\x1b[36;1m04\x1b[34;1m] \x1b[32;1msha-256\n\t\x1b[34;1m[\x1b[36;1m05\x1b[34;1m] \x1b[32;1msha-384\n\t\x1b[34;1m[\x1b[36;1m06\x1b[34;1m] \x1b[32;1msha3-224\n\t\x1b[34;1m[\x1b[36;1m07\x1b[34;1m] \x1b[32;1msha3-256\n\t\x1b[34;1m[\x1b[36;1m08\x1b[34;1m] \x1b[32;1msha3-384\n\t\x1b[34;1m[\x1b[36;1m09\x1b[34;1m] \x1b[32;1msha3-512\n\t\x1b[34;1m[\x1b[36;1m10\x1b[34;1m] \x1b[32;1msha512\n"+o)
    while True:
        try:met = int(input (r3+"pilih method :"+o+" \x1b[31;1m"))
        except (EOFError,KeyboardInterrupt):exit ("\t\x1b[36;1;4mthanks gan"+o)
        except (ValueError):print ("\t\x1b[31;1;3mmasukan sebuah angka cuk :v"+o);continue
        if met not in [ff for ff in range (1,11)]:print ("\t\x1b[31;1;3mpilihan tidak ada"+o);continue
        else:break
    if met == 1 :hasil = hashlib.md5 (mes.encode ()).hexdigest ()
    elif met == 2:hasil = hashlib.sha1 (mes.encode ()).hexdigest ()
    elif met == 3:hasil = hashlib.sha224 (mes.encode ()).hexdigest ()
    elif met == 4:hasil = hashlib.sha256 (mes.encode ()).hexdigest ()
    elif met == 5:hasil = hashlib.sha384 (mes.encode ()).hexdigest ()
    elif met == 6:hasil = hashlib.sha3_224 (mes.encode ()).hexdigest ()
    elif met == 7:hasil = hashlib.sha3_256 (mes.encode ()).hexdigest ()
    elif met == 8:hasil = hashlib.sha3_384 (mes.encode ()).hexdigest ()
    elif met == 9:hasil = hashlib.sha3_512 (mes.encode ()).hexdigest ()
    elif met == 10:hasil = hashlib.sha512 (mes.encode ()).hexdigest ()
    ab,bb=get_terminal_size ()
    with open ("result.txt","a") as aa:aa.write ("#"*(5)+"\nwaktu : "+str (ctime ())+"\nawal : "+mes+"\nhasil : "+hasil+"\n\n\n")
    print ("\n\n\x1b[35;1;3;4mhasil lainnya bisa di lihat di"+o+"\n\t\x1b[35;1;3;4mresult.txt"+o);print ("\x1b[36;1;3mresult\x1b[0m :\n\x1b[32;1m"+"="*(int (ab/2))+"\n\x1b[33;1m"+hasil+o+"\n\x1b[32;1m"+"="*int( (ab/2))+o)
def decode ():
    try:
        with open ("wordlist.txt","r") as aa:aa = aa.read ()
    except (FileNotFoundError):exit ("\x1b[31;1;3mfile wordlist.txt tidak ditemukan\nsilahkan tambahkan sebuah file wordlist.txt"+o+"\n")
    bb = [ff for ff in aa.strip ("\n").split ("\n")];mes = str (input ("\x1b[32;1;7mmasukan kode hash :"+o+" \x1b[35;1m")).strip (" \" '");print ("\n\n\r\x1b[34;1mmemeriksa . . .",end="");hasil = "";method = ""
    try:
        for ii in bb:
            if hashlib.md5 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "md5";break
            elif hashlib.sha1 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha1";break
            elif hashlib.sha224 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha224";break
            elif hashlib.sha256 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha256";break
            elif hashlib.sha384 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha384";break
            elif hashlib.sha3_224 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha3-224";break
            elif hashlib.sha3_256 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha3-256";break
            elif hashlib.sha3_384 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha3-384";break
            elif hashlib.sha3_512 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha3-512";break
            elif hashlib.sha512 (ii.encode ()).hexdigest () == mes:hasil = ii;method = "sha512";break
    except (KeyboardInterrupt,EOFError):exit ("\x1b[32;1;3mthanks gan"+o)
    if len (hasil) > 0:
        with open ("result.txt","a") as aa:
            aa.write ("#"*(5)+"\nwaktu : "+str (ctime ())+"\nawal : "+mes+"\nmethod : "+method+"\nhasil : "+hasil+"\n\n\n")
        ab,bb=get_terminal_size ();print ("\r\x1b[35;1;3;4mhasil bisa dilihat di"+o+"\n\t\x1b[33;1mresult.txt\n\x1b[36;1;3mresult "+o+": \n\x1b[34;1m"+"="*(int (ab/2))+"\n");print ("\t"+r5+" hasil  :"+o+" \x1b[33;1m"+hasil+" \n\t"+r2+" method :"+o+" \x1b[36;1m"+method+o+"\n")
    else:
        print ("\r\x1b[31;1mhasil tidak ditemukan!"+o)
bau = ""
while True:
    system ("clear");print ("\n\n");print (b'\x1b[32;1m \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x84\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x84\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x84\xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\n \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x96\x91 \xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\n \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80\xe2\x96\x80\x1b[0m\x1b[36;1m\n==============================\x1b[0m\x1b[35;1m\n# \x1b[33;1mauthor   : \x1b[32;1mgumball watterson\x1b[35;1m\n# \x1b[33;1mcountry  : \x1b[32;1mindonesia\x1b[35;1m\n# \x1b[33;1mreligion : \x1b[32;1mislam\x1b[0m\n\x1b[36;1m==============================\x1b[0m'.decode ());print (bau+"\n\n \x1b[34;1m[\x1b[32;1m01\x1b[34;1m] "+r3+"encode"+o+"    \x1b[34;1m[\x1b[32;1m02\x1b[34;1m] "+r6+"decode"+o+"\n")
    try:
        pil = int (input (r6+"choose :"+o+" \x1b[31;1m"))
    except (ValueError):bau = "     "+r1+"harus masukan angka!"+o;continue
    except (KeyboardInterrupt,EOFError):exit ("\x1b[32;1;3mthanks gan"+o)
    if pil == 1:exit (encode ())
    elif pil == 2:exit (decode ())
    else:bau = "     "+r1+"pilih sesuai pilihan"+o;continue;
