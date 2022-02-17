# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger

import qrcode
from PIL import Image

encode = qrcode.QRCode(
    box_size = 6,
    version = 1,
    border = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H 
)

info = """ Student Information

Personal Information
	Name		: Jezell C. Domer
	Nickname(s)	: Seng, Kang, Berry, Jez
	Section		: BSCOE 1-6
	Gender		: Female
	Age			: 18 Years Old (19 this year)
	Birthday	: April 18, 2003
	Location	: Luzon, Philippines
	Phone Number: 09123456789
	School: Polytechnic University of the Philippines
	Course: Bachelor of Science in Computer Engineering
	E-mail: brrybrry671@gmail.com

Motto in Life
	Motto: Stop thinking others should love you first when you can already start loving and fighting for yourself. 
	Favorite Bible Verse: Psalm 144:15 Happy are the people whose God is the LORD!

Like(s)
	K-POP: BTS, TXT, ENHYPEN, STRAY KIDS, ASTRO, GOT7, EXO, CRAVITY
		   TWICE, BLACKPINK, AESPA, ITZY, FROMIS_9, KEP1ER, SNSD, RED VELVET
	Food: Chocolate, Strawberry, Chicken, Burger, Ampalaya, Adobo, French Fries

Hobbies:
	Watching Youtube, Dramas (K-drama and C-drama), Reading Wattpad Stories, Chatting with friends in Social Media (Facebook, Messenger, Twitter, Instagram, Discord)

Recommended Must-Watch: https://www.youtube.com/watch?v=fYZSl2Yro-Q"""

