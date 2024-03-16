class Data:
  def_init_(self):
    pass
  def daftar (self):
    nama lengkap = input("input nama lengkap: ")
    usia = input("input usia: ")
    jenis kelamin = input("input jenis kelamin: ")
    tanggal = input("input tanggal: ")
    bulan = input("input bulan: ")
    tahun = input("input tahun: ")
    email = input("input email: ")
    password = input("input password: ")
    main(nama_lengkap, usia, jenis_kelamin, tanggal, bulan, tahun, email, password)
   
    class main:
      def_init_(self,nama_lengkap,usia,jeniskelamin,tanggal,bulan,tahun,email,password)
  self.nama_lengkap = nama_lengkap
  self.usia = usia
  self.jenis_kelamin = jenis_kelamin
  self.tanggal = tanggal
  self.bulan = bulan
  self.tahun = tahun
  self.email = email
  self.password = password
  
  self.r = requests.Session()
  self.url = "https://mbasic.facebook.com/reg/?cid=103&refid=8&rtime =1708262799&hrc=1&wtsid=rdr_0s 7Cabjz06IVZRPXc&refsrc=deprecated&_rdr"

self.Create(self.url, self.nama_lengkap, self.email, self.jenis_kelamin, self.usia, self.tanggal, self.bulan, self.tahun, self.password)
