import segno
from urllib.request import urlopen

qrcode = segno.make_qr("First")
qrcode.save("lightblue_qr.png" , scale = 5 , light = "lightblue")

qrcode1 = segno.make_qr("https://www.linkedin.com/in/akshit-rao-73b962228/")
qrcode1.save("link_qr.png" , scale = 5 , light = "red")

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=F2RnxZnubCM")
titanic_url = urlopen("https://media.giphy.com/media/mQQZiX8MX07EgeAcgm/giphy.gif")
slts_qrcode.to_artistic(
    background=titanic_url,
    target="animated_qrcode.gif",
    scale=5 )