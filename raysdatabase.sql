CREATE TABLE `admission` (
  `adm_no` varchar(50) DEFAULT NULL,
  `adm_date` date DEFAULT NULL,
  `reg_no` varchar(30) DEFAULT NULL,
  `cou_apply` varchar(300) DEFAULT NULL,
  `fee` varchar(30) DEFAULT NULL,
  `disc_ty` varchar(100) DEFAULT NULL,
  `dis` varchar(150) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL,
  `u_id` varchar(450) DEFAULT NULL,
  `cancel` int DEFAULT NULL
);
CREATE TABLE `automatic` (
  `ch` varchar(5) DEFAULT NULL,
  `cert` int DEFAULT NULL,
  `yy` varchar(5) DEFAULT NULL,
  `cert_ch` varchar(20) DEFAULT NULL,
  `cert_no` int DEFAULT NULL,
  `int_no` int DEFAULT NULL,
  `int_ch` varchar(45) DEFAULT NULL
);
CREATE TABLE `book_details` (
  `reg_no` varchar(40) DEFAULT NULL,
  `sname` varchar(300) DEFAULT NULL,
  `bname` varchar(500) DEFAULT NULL,
  `aname` varchar(500) DEFAULT NULL,
  `pname` varchar(500) DEFAULT NULL,
  `issue_dt` date DEFAULT NULL,
  `subm_dt` date DEFAULT NULL,
  `receice` varchar(500) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL
);
CREATE TABLE `branch_details` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `bcode` varchar(250) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `bname` varchar(300) DEFAULT NULL,
  `bcont_pr` varchar(200) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phno` varchar(50) DEFAULT NULL,
  `addr` varchar(200) DEFAULT NULL,
  `state1` varchar(200) DEFAULT NULL,
  `dist` varchar(200) DEFAULT NULL,
  `reg_no` int DEFAULT NULL,
  `adm_no` int DEFAULT NULL,
  `adm_ch` varchar(45) DEFAULT NULL,
  `cid` int DEFAULT NULL,
  `rec_no` int DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `certificate` (
  `cref_no` varchar(50) DEFAULT NULL,
  `cer_date` date DEFAULT NULL,
  `reg_no` varchar(50) DEFAULT NULL,
  `course` varchar(200) DEFAULT NULL,
  `sname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `cstart` date DEFAULT NULL,
  `cend` date DEFAULT NULL,
  `study_c` varchar(500) DEFAULT NULL,
  `stu_pic` longblob,
  `bcode` varchar(45) DEFAULT NULL,
  `us_id` varchar(200) DEFAULT NULL,
  `cancel` int DEFAULT NULL
);
CREATE TABLE `course` (
  `cid` varchar(25) DEFAULT NULL,
  `cname` varchar(150) DEFAULT NULL,
  `mod_name` varchar(345) DEFAULT NULL,
  `mod_desc` varchar(5500) DEFAULT NULL,
  `cfee` varchar(12) DEFAULT NULL,
  `cdur` varchar(150) DEFAULT NULL,
  `otp` varchar(12) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL,
  `u_id` varchar(405) DEFAULT NULL
);
CREATE TABLE `internship` (
  `intern_no` varchar(50) DEFAULT NULL,
  `int_date` date DEFAULT NULL,
  `sname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `cont_no` varchar(500) DEFAULT NULL,
  `email_id` varchar(500) DEFAULT NULL,
  `coll_name` varchar(500) DEFAULT NULL,
  `pro_tit` varchar(500) DEFAULT NULL,
  `dur` varchar(500) DEFAULT NULL,
  `techno` varchar(500) DEFAULT NULL,
  `guide_name` varchar(500) DEFAULT NULL,
  `stip_amt` varchar(500) DEFAULT NULL,
  `study_c` varchar(500) DEFAULT NULL,
  `study_add` varchar(500) DEFAULT NULL,
  `stu_pic` longblob,
  `us_id` varchar(200) DEFAULT NULL,
  `bcode` varchar(45) DEFAULT NULL,
  `cancel` int DEFAULT NULL
);
CREATE TABLE `marksheet` (
  `cref_no` varchar(50) DEFAULT NULL,
  `mark_date` date DEFAULT NULL,
  `reg_no` varchar(50) DEFAULT NULL,
  `sname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `course` varchar(200) DEFAULT NULL,
  `dur` varchar(200) DEFAULT NULL,
  `study_c` varchar(500) DEFAULT NULL,
  `mod_cov` varchar(1500) DEFAULT NULL,
  `mod_name` varchar(1500) DEFAULT NULL,
  `theory` varchar(500) DEFAULT NULL,
  `lab` varchar(500) DEFAULT NULL,
  `us_id` varchar(200) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL
);
CREATE TABLE `money_receipt` (
  `recpt_no` varchar(150) DEFAULT NULL,
  `rdate` date DEFAULT NULL,
  `aform_no` varchar(150) DEFAULT NULL,
  `cash` varchar(20) DEFAULT NULL,
  `upi` varchar(20) DEFAULT NULL,
  `cheque` varchar(20) DEFAULT NULL,
  `dd` varchar(20) DEFAULT NULL,
  `dues_amt` varchar(15) DEFAULT NULL,
  `ins_date` date DEFAULT NULL,
  `rec_from` varchar(200) DEFAULT NULL,
  `reg_no` varchar(150) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL
);
CREATE TABLE `perf_report` (
  `intern_no` varchar(50) DEFAULT NULL,
  `int_date` date DEFAULT NULL,
  `sname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `pro_tit` varchar(500) DEFAULT NULL,
  `os` varchar(500) DEFAULT NULL,
  `backend` varchar(500) DEFAULT NULL,
  `frontend` varchar(500) DEFAULT NULL,
  `databas` varchar(500) DEFAULT NULL,
  `tl_name` varchar(500) DEFAULT NULL,
  `team_meb` varchar(500) DEFAULT NULL,
  `meb_name` varchar(500) DEFAULT NULL,
  `dbms` varchar(500) DEFAULT NULL,
  `interface` varchar(500) DEFAULT NULL,
  `back` varchar(500) DEFAULT NULL,
  `testing` varchar(500) DEFAULT NULL,
  `documentation` varchar(500) DEFAULT NULL,
  `us_id` varchar(200) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL
);
CREATE TABLE `registration` (
  `reg_no` varchar(150) DEFAULT NULL,
  `reg_date` date DEFAULT NULL,
  `sname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `mname` varchar(200) DEFAULT NULL,
  `sdob` date DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `cont_no` varchar(15) DEFAULT NULL,
  `prog` varchar(300) DEFAULT NULL,
  `blood_grp` varchar(10) DEFAULT NULL,
  `clg_name` varchar(200) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `prmt_add` varchar(300) DEFAULT NULL,
  `dis` varchar(100) DEFAULT NULL,
  `stt` varchar(300) DEFAULT NULL,
  `sphoto` longblob,
  `aadhar` longblob,
  `cor_add` varchar(300) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL,
  `u_id` varchar(200) DEFAULT NULL,
  `cancel` int DEFAULT NULL
);
CREATE TABLE `signup` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `role` varchar(45) DEFAULT NULL,
  `Uname` varchar(150) DEFAULT NULL,
  `u_id` varchar(150) DEFAULT NULL,
  `sec_qus` varchar(300) DEFAULT NULL,
  `sec_ans` varchar(250) DEFAULT NULL,
  `pas` varchar(200) DEFAULT NULL,
  `stat` varchar(25) DEFAULT NULL,
  `bcode` varchar(25) DEFAULT NULL,
  `cancel` int DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `state` (
  `ad` int DEFAULT NULL,
  `ar` int DEFAULT NULL,
  `am` int DEFAULT NULL,
  `br` int DEFAULT NULL,
  `cg` int DEFAULT NULL,
  `dl` int DEFAULT NULL,
  `ga` int DEFAULT NULL,
  `gj` int DEFAULT NULL,
  `hr` int DEFAULT NULL,
  `hp` int DEFAULT NULL,
  `jk` int DEFAULT NULL,
  `jh` int DEFAULT NULL,
  `ka` int DEFAULT NULL,
  `kl` int DEFAULT NULL,
  `ld` int DEFAULT NULL,
  `mp` int DEFAULT NULL,
  `mh` int DEFAULT NULL,
  `mn` int DEFAULT NULL,
  `ml` int DEFAULT NULL,
  `mz` int DEFAULT NULL,
  `nl` int DEFAULT NULL,
  `od` int DEFAULT NULL,
  `py` int DEFAULT NULL,
  `pb` int DEFAULT NULL,
  `rj` int DEFAULT NULL,
  `sk` int DEFAULT NULL,
  `tn` int DEFAULT NULL,
  `ts` int DEFAULT NULL,
  `tr` int DEFAULT NULL,
  `up` int DEFAULT NULL,
  `uk` int DEFAULT NULL,
  `wb` int DEFAULT NULL,
  `an` int DEFAULT NULL,
  `ch` int DEFAULT NULL,
  `dn` int DEFAULT NULL,
  `la` int DEFAULT NULL
);
CREATE TABLE `state1` (
  `stat` varchar(50) DEFAULT NULL,
  `distr` longtext
);
CREATE TABLE `blogs` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `headline` varchar(1000) DEFAULT NULL,
  `msg` longtext,
  `image` longblob,
  `author` varchar(100) DEFAULT NULL,
  `pub_date` date DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `certificate_details` (
  `cert_no` varchar(100) DEFAULT NULL,
  `regno` varchar(45) DEFAULT NULL,
  `inst_code` varchar(45) DEFAULT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `duration` varchar(45) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `marks` varchar(45) DEFAULT NULL,
  `sphoto` longblob,
  `issue_date` varchar(45) DEFAULT NULL
);
CREATE TABLE `internship_details` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `position` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `s_date` varchar(100) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `stipend` int DEFAULT NULL,
  `skill_req` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `placement` (
  `name` varchar(100) DEFAULT NULL,
  `image` longblob,
  `company` varchar(100) DEFAULT NULL,
  `package` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL
);
CREATE TABLE `rays_carear` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `position` varchar(500) DEFAULT NULL,
  `skil` varchar(5000) DEFAULT NULL,
  `mode` varchar(1000) DEFAULT NULL,
  `exp` varchar(100) DEFAULT NULL,
  `vacency` varchar(100) DEFAULT NULL,
  `clo_data` varchar(45) DEFAULT NULL,
  `place` varchar(500) DEFAULT NULL,
  `sal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `video_details` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `topic` varchar(500) DEFAULT NULL,
  `url` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
insert into automatic values(
  'A',0,0,'A',0,0,'A'
);
CREATE TABLE rays_intern_apply (
  sn int not NULL AUTO_INCREMENT,
  name varchar(200),
  mo_no varchar(200),
  email varchar(200),
  resume longblob,
  position varchar(200),
  mode varchar(200),
  PRIMARY KEY (sn)
);
CREATE TABLE rays_job_apply (
  sn int not NULL AUTO_INCREMENT,
  name varchar(200),
  mo_no varchar(200),
  email varchar(200),
  resume longblob,
  position varchar(200),
  mode varchar(200),
  PRIMARY KEY (sn)
);
CREATE TABLE `placement` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `image` longblob,
  `company` varchar(200) DEFAULT NULL,
  `package` varchar(200) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `msg` varchar(4400) DEFAULT NULL,
  `spic` longblob,
  PRIMARY KEY (`sn`)
);
CREATE TABLE `test` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(5500) DEFAULT NULL,
  `topic` varchar(5500) DEFAULT NULL,
  `q` longtext,
  `a` longtext,
  `o1` longtext,
  `o2` longtext,
  `o3` longtext,
  `o4` longtext,
  PRIMARY KEY (`sn`)
);
insert into state values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
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