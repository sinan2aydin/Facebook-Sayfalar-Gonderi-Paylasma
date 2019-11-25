# Facebook
Facebook sayfalarda otomatik paylaşım yapmak için düzenlendi.
Bu program ile, tek bir tıklama ile facebook sayfanızda, Python Selenium kullanarak paylaşım yapabilirsiniz.

Programı kullanmadan önce, paylaşım yapılacak fotoğrafların hazır bulunması gerekiyor.

Program, belirlemiş olduğunuz klasördeki fotoğraflardan rastgele 1 tane fotoğraf seçiyor ve bu fotoğrafı facebook sayfasına girerek gönderiyor ve bu fotoğrafı ismi ne ise, fotoğrafın ismini de iletinizin text kısmına yazıyor.

Mesela, ABC.jpg ismindeki bir fotoğraf var ise, Gönderinin text kısmına, ABC yazıyor.

İleti gönderildikten sonra, gönderilen fotoğraf, klasörünüzün içindeki "eklendi" isimli bir klasöre gönderiliyor.
Eğer fotoğrafların alındığı bölümde fotoğraf kalmamışsa; eklendi klasöründeki tüm fotoğraflar ana klasöre geliyor ve işlem aynen devam ediyor.

Fotoğrafın paylaşım sırası yok. Fotoğraf seçimi random olarak yapılıyor.

Python Selenium için Chrome yüklü olması gerekiyor.

Aşağıdaki alanları kendinize göre dolduracaksınız.

Facebook Pages
username.send_keys("XXXXX")
Bu kısımda facebook kullanıcı adı girilecek.

password.send_keys("XXXXX")
Bu kısımda facebook şifresi girilecek.

driver.get("https://www.facebook.com/XXXXX/")
Bu kısımda, facebook'da paylaşım yapılmak istenen sayfa URL'i girilecek.

klasor="XXXXXXX"
Bu kısım, Fotoğraf çektiğimiz klasörün ismi girilecek. (Son Klasör)

path, dirs, files = next(os.walk("C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\"+klasor))
Burada, Fotoğrafların bulunduğu Dosya yolu girilecek. (Son dosyayı üstte klasor olarak adlandırmıştık zaten)

source = 'C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\eklendi\\'
Paylaşımı yapılan fotoğrafların bulunduğu dosyanın içerisinde "eklendi" adındaki klasör var. Yani paylaşımı yapılan fotoğraflar otomatik bu klasöre atılacak.

dest1 = 'C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\'
Dosya yolunu bu şekilde yazıyoruz.

dl = os.path.join('C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor)
Dosya yolu aynı şekilde.

go = os.path.join('C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\eklendi')
Eklenen fotoğrafların dosya yolu yine.

rastgele_dosya=random.choice([x for x in os.listdir("C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\"+klasor) if os.path.isfile(os.path.join("C:\\Users\\ELF\\Desktop\\qqq\\z-facebooklar\\"+klasor, x))])
Dosya yoluncan rastgele bir fotoğraf seçilip paylaşım yapılacak. Burada yine dosya yolu bölümlerini kendinize göre uyarlayın.

tam_dosya_ismi = 'C:\\Users\\ELF\Desktop\\qqq\\z-facebooklar\\'+klasor+'\\'+rastgele_dosya
Yine dosya yolu.
