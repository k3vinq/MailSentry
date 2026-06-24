# Error Analysis: error_analysis_distilbert

## False Positives (Actual: Safe -> Predicted: Phishing)
*Total False Positives in test set: 61*

### Sample FP #1
```text
empty
```

### Sample FP #2
```text
empty
```

### Sample FP #3
```text
flood pictures from the tunnels under pennzoil place in downtown houston bammelyoungfamilies - - - - - - - - - - - - - - - - - - - - - - - - - - - listbot sponsor - - - - - - - - - - - - - - - - - - - - - - - - - - get a low apr nextcard visa in 30 seconds ! 1 . fill in the brief application 2 . receive approval decision within 30 seconds 3 . get rates as low as 2 . 99 % intro or 9 . 99 % ongoing apr and no annual fee ! apply now ! http : / / www . bcentral . com / listbot / nextcard to unsubscribe , write to - unsubscribe @ listbot . com
```

### Sample FP #4
```text
empty
```

### Sample FP #5
```text
clickathome portal is here ! version 2 . 0 of the clickathome portal is now available ! log into www . clickathome . net now , from work or home ! access the pep system through the portal ! choose your reviewers and fill out your evaluations in the comfort and privacy of your home ! outlook web access and ehronline will be available soon ! the clickathome portal is fully customizable for you ! you choose the content on each page , as well as the look and feel ! note : the clickathome portal must be launched through an internet explorer browser , 5 . 0 or higher .
```

### Sample FP #6
```text
SPAM: This mail is probably spam.  The original message has been altered
SPAM: so you can recognise or block similar unwanted mail in future.
SPAM: See http://spamassassin.org/tag/ for more details.
SPAM: 
SPAM: Content analysis details:   (5.30 hits, 5 required)
SPAM: INVALID_DATE       (1.6 points)  Invalid Date: header (not RFC 2822)
SPAM: REMOVE_SUBJ        (1.7 points)  BODY: List removal information
SPAM: SPAM_PHRASE_05_08  (0.7 points)  BODY: Spam phrases score is 05 to 08 (medium)
SPAM:                    [score: 6]
SPAM: SUPERLONG_LINE     (-2.2 points) BODY: Contains a line >=199 characters long
SPAM: MSG_ID_ADDED_BY_MTA_3 (0.2 points)  'Message-Id' was added by a relay (3)
SPAM: MISSING_MIMEOLE    (1.6 points)  Message has X-MSMail-Priority, but no X-MimeOLE
SPAM: MISSING_OUTLOOK_NAME (1.7 points)  Message looks like Outlook, but isn't
SPAM: *************************************
*   Reich for Governor Committee    *
*   Newsletter Sign-up Confirmation *
*************************************Thank you for signing up for the Reich Report, the weekly newsletter of the Reich for Governor campaign. You can read our previous newsletter on our website at http://RobertReich.org/gov/Newsletter.asp . If you would like to volunteer for the campaign, please contact our volunteer coordinator, Meg Ansara, at Meg@RobertReich.org or call (617) 547-2206 x132. Our headquarters is located at 625 Mount Auburn Street, near the Star Market in Cambridge.  We are open from 9 am to 9 pm Monday through Thursday, 9 am to 6 pm Friday, 10 am to 6 pm Saturday, and 12 noon to 8 pm on Sundays. We are a bus ride away from Harvard Square (bus #71 or #73) and parking is readily available in the back of the building. We encourage all Reich supporters to come to the headquarters for events, to volunteer for phone banking, or just to see how we operate. We encourage you to forward this e-mail to your friends, family, and colleagues, and ask them to sign up for our newsletter at http://www.robertreich.org/gov/emailpage.asp . Help us start a 'virtual' campaign!If you do not want to receive future newsletters, please send an e-mail to newsletter@RobertReich.org with 'Remove' as the subject line. -- Jesse Alan Gordon
Technology Director
Reich for Governor Committee
Jesse@RobertReich.org*************************************
*   Reich for Governor Committee    *
*   P.O. Box 381483                 *
*   Cambridge, MA 02238             *
*   http://www.RobertReich.org      *
*************************************
```

### Sample FP #7
```text
subscribe this message has been automatically generated in response to your mckinseyquarterly . com registration . you requested notification about new articles in the categories listed below . to confirm your enrollment , please reply to this message and remove any / all characters that may preceed the word subscribe . subscribe economic - performance subscribe retail subscribe environment subscribe countries subscribe strategy subscribe interviews subscribe financial - institutions subscribe energy subscribe telecommunications subscribe corporate - finance subscribe electronic - commerce
```

### Sample FP #8
```text
cdnow shipment confirmation dear daren , thank you for shopping at cdnow . please keep this email invoice for your records . on february 21 we shipped your order number 16840862 for the following item : cash / nelson : vhl storytellers format : cd quantity : 1 price : 11 . 49 to the following address via u . s . postal service : daren farmer 5519 clarkston ln spring , tx 77379 total number of items : 1 subtotal : $ 11 . 49 shipping : $ 2 . 99 sales tax : $ 0 . 00 - - - - - - - - - - shipment total : $ 14 . 48 your order was billed to daren farmer . this shipment completes your order and is paid in full . most orders arrive within 4 - 8 business days . however , in rare instances it may take up to 2 weeks . turn up the volume on your career ! bose audio products are legendary . so are bose careers ! for excitement , innovation and uncompromising performance , nothing takes you to a higher level than a job at bose . make a sound career move by visiting http : / / www . bose . com / hl 01 for complete information about your order ( number 16840862 ) or to confirm the status , click or copy / paste this link into your web browser : http : / / cdnow . com / myorder / otid = 16840862 you can also access your order history directly from our home page . please do not reply to this email . if you have questions about your order that are not addressed in your online order history , please visit our contact cdnow page using this link : http : / / cdnow . com / service fast forward rewards ( tm ) program points for this order will be credited in your membership summary as " points earned . " thanks again for your order . sincerely , customer service cdnow , inc . your music . your store . http : / / cdnow . com aol keyword : cdnow 1757978
```

### Sample FP #9
```text
empty
```

### Sample FP #10
```text
empty
```

### Sample FP #11
```text
empty
```

### Sample FP #12
```text
empty
```

### Sample FP #13
```text
empty
```

### Sample FP #14
```text
empty
```

### Sample FP #15
```text
empty
```

## False Negatives (Actual: Phishing -> Predicted: Safe)
*Total False Negatives in test set: 22*

### Sample FN #1
```text
this works the latter allowed it to come within half a cable ' s length ; then , as if disdaining to dive , it took a little turn , and stopped a short distance off no msg two days passed , the steam was at half pressure ; a thousand schemes were tried to attract the attention and stimulate the apathy of the animal in case it should be met in those parts . little by little , ned land acquired a taste for chatting , and i loved to hear the recital of his adventures in the polar seas ! ! the darkness was then profound , and , however good the canadian ' s eyes .
```

### Sample FN #2
```text
fw : windows xp + office xp = 80 dol lars . hey guys , remember that website a couple of you asked about a while back that had oem software , like microsoft , adobe , corel or macromedia and such ( retail being say 700 bucks they ' d have it here for 99 bucks , etc etc ) . cassie found this one and it has fre e shipping . i even forwarded the email that was sent to me below that has everything they have in stock . i ' ve grabbed 9 titles myself , so i know they ' re good , just check out the list below and see if there ' s anything you ' re looking for , they even have some mac software in there . talk to you tommorow at work . s . kauffman - - - - - - - - - - - original message - - - - - - - - - - - from : cassie [ iiahby @ yahoo . tv ] sent : sun , 27 feb 2005 01 : 50 : 29 + 0600 to : cassiekauffman 37 @ yahoo . nl subject : fw : windows xp + office xp = 80 dol lars . microsoft windows software windows xp professional 69 . 95 windows xp professional with sp 2 full version 79 . 95 windows 2000 professional 59 . 95 windows 2000 advanced server 69 . 95 windows nt 4 . 0 server 49 . 95 windows nt 4 . 0 terminal server 49 . 95 windows millenium 59 . 95 windows 9 . 958 second edition 49 . 95 windows 9 . 958 49 . 95 windows 9 . 955 49 . 95 microsoft office software office xp professional 79 . 95 office 2000 premium edition pe ( 2 cd ) 59 . 95 office 9 . 957 sr 2 49 . 95 office 2003 professional ( 1 cd edition ) 89 . 95 microsoft visio 2003 professional 69 . 95 filemaker 7 . 0 professional 69 . 95 other microsoft software ms plus ! xp 59 . 95 ms sql server 2000 enterprise edition 69 . 95 ms visual studio . net architect edition ( 8 cd ) 139 . 95 ms encarta encyclopedia delux 2004 ( 3 cd ) 89 . 95 ms project 2003 professional 69 . 95 ms money 2004 69 . 95 ms streets and trips 2004 north america ( 2 cd ) 69 . 95 ms works 7 69 . 95 ms picture it premium 9 . 95 59 . 95 ms exchange 2003 enterprise server 69 . 95 adobe software for pc photoshop 7 our price : 69 . 95 pagemaker 7 ( 2 cd ) our price : 69 . 95 illustrator 10 our price : 69 . 95 acrobat 6 professional our price : 79 . 95 premiere 7 our price : 69 . 95 photoshop cs with imageready cs our price : 9 . 959 . 95 adobe creative suite standard ( 3 cd ) our price : 129 . 95 adobe creative suite premium ( 5 cd ) our price : 149 . 95 adobe photoshop elements 3 . 0 windows our price : 59 . 95 adobe indesign cs pagemaker edition our price : 69 . 95 adobe software for mac adobe actobat 6 . 0 pro ( apple macintosh ) our price : 79 . 95 adobe after effects 6 ( apple macintosh ) our price : 69 . 95 adobe illustrator cs ce ( apple macintosh ) our price : 69 . 95 adobe indesign cs ( apple macintosh ) our price : 69 . 95 adobe livemotion 2 . 0 ( apple macintosh ) our price : 69 . 95 adobe photoshop cs ( apple macintosh ) our price : 9 . 959 . 95 adobe premiere 6 . 5 ( apple macintosh ) our price : 89 . 95 macromedia software for pc dreamwaver mx 2004 our price : 69 . 95 flash mx 2004 our price : 69 . 95 fireworks mx 2004 our price : 69 . 95 freehand mx 11 our price : 69 . 95 macromedia software for mac macromedia director mx 2004 ( apple macintosh ) our price : 69 . 95 macromedia freehand mx ( apple macintosh ) our price : 69 . 95 macromedia dreamweaver mx 2004 ( apple macintosh ) our price : 69 . 95 macromedia fireworks mx 2004 ( apple macintosh ) our price : 69 . 95 macromedia flash mx 2004 ( apple macintosh ) our price : 69 . 95 macromedia studio mx 2004 with director mx 2004 ( apple macintosh ) our price : 139 . 95 corel software for pc corel draw graphics suite 11 our price : 59 . 95 corel photo painter 8 our price : 59 . 95 corel wordperfect office 10 our price : 69 . 95 other software for pc norton system works 2003 our price : 59 . 95 borland delphi 7 enterprise edition ( 2 cd ) our price : 69 . 95 quark xpress 6 passport multilanguage our price : 69 . 95 corel software for mac corel draw graphics suite 11 ( apple macintosh ) our price : 59 . 95 corel painter 8 ( apple macintosh ) our price : 59 . 95 other software for mac extensis portfolio 7 . 0 ( apple macintosh ) our price : 59 . 95 photoretouch pro 3 . 0 ( apple macintosh ) our price : 59 . 95 visit us today ! http : / / clydeulyrfbumt 8 cjrdu . mbnenbhaa . com / claus to be taken off the updates
```

### Sample FN #3
```text
hi 56281814119876554443333 we wwer house passle cli to stving this , remink on the site . 56281814119876554443333
```

### Sample FN #4
```text
madge , absence of proof is not proof of absence . if you ' re going to kick authority in the teeth , you might as well use two feet . here is my principle : taxes shall be levied according to ability to pay . that is the only american principle .
```

### Sample FN #5
```text

New Page 1
This page uses frames, but your browser doesn't support them.--DeathToSpamDeathToSpamDeathToSpam--
-------------------------------------------------------
This sf.net email is sponsored by:ThinkGeek
Welcome to geek heaven.
http://thinkgeek.com/sf
_______________________________________________
Spamassassin-Sightings mailing list
Spamassassin-Sightings@lists.sourceforge.net
https://lists.sourceforge.net/lists/listinfo/spamassassin-sightings

```

### Sample FN #6
```text
i just got mine nudge webster egan face = arial size = 2 > i love mickey mouse more than any woman i have ever known . - walt disney ( 1901 - 1966 ) a celebrity is a person who works hard all his life to become well known , then wears dark glasses to avoid being recognized . fred allen ( 1894 - 1956 ) / span >
```

### Sample FN #7
```text
this has worked for me marrow enemy i think there is a world market for maybe five computers . - thomas watson ( 1874 - 1956 ) ; chairman of ibm ; 1943 your highness ; i have no need of this hypothesis . - pierre laplace ( 1749 - 1827 ) ; to napoleon on why his works on celestial mechanics make no mention of god . you got to be careful if you dont know where youre going ; because you might not get there . - yogi berra
```

### Sample FN #8
```text
mid summer flag special : free shipping armstrong flag company spring special : free shipping order today and receive a free car flag free shipping on all orders over $ 35 . 00 . promo good thru june 30 th . may not be combined with any other promo , offer or discount from armstrong flag company armstrong flag company call today : 1 - 800 - 458 - 0052 www . armstrongflag . com armstrong flag company 20 park st . winchester , ma 01890 this e - mail message is an advertisement and / or solicitation .
```

### Sample FN #9
```text
hi hi i ' m ashley . i am such a cyber geek now . all i do is set online , read , chat and i am mostly on my site , updating and renovating it all the time . i am currently a collage student . i have lots of free time on my hands , so i decided to make a website about my life . the best thing about my site is that i finally got my self a program to verify age . dont ' worry its free . i made this so that minors won ' t be able to access my page . i am looking to meet new cyber friend , and who knows maybe even more then just friends ; d . http : / / codicil . calll 234 picture . com / as 5 /
```

### Sample FN #10
```text
best regards dear friend , good day to you . i may have to trouble your sense of personal achievement and reward for an opportunity properly taken advantage of . i am mr . michael ramsey , a representative and an attorney to kenneth lay , the former chairman & ceo , enron corp . industry : energy & natural resources home , is presently in jail and facing trial on charges of corruption and embezzlement of funds while in power . he deposited twenty one million u . s dollars ( $ 21 , 000 , 000 . 00 ) with me when he was in power as the chairman . i am contacting you because i want you to deal with the finance house and claim the money on my behalf since i have declared that the funds belong to my foreign business partner . you shall also be required to assist me in investment in your country . i hope to trust you as a god fearing person who will not sit on this money when you claim it , rather assist me properly , shared in these percentages , 60 % to me and 40 % to you . when i receive your positive response i will let you know where the finance houses his and the document ' s to lay claims to the funds , which is very important . what i need is for you to indicate your interest that you will assist us by receiving the money on my behalf in europe . for this , you shall be considered to be the beneficiary to the funds . the project in brief , is that the funds with which we intend to carry out our proposed investments in your country , is presently in the custody of a bank in europe . i do not want the government of my country to know about the money because they will believe i got the money from the sales of enron stock when he was the chairman of enron & c . e . o . once i have your details in full , the finance house will contact you for release of the funds to your account as soon as payment is effected , and the amount mentioned above is successfully transferred into your account , i intend to use my own share in acquiring some estates abroad . for this too you shall also be the overseas manager of all our properties and you will be paid based on a certain percentage agreed on by both parties . i guarantee you that this will be executed under a legitimate arrangement that will protect you from any breach of the law . please get in touch with me urgently by e - mail : michaelramseyl 200 @ myway . com i am presently in london . please , provide me the following : 1 . your full name 2 . your telephone number and fax number 3 . your contact address best regards , michael ramsey .
```

### Sample FN #11
```text
call for papers : the international joint conferences on computer , information and systems sciences and engineering cisse 05 if you received this email in error , please forward it to the appropriate department at your institution please do not reply to this message , your reply will not be received . if you need to contact us , please email us at info @ cisse 2005 . org * international joint conferences on computer , information , * * and systems sciences , and engineering ( cisse 05 ) * * * * * * http : / / www . cisse 2005 . org * * * * * * * december 10 - 20 , 2005 sponsored by : institute of electrical & electronics engineers ( ieee ) university of bridgeport conference overview cisse 05 provides a virtual forum for presentation and discussion of the state - of the - art research on computers , information and systems sciences and engineering . the virtual conference will be conducted through the internet using web - conferencing tools , made available by the conference . authors will be presenting their powerpoint , audio or video presentations using web - conferencing tools without the need for travel . conference sessions will be broadcast to all the conference participants , where session participants can interact with the presenter during the presentation and ( or ) during the q & a slot that follows the presentation . this international conference will be held entirely on - line . the accepted and presented papers will be made available after the conference both on a cd and as a book publication . conference participants - authors , presenters and attendees - only need an internet connection and sound available on their computers in order to be able to contribute and participate in this international ground - breaking conference . the on - line structure of this high - quality event will allow academic professionals and industry participants to contribute work and attend world - class technical presentations based on rigorously refereed submissions , live , without the need for investing significant travel funds or time out of the office . potential non - author conference attendees who cannot make the on - line conference dates are encouraged to register , as the entire joint conferences will be archived for future viewing . please feel free to download the call for papers at : http : / / www . cisse 2005 . org / cfpcisseo 5 . doc ( microsoft word format ) or http : / / www . cisse 2005 . org / cfpcisseo 5 . pdf ( adobe pdf format ) cisse 05 is composed of the following four conferences : * international conference on industrial electronics , technology & automation ( ieta 05 ) topics : advanced and distributed control systems , intelligent control systems ( nn , fl , ga , . etc ) , expert systems , man machine interaction , data fusion , factory automation , robotics , motion control , machine vision , mems sensors and actuators , sensors fusion , power electronics , high frequency converters , motors and drives , power converters , power devices and components , electric vehicles and intelligent transportation , process automation , factory communication , manufacturing information system advances in manufacturing systems , industrial applications of multi media , intelligent systems instrumentation , industrial instrumentation , modeling and simulation , signal processing , image and data processing , vr and parallel systems . conference page : http : / / www . cisse 2005 . org / ieta . aspx * international conference on telecommunications and networking ( teneo 5 ) topics : optical networks and switching , computer networks , network architectures and equipment , access technologies , telecommunication technology , coding and modulation technique , modeling and simulation , spread spectrum and cdma systems , ofdm technology , space - time coding , ultra wideband communications , medium access control , spread spectrum , wireless lan : ieee 802 . 11 , hiperlan , bluetooth , cellular wireless networks , cordless systems and wireless local loop , mobile network layer , mobile transport layer , support for mobility , conventional encryption and message confidentiality , block ciphers design principles , block ciphers modes of operation , public - key cryptography and message authentication , authentication application , stenography , electronic mail security , web security , ip security , firewalls , computer forensics . conference page : http : / / www . cisse 2005 . org / tene . aspx * international conference on systems , computing sciences and software engineering ( scss 05 ) topics : grid computing , internet - based computing models , resource discovery , programming models and tools , e - science and virtual instrumentation , biometric authentication , computers for people of special needs , human computer interaction , information and knowledge engineering , algorithms , parallel and distributed processing , modeling and simulation , services and applications , embedded systems and applications , databases , programming languages , signal processing theory and methods , signal processing for communication , signal processing architectures and implementation , information processing , geographical information systems , object based software engineering , parallel and distributed computing , real time systems multiprocessing , file systems and i / o , kernel and os structures . conference page : http : / / www . cisse 2005 . org / scss . aspx * international conference on engineering education , instructional technology , assessment , and e - learning ( eiae 05 ) topics : instructional design , accreditation , curriculum design , educational tools , 2 - 2 - 2 platforms , teaching capstone design , teaching design at the lower levels , design and development of e - learning tools , assessment methods in engineering , development and implementation of e - learning tools , economical and social impacts of e - learning , platforms and systems for k - 12 / industry and higher education cooperation . conference page : http : / / www . cisse 2005 . org / eiae . aspx paper submission prospective authors are invited to submit full papers electronically in microsoft word or pdf format through the website of each conference at http : / / www . cisse 2005 . org . accepted papers must be presented in the virtual conference by one of the authors . to submit your paper , visit http : / / www . cisse 2005 . org / author / submit . aspx or visit the individual conference pages . important dates paper submission : september 30 , 2005 notification of acceptance : october 28 , 2005 final manuscript and registration : november 18 , 2005 cisse 2005 66 glenbrook rd stamford , ct 06902 this e - mail message is an advertisement and / or solicitation .
```

### Sample FN #12
```text
referred by , james hi , i found following web site quite interesting . i am sure it will ease your access to middle eastern markets . http : / / www . ceobusinessclub . org regards , james
```

### Sample FN #13
```text
sci - fi convention hi , i was asked to pass this on as you might be interested . the large infinity convention in cardiff in july has now confirmed their star wars , dr . who and star trek guests - it looks to be one of the largest events that part of the uk has seen for some time , and great fun . their site is at http : / / www . cf . ac . uk / ccin / main / ents / sffc / infinity . html and is in aid of children 's cancer . the guests include dave prowse ( darth vader ) , colin baker ( 6th dr . who ) , ed bishop ( cmdr . straker ufo ) , authors diane duane and peter morewood and many more . ideal for the family or with friends . regards , mike
```

### Sample FN #14
```text
service cancellation as per phone conversation , please cancel my service as of 8 / 8 / 05 . my customer id number is 1302 should you need to contact me in person regarding this matter please call ken or charlotte steury at 260 . 969 . 2750 . thank - you ! charlotte ken steury - abr , crs , e - pro , grireal estate ' s " information central " ken @ nearrealtors . com 260 . 969 . 2750 direct line 800 . 226 . near toll freecharlotte steury - licensed assistant closing marketing specialistcsteury @ nearrealtors . com 260 . 484 . 5888 ext . 200 near , realtorsl 1535 leo rd . , l 2 fort wayne , in 46845 confidentiality statement : this e - mail message , including anyattachment ( s ) , contains information that may be confidential . thisinformation is intended only for the use of the individuals or entitieslisted above . if you are not the intended recipient , you are herebynotified that any disclosure , copying , distribution , or action taken inreliance on the contents of these documents is strictly prohibited . if youhave received this information in error , please notify the senderimmediately and arrange for the return or destruction of these documents .
```

### Sample FN #15
```text
jeanie whittaker qhc 775 bryce manning - http : / / bedraggle . tortricidpeel . net bqlo 23
```

