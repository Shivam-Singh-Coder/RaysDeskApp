create table signup
( 
sn varchar(50),
role int,
Uname varchar(150),
u_id varchar(150)  ,
sec_qus varchar(300),
sec_ans varchar(250) ,
pas varchar(200),
stat varchar(5),
bcode varchar (25)
)
;
create table registration
(
    reg_no varchar(150),
    reg_date date,
    sname varchar(200),
    fname varchar(200),
    mname varchar(200),
    sdob date,
    email varchar(150),
    cont_no varchar(15),
    prog varchar(300),
    blood_grp varchar(10),
    clg_name varchar(200),
    gender varchar(10),
    prmt_add varchar(300),
    dis varchar(100),
    stt varchar(300),
    sphoto blob,
    aadhar blob,
    cor_add varchar(300),
    bcode varchar (25)
)
 ;
 create table certificate
 (
    cref_no varchar(50) ,
    cer_date date,
    reg_no varchar(50)  ,
    course varchar(200) ,
    sname varchar (200) ,
    fname varchar(200) ,
    cstart date ,
    cend date ,
    stu_pic blob,
    study_c varchar(500),
    us_id varchar(200),
    bcode varchar (25)
 )
 ;
 create table marksheet(
   cref_no varchar(50) ,
    mark_date date,
    reg_no varchar(50)  ,
    sname varchar (200) ,
    fname varchar(200) ,
    course varchar(200) ,
    dur varchar(200),
    study_c varchar(500),
    mod_cov varchar(1500),
    mod_name varchar(1500),
    theory varchar(500),
    lab varchar(500),
    us_id varchar(200),
    bcode varchar (25)
 )
 ;
 create table internship
 (
    intern_no varchar(50) ,
    int_date date,
    sname varchar (200) ,
    fname varchar(200) ,
    gender varchar(200) ,
    dob date ,
    cont_no varchar(500),
    email_id varchar(500),
    coll_name varchar(500),
    pro_tit varchar(500),
    dur varchar(500),
    techno varchar(500),
    guide_name varchar(500),
    stip_amt varchar(500),
    stu_pic blob,
    study_c varchar(500),
    study_add varchar(500),
    us_id varchar(200),
    bcode varchar (25)
 )
 ;
 create table perf_report(
   intern_no varchar(50) ,
    int_date date,
    sname varchar (200) ,
    fname varchar(200) ,
    pro_tit varchar(500),
    os varchar(500),
    backend varchar(500),
    frontend varchar(500),
    databas varchar(500),
    tl_name varchar(500),
    team_meb varchar(500),
    meb_name varchar(500),
    dbms varchar(500),
    interface varchar(500),
    back varchar(500),
    testing varchar(500),
    documentation varchar(500),
    us_id varchar(200),
    bcode varchar (25)
 )
 ;
 create table admission 
 (
    adm_no varchar(50) ,
    adm_date date,
    reg_no varchar(30) ,
    cou_apply varchar(300) ,
    fee varchar(30) ,
    dis varchar(150),
    bcode varchar (25)
 )
 ;
 create table course
 (
    cid varchar(25),
    cname varchar(150),
    cdur varchar(150),
    cfee varchar(12),
    otp varchar(12),
    bcode varchar (25)
 )
;
create table money_receipt
(
    recpt_no varchar(150),
    rdate date,
    aform_no varchar(150),
    cash varchar(20),
    upi varchar(20),
    cheque varchar(20),
    dd varchar(20),
    dues_amt varchar(15) ,
    ins_date date,
    rec_from varchar(200) ,
    reg_no varchar(150),
    bcode varchar (25)
)
;
CREATE TABLE branch_details (
  sn int NOT NULL AUTO_INCREMENT,
  bcode varchar(250),
  date varchar(45),
  bname varchar(300),
  bcont_pr varchar(200),
  email varchar(150),
  phno varchar(50),
  addr varchar(200),
  state1 varchar(200),
  dist varchar(200),
  reg_no int,
  adm_no int,
  cid int,
  receipt_no int,
  PRIMARY KEY (sn)
) 
;
create table state(
   ad int,
   ar int,
   am int,
   br int,
   cg int,
   dl int,
   ga int,
   gj int,
   hr int,
   hp int,
   jk int,
   jh int,
   ka int,
   kl int,
   ld int,
   mp int,
   mh int,
   mn int,
   ml int,
   mz int,
   nl int,
   od int,
   py int,
   pb int,
   rj int,
   sk int,
   tn int,
   ts int,
   tr int,
   up int,
   uk int,
   wb int,
   an int,
   ch int,
   dn int,
   la int)
;
insert into state values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
create table book_details
(
   reg_no varchar(40),
   sname varchar(300),
   bname varchar(500),
   aname varchar(500),
   pname varchar(500),
   issue_dt date,
   subm_dt date,
   receice varchar(500),
   bcode varchar (25)
)
;
create table automatic 
(
   reg_no int,
   adm_no int,
   cid int,
   recpt_no int,
   ch varchar(20),
   cert_ch varchar(20),
   cert_no int
)
;
insert into automatic values(
  0,0,0,0,'A','A',0
)
;
create table state1(
    stat varchar(50),
    distr longtext
)
;
insert into state1 values('Bihar','Araria,Arwal,Aurangabad,Banka,Begusarai,Bhagalpur,Bhojpur,Buxar,Darbhanga,East Champaran(Motihari),Gaya,Gopalganj,Jamui,Jehanabad,Kaimur(Bhabua),Katihar,Khagaria,Kishanganj,Lakhisarai,Madhepura,Madhubani,Munger(Monghyr),Muzaffarpur,Nalanda,Nawada,Patna,Purnia(Purnea),Rohtas,Saharsa,Samastipur,Saran,Sheikhpura,Sheohar,Sitamarhi,Siwan,Supaul,Vaishali,West Champaran(Bettiah)')
;
insert into state1 values('Uttar Pradesh','Agra,Aligarh,Allahabad,Ambedkar Nagar,Amethi,Amroha,Auraiya,Azamgarh,Baghpat,Bahraich,Ballia,Balrampur,Banda,Barabanki,Bareilly,Basti,Bhadohi,Bijnor,Budaun,Bulandshahr,Chandauli,Chitrakoot,Deoria,Etah,Etawah,Faizabad,Farrukhabad,Fatehpur,Firozabad,Gautam Buddha Nagar (Noida),Ghaziabad,,Ghazipur,Gonda,Gorakhpur,Hamirpur,Hapur (Panchsheel Nagar),Hardoi,Hathras,Jalaun,Jaunpur,Jhansi,Kannauj,Kanpur Dehat,Kanpur Nagar,Kasganj,Kaushambi,Kushinagar,Lakhimpur Kheri,Lalitpur,Lucknow,Maharajganj,Mahoba,Mainpuri,Mathura,Mau,Meerut,Mirzapur,Moradabad,Muzaffarnagar,Pilibhit,Pratapgarh,Raebareli,Rampur,Saharanpur,Sambhal,Sant Kabir Nagar,Sant Ravidas Nagar (Bhadohi),Shahjahanpur,Shamli,Shravasti,Siddharthnagar,Sitapur,Sonbhadra,Sultanpur,Unnao')
;
insert into state1 values('Andhra Pradesh','Anantapur,Chittoor,East Godavari,Guntur,Krishna,Kurnool,Nellore,Prakasam,Srikakulam,Visakhapatnam,Vizianagaram,West Godavari,Kadapa (YSR)')
;
insert into state1 values('Arunachal Pradesh','Tawang,West Kameng,East Kameng,Papumpare,Kurung Kumey,Kra Daadi,Lower Subansiri,Upper Subansiri,West Siang,East Siang,Siang,Upper Siang,Dibang Valley,Lower Dibang Valley,Lohit,Namsai,Anjaw,Changlang,Tirap,Longding')
;
insert into state1 values('Assam','Baksa,Barpeta,Biswanath,Bongaigaon,Cachar,Charaideo,Chirang,Darrang,Dhemaji,Dhubri,Dibrugarh,Dima Hasao,Goalpara,Golaghat,Hailakandi,Hojai,Jorhat,Kamrup,Kamrup Metropolitan,Karbi Anglong,Karimganj,Kokrajhar,Lakhimpur,Majuli,Morigaon,Nagaon,Nalbari,Dima Hasao,Sivasagar,Sonitpur,South Salamara-Mankachar,Tinsukia,Udalguri,West Karbi Anglong')
;
insert into state1 values('Chattisgarh','Balod,Baloda Bazar,Balrampur,Bastar,Bemetara,Bijapur,Bilaspur,Dantewada,Dhamtari,Durg,Gariaband,Janjgir-Champa,Jashpur,Kanker,Kabirdham,Korba,Kondagaon,Mahasamund,Mungeli,Narayanpur,Raigarh,Raipur,Rajnandgaon,Sukma,Surajpur,Surguja')
;
insert into state1 values('Delhi','Central Delhi,East Delhi,New Delhi,North Delhi,North East Delhi,North West Delhi,Shahdara,South Delhi,South East Delhi,South West Delhi,West Delhi')
;
insert into state1 values('Goa','North Goa,South Goa')
;
insert into state1 values('Andaman & Nicobar','Nicobar district,North and Middle Andaman district,South Andaman district')
;
insert into state1 values('Gujarat','Ahmedabad,Amreli,Anand,Aravalli,Banaskantha (Palanpur),Bharuch,Bhavnagar,Botad,Chhota Udepur,Dahod,Dangs (Ahwa),Devbhoomi Dwarka,Gandhinagar,Gir Somnath,Jamnagar,Junagadh,Kheda (Nadiad),Kutch (Bhuj),Mahisagar (Lunavada),Mehsana,Morbi,Narmada (Rajpipla),Navsari,Panchmahal (Godhra),Patan,Porbandar,Rajkot,Sabarkantha (Himmatnagar),Surat,Surendranagar,Tapi (Vyara),Vadodara,Valsad')
;
insert into state1 values('Haryana','Ambala,Bhiwani,Charkhi Dadri,Faridabad,Fatehabad,Gurugram (Gurgaon),Hisar,Jhajjar,Jind,Kaithal,Karnal,Kurukshetra,Mahendragarh,Nuh,Palwal,Panchkula,Panipat,Rewari,Rohtak,Sirsa,Sonipat,Yamunanagar')
;
insert into state1 values('Himachal Pradesh','Bilaspur,Chamba,Hamirpur,Kangra,Kinnaur,Kullu,Lahaul and Spiti.Mandi,Shimla,Sirmaur,Solan,Una')
;
insert into state1 values('Jammu & Kashmir','Anantnag,Bandipora,Baramulla,Budgam,Doda,Ganderbal,Jammu,Kathua,Kishtwar,Kulgam,Kupwara,Leh,Poonch,Pulwama,Rajouri,Ramban,Reasi,Samba,Shopian,Srinagar')
;
insert into state1 values('Jharkhand','Bokaro,Chatra,Deoghar,Dhanbad,Dumka,East Singhbhum (Jamshedpur),Garhwa,Giridih,Godda,Gumla,Hazaribagh,Jamtara,Khunti,Koderma,Latehar,Lohardaga,Pakur,Palamu,Ramgarh,Ranchi,Sahibganj,Seraikela-Kharsawan,Simdega,West Singhbhum (Chaibasa)')
;
insert into state1 values('Karnataka','Bagalkot,Ballari (Bellary),Belagavi (Belgaum),Bengaluru (Bangalore) Rural,Bengaluru (Bangalore) Urban,Bidar,Chamarajanagar,Chikballapur,Chikkamagaluru (Chikmagalur),Chitradurga,Dakshina Kannada,Davangere,Dharwad,Gadag,Hassan,Haveri,Kalaburagi (Gulbarga),Kodagu,Kolar,Koppal,Mandya,Mysuru (Mysore),Raichur,Ramanagara,Shivamogga (Shimoga),Tumakuru (Tumkur),Udupi,Uttara Kannada (Karwar),Vijayapura (Bijapur),Yadgir')
;
insert into state1 values('Kerala','Alappuzha,Ernakulam,Idukki,Kannur,Kasaragod,Kollam,Kottayam,Kozhikode,Malappuram,Palakkad,Pathanamthitta,Thiruvananthapuram,Thrissur,Wayanad')
;
insert into state1 values('Lakshadweep','Lakshadweep')
;
insert into state1 values('Madhya Pradesh','Agar Malwa,Alirajpur,Anuppur,Ashoknagar,Balaghat,Barwani,Betul,Bhind,Bhopal,Burhanpur,Chhatarpur,Chhindwara,Damoh,Datia,Dewas,Dhar,Guna,Gwalior,Harda,Hoshangabad,Indore,Jabalpur,Katni,Khandwa,Khargone,Mandla,Mandsaur,Morena,Narsinghpur,Narayanpur,Neemuch,Panna,Raisen,Rajgarh,Ratlam,Rewa,Sagar,Satna,Sehore,Seoni,Shahdol,Shajapur,Sheopur,Shivpuri,Sidhi,Singrauli,Tikamgarh,Ujjain,Umaria,Vidisha')
;
insert into state1 values('Maharashtra','Ahmednagar,Akola,Amravati,Aurangabad,Beed,Bhandara,Buldhana,Chandrapur,Dhule,Gadchiroli,Gondia,Hingoli,Jalgaon,Jalna,Kolhapur,Latur,Mumbai,Nagpur,Nanded,Nandurbar,Nashik,Osmanabad,Palghar,Parbhani,Pune,Raigad,Ratnagiri,Sangli,Satara,Sindhudurg,Solapur,Thane,Wardha,Washim,Yavatmal')
;
insert into state1 values('Manipur','Bishnupur,Chandel,Churachandpur,Imphal East,Imphal West,Jiribam,Kakching,Kamjong,Kangpokpi,Noney,Pherzawl,Senapati,Tamenglong,Tengnoupal,Thoubal,Ukhrul')
;
insert into state1 values('Meghalaya','East Garo Hills,West Garo Hills,South Garo Hills,North Garo Hills,South West Garo Hills,East Khasi Hills,West Khasi Hills,South West Khasi Hills,Ri Bhoi,East Jaintia Hills,West Jaintia Hills')
;
insert into state1 values('Mizoram','Aizawl,Champhai,Kolasib,Lawngtlai,Lunglei,Mamit,Saiha,Serchhip')
;
insert into state1 values('Nagaland','Dimapur,Kiphire,Kohima,Longleng,Mokokchung,Mon,Peren,Phek,Tuensang,Wokha,Zunheboto')
;
insert into state1 values('Odisha','Angul,Balangir,Balasore,Bargarh,Bhadrak,Boudh,Cuttack,Deogarh,Dhenkanal,Gajapati,Ganjam,Jagatsinghpur,Jajpur,Jharsuguda,Kalahandi,Kandhamal,Kendrapara,Kendujhar (Keonjhar),Khordha,Koraput,Malkangiri,Mayurbhanj,Nabarangpur,Nayagarh,Nuapada,Puri,Rayagada,Sambalpur,Sonepur,Sundargarh')
;
insert into state1 values('Punjab','Amritsar,Barnala,Bathinda,Faridkot,Fatehgarh Sahib,Fazilka,Ferozepur,Gurdaspur,Hoshiarpur,Jalandhar,Kapurthala,Ludhiana,Mansa,Moga,Muktsar,Nawanshahr (Shahid Bhagat Singh Nagar),Pathankot,Patiala,Rupnagar,Sahibzada Ajit Singh Nagar (Mohali),Sangrur,Tarn Taran')
;
insert into state1 values('Rajasthan','Ajmer,Alwar,Banswara,Baran,Barmer,Bharatpur,Bhilwara,Bikaner,Bundi,Chittorgarh,Churu,Dausa,Dholpur,Dungarpur,Hanumangarh,Jaipur,,Jaisalmer,Jalore,Jhalawar,Jhunjhunu,,,Jodhpur,Karauli,Kota,Nagaur,Pali,Pratapgarh,Rajsamand,Sawai Madhopur,Sikar,Sirohi,Sri Ganganagar,Tonk,Udaipur')
;
insert into state1 values('Sikkim','East Sikkim,North Sikkim,South Sikkim,West Sikkim')
;
insert into state1 values('Tamil Nadu','Ariyalur,Chennai,Coimbatore,Cuddalore,Dharmapuri,Dindigul,Erode,Kanchipuram,Kanyakumari,Karur,Krishnagiri,Madurai,Nagapattinam,Namakkal,Nilgiris,Perambalur,Pudukkottai,Ramanathapuram,Salem,Sivaganga,Thanjavur,Theni,Thoothukudi (Tuticorin),Tiruchirappalli (Trichy),Tirunelveli,Tirupathur,Tiruppur,Tiruvallur,Tiruvannamalai,Tiruvarur,Vellore,Viluppuram,Virudhunagar')
;
insert into state1 values('Telangana','Adilabad,Bhadradri Kothagudem,Hyderabad,Jagitial,Jangaon,Jayashankar Bhupalpally,Jogulamba Gadwal,Kamareddy,Karimnagar,Khammam,Komaram Bheem Asifabad,Mahabubabad,Mahabubnagar,Mancherial,Medak,Medchal-Malkajgiri,Mulugu,Nagarkurnool,Nalgonda,Narayanpet,Nirmal,Nizamabad,Peddapalli,Rajanna Sircilla,Ranga Reddy,Sangareddy,Siddipet,Suryapet,Vikarabad,Wanaparthy,Warangal Rural,Warangal Urban,Yadadri Bhuvanagiri')
;
insert into state1 values('Tripura','Dhalai,Gomati,Khowai,North Tripura,Sepahijala,South Tripura,Unakoti,West Tripura')
;
insert into state1 values('Uttarakhand','Almora,Bageshwar,Chamoli,Champawat,Dehradun,Haridwar,Nainital,Pauri Garhwal,Pithoragarh,Rudraprayag,Tehri Garhwal,Udham Singh Nagar,Uttarkashi')
;
insert into state1 values('West Bengal','Alipurduar,Bankura,Birbhum,Cooch Behar,Dakshin Dinajpur (South Dinajpur),Darjeeling,Hooghly,Howrah,Jalpaiguri,Jhargram,Kalimpong,Kolkata (formerly Calcutta),Malda,Murshidabad,Nadia,North 24 Parganas,Paschim Bardhaman (West Bardhaman),Paschim Medinipur (West Medinipur),Purba Bardhaman (East Bardhaman),Purba Medinipur (East Medinipur),Purulia,South 24 Parganas,Uttar Dinajpur (North Dinajpur)')
;
insert into state1 values('Chandigarh','Lakshadweep')
;
insert into state1 values('Dadra & Nagar Haveli and Daman & Diu','Dadra and Nagar Haveli and Daman,Diu')
;
insert into state1 values('Pondicherry','Karaikal,Mahe,Pondicherry,Yanam')
;
commit;
