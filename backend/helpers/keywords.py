
def getKeywords():
    keywordDict =
        {'President':['biden','trump','obama'], "States":["Alaska","Alabama","Arkansas","American Samoa","Arizona","California","Colorado","Connecticut","District of Columbia","Delaware","Florida","Georgia","Guam","Hawaii","Iowa","Idaho","Illinois","Indiana","Kansas","Kentucky","Louisiana","Massachusetts","Maryland","Maine","Michigan","Minnesota","Missouri","Mississippi","Montana","North Carolina","North Dakota","Nebraska","New Hampshire",'New Jersey',"New Mexico","Nevada","New York","Ohio","Oklahoma","Oregon","Pennsylvania","Puerto Rico","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Virginia","Virgin Islands","Vermont","Washington","Wisconsin","West Virginia","Wyoming"],"Russia":["Putin","Kremlin","Moscow","Ukraine"],"Ukraine":["Russia","Donbas","Zelenskyy","Kyiv"], 
        "Congress":[
        'Brown',

        'Cantwell',

        'Cardin',

        'Carper',

        'Casey',

        'Feinstein',

        'Klobuchar',

        'Menendez',

        'Sanders',

        'Stabenow',

        'Tester',

        'Whitehouse',

        'Barrasso',

        'Wicker',

        'Collins',

        'Cornyn',

        'Durbin',

        'Graham',

        'McConnell',

        'Merkley',

        'Reed',

        'Risch',

        'Shaheen',

        'Warner',

        'Gillibrand',

        'Coons',

        'Manchin',

        'Aderholt',

        'Baldwin',

        'Bennet',

        'Bilirakis',

        'Bishop',

        'Blackburn',

        'Blumenauer',

        'Blumenthal',

        'Boozman',

        'Buchanan',

        'Bucshon',

        'Burgess',

        'Calvert',

        'Capito',

        'Carson',

        'Carter',

        'Cassidy',

        'Castor',

        'Chu',

        'Cicilline',

        'Clarke',

        'Cleaver',

        'Clyburn',

        'Cohen',

        'Cole',

        'Connolly',

        'Costa',

        'Courtney',

        'Crapo',

        'Crawford',

        'Cuellar',

        'Davis',

        'DeGette',

        'DeLauro',

        'DesJarlais',

        'Diaz-Balart',

        'Doggett',

        'Duncan',

        'Eshoo',

        'Fleischmann',

        'Foxx',

        'Garamendi',

        'Gosar',

        'Granger',

        'Grassley',

        'Graves',

        'Green',

        'Griffith',

        'Grijalva',

        'Guthrie',

        'Harris',

        'Heinrich',

        'Higgins',

        'Himes',

        'Hirono',

        'Hoeven',

        'Hoyer',

        'Huizenga',

        'Jackson Lee',

        'Johnson',

        'Johnson',

        'Johnson',

        'Jordan',

        'Kaptur',

        'Keating',

        'Kelly',

        'Lamborn',

        'Lankford',

        'Larsen',

        'Larson',

        'Latta',

        'Lee',

        'Lee',

        'Lofgren',

        'Lucas',

        'Luetkemeyer',

        'Luján',

        'Lynch',

        'Markey',

        'Matsui',

        'McCarthy',

        'McCaul',

        'McClintock',

        'McCollum',

        'McGovern',

        'McHenry',

        'McMorris Rodgers',

        'Meeks',

        'Moore',

        'Moran',

        'Murkowski',

        'Murphy',

        'Murray',

        'Nadler',

        'Napolitano',

        'Neal',

        'Norton',

        'Pallone',

        'Pascrell',

        'Paul',

        'Pelosi',

        'Peters',

        'Pingree',

        'Posey',

        'Quigley',

        'Rogers',

        'Rogers',

        'Rubio',

        'Ruppersberger',

        'Sablan',

        'Sarbanes',

        'Scalise',

        'Schakowsky',

        'Schiff',

        'Schumer',

        'Schweikert',

        'Scott',

        'Scott',

        'Scott',

        'Scott',

        'Sewell',

        'Sherman',

        'Simpson',

        'Smith',

        'Smith',

        'Smith',

        'Sánchez',

        'Thompson',

        'Thompson',

        'Thompson',

        'Thune',

        'Tonko',

        'Turner',

        'Van Hollen',

        'Velázquez',

        'Walberg',

        'Wasserman Schultz',

        'Waters',

        'Webster',

        'Welch',

        'Wilson',

        'Wilson',

        'Wittman',

        'Womack',

        'Wyden',

        'Young',

        'Amodei',

        'Bonamici',

        'DelBene',

        'Massie',

        'Payne',

        'Schatz',

        'Foster',

        'Titus',

        'Cotton',

        'Sinema',

        'LaMalfa',

        'Huffman',

        'Bera',

        'Swalwell',

        'Brownley',

        'Cárdenas',

        'Ruiz',

        'Takano',

        'Vargas',

        'Peters',

        'Frankel',

        'Duckworth',

        'Barr',

        'Warren',

        'King',

        'Kildee',

        'Wagner',

        'Daines',

        'Hudson',

        'Cramer',

        'Fischer',

        'Kuster',

        'Meng',

        'Jeffries',

        'Wenstrup',

        'Beatty',

        'Joyce',

        'Mullin',

        'Perry',

        'Cartwright',

        'Cruz',

        'Weber',

        'Castro',

        'Williams',

        'Veasey',

        'Stewart',

        'Kaine',

        'Kilmer',

        'Pocan',

        'Kelly',

        'Smith',

        'Booker',

        'Clark',

        'Norcross',

        'Adams',

        'Palmer',

        'Hill',

        'Westerman',

        'Gallego',

        'DeSaulnier',

        'Aguilar',

        'Lieu',

        'Torres',

        'Buck',

        'Carter',

        'Loudermilk',

        'Allen',

        'Bost',

        'Graves',

        'Moulton',

        'Moolenaar',

        'Dingell',

        'Emmer',

        'Rouzer',

        'Watson Coleman',

        'Stefanik',

        'Boyle',

        'Babin',

        'Beyer',

        'Plaskett',

        'Newhouse',

        'Grothman',

        'Mooney',

        'Radewagen',

        'Sullivan',

        'Ernst',

        'Tillis',

        'Rounds',

        'Kelly',

        'LaHood',

        'Davidson',

        'Comer',

        'Evans',

        'Kennedy',

        'Hassan',

        'Cortez Masto',

        'Schneider',

        'Biggs',

        'Khanna',

        'Panetta',

        'Carbajal',

        'Barragán',

        'Correa',

        'Blunt Rochester',

        'Gaetz',

        'Dunn',

        'Rutherford',

        'Soto',

        'Mast',

        'Ferguson',

        'Krishnamoorthi',

        'Banks',

        'Marshall',

        'Higgins',

        'Johnson',

        'Raskin',

        'Bergman',

        'Budd',

        'Bacon',

        'Gottheimer',

        'Rosen',

        'Espaillat',

        'Fitzpatrick',

        'Smucker',

        'González-Colón',

        'Kustoff',

        'Gonzalez',

        'Arrington',

        'Jayapal',

        'Gallagher',

        'Estes',

        'Norman',

        'Gomez',

        'Curtis',

        'Smith',

        'Hyde-Smith',

        'Lesko',

        'Cloud',

        'Balderson',

        'Hern',

        'Morelle',

        'Scanlon',

        'Wild',

        'Case',

        'Horsford',

        'Stanton',

        'Harder',

        'Porter',

        'Levin',

        'Neguse',

        'Crow',

        'Hayes',

        'Waltz',

        'Steube',

        'McBath',

        'Fulcher',

        'García',

        'Casten',

        'Underwood',

        'Baird',

        'Pence',

        'Davids',

        'Trahan',

        'Pressley',

        'Trone',

        'Slotkin',

        'Stevens',

        'Tlaib',

        'Craig',

        'Phillips',

        'Omar',

        'Stauber',

        'Guest',

        'Armstrong',

        'Pappas',

        'Van Drew',

        'Kim',

        'Sherrill',

        'Lee',

        'Ocasio-Cortez',

        'Dean',

        'Houlahan',

        'Meuser',

        'Joyce',

        'Reschenthaler',

        'Timmons',

        'Johnson',

        'Burchett',

        'Rose',

        'Green',

        'Crenshaw',

        'Gooden',

        'Fletcher',

        'Escobar',

        'Roy',

        'Garcia',

        'Allred',

        'Cline',

        'Spanberger',

        'Wexton',

        'Schrier',

        'Steil',

        'Miller',

        'Scott',

        'Braun',

        'Hawley',

        'Romney',

        'Golden',

        'Bishop',

        'Murphy',

        'Mfume',

        'Tiffany',

        'Garcia',

        'Kelly',

        'Lummis',

        'Issa',

        'Sessions',

        'Valadao',

        'Tuberville',

        'Hickenlooper',

        'Hagerty',

        'Carl',

        'Moore',

        'Obernolte',

        'Kim',

        'Steel',

        'Jacobs',

        'Boebert',

        'Cammack',

        'Franklin',

        'Donalds',

        'Gimenez',

        'Salazar',

        'Williams',

        'Clyde',

        'Greene',

        'Hinson',

        'Miller-Meeks',

        'Feenstra',

        'Miller',

        'Mrvan',

        'Spartz',

        'Mann',

        'LaTurner',

        'Auchincloss',

        'McClain',

        'Fischbach',

        'Bush',

        'Rosendale',

        'Ross',

        'Manning',

        'Leger Fernandez',

        'Garbarino',

        'Malliotakis',

        'Torres',

        'Bowman',

        'Bice',

        'Bentz',

        'Mace',

        'Harshbarger',

        'Fallon',

        'Pfluger',

        'Jackson',

        'Nehls',

        'Gonzales',

        'Van Duyne',

        'Moore',

        'Owens',

        'Good',

        'Strickland',

        'Fitzgerald',

        'Padilla',

        'Ossoff',

        'Warnock',

        'Tenney',

        'Letlow',

        'Carter',

        'Stansbury',

        'Ellzey',

        'Brown',

        'Carey',

        'Cherfilus-McCormick',

        'Flood',

        'Finstad',

        'Peltola',

        'Ryan',

        'Yakym',

        'Zinke',

        'Britt',

        'Schmitt',

        'Vance',

        'Fetterman',

        'Strong',

        'Crane',

        'Ciscomani',

        'Kiley',

        'Duarte',

        'Mullin',

        'Kamlager',

        'Garcia',

        'Pettersen',

        'Caraveo',

        'Bean',

        'Mills',

        'Frost',

        'Paulina Luna',

        'Lee',

        'Moskowitz',

        'McCormick',

        'Collins',

        'Moylan',

        'Tokuda',

        'Nunn',

        'Jackson',

        'Ramirez',

        'Budzinski',

        'Sorensen',

        'Houchin',

        'McGarvey',

        'Ivey',

        'Scholten',

        'James',

        'Thanedar',

        'Alford',

        'Burlison',

        'Ezell',

        'Davis',

        'Foushee',

        'Edwards',

        'Nickel',

        'Jackson',

        'Kean',

        'Menendez',

        'Vasquez',

        'LaLota',

        'Santos',

        "'D\'Esposito'",

        'Goldman',

        'Lawler',

        'Molinaro',

        'Williams',

        'Langworthy',

        'Landsman',

        'Miller',

        'Sykes',

        'Brecheen',

        'Hoyle',

        'Chavez-DeRemer',

        'Salinas',

        'Lee',

        'Deluzio',

        'Magaziner',

        'Fry',

        'Ogles',

        'Moran',

        'Self',

        'Luttrell',

        'De La Cruz',

        'Crockett',

        'Casar',

        'Hunt',

        'Kiggans',

        'Balint',

        'Gluesenkamp Perez',

        'Van Orden',

        'Hageman',

        'Ricketts',

        'McClellan']
    }
return keywordDict

