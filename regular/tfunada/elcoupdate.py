import elasticsearch

temp_data = [
    {
        "tweet": {
            "country": "us",
            "freq": "1,246,357",
            "location": {
                "lat": "38.0000",
                "lon": "-97.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "br",
            "freq": "236,836",
            "location": {
                "lat": "-10.0000",
                "lon": "-55.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gb",
            "freq": "204,255",
            "location": {
                "lat": "54.0000",
                "lon": "-2.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tr",
            "freq": "72,852",
            "location": {
                "lat": "39.0000",
                "lon": "35.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ph",
            "freq": "71,205",
            "location": {
                "lat": "13.0000",
                "lon": "122.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "jp",
            "freq": "58,667",
            "location": {
                "lat": "36.0000",
                "lon": "138.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "es",
            "freq": "58,653",
            "location": {
                "lat": "40.0000",
                "lon": "-4.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ca",
            "freq": "53,290",
            "location": {
                "lat": "60.0000",
                "lon": "-95.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ar",
            "freq": "48,426",
            "location": {
                "lat": "-34.0000",
                "lon": "-64.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "in",
            "freq": "46,030",
            "location": {
                "lat": "20.0000",
                "lon": "77.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mx",
            "freq": "41,446",
            "location": {
                "lat": "23.0000",
                "lon": "-102.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "za",
            "freq": "39,554",
            "location": {
                "lat": "-29.0000",
                "lon": "24.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "my",
            "freq": "38,527",
            "location": {
                "lat": "2.5000",
                "lon": "112.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "fr",
            "freq": "32,192",
            "location": {
                "lat": "46.0000",
                "lon": "2.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "au",
            "freq": "29,807",
            "location": {
                "lat": "-27.0000",
                "lon": "133.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ng",
            "freq": "22,791",
            "location": {
                "lat": "10.0000",
                "lon": "8.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "it",
            "freq": "20,869",
            "location": {
                "lat": "42.8333",
                "lon": "12.8333"
            }
        }
    },
    {
        "tweet": {
            "country": "id",
            "freq": "19,530",
            "location": {
                "lat": "-5.0000",
                "lon": "120.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "co",
            "freq": "17,561",
            "location": {
                "lat": "4.0000",
                "lon": "-72.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "de",
            "freq": "17,259",
            "location": {
                "lat": "51.0000",
                "lon": "9.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ie",
            "freq": "14,526",
            "location": {
                "lat": "53.0000",
                "lon": "-8.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "pt",
            "freq": "12,889",
            "location": {
                "lat": "39.5000",
                "lon": "-8.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cl",
            "freq": "12,787",
            "location": {
                "lat": "-30.0000",
                "lon": "-71.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "th",
            "freq": "12,548",
            "location": {
                "lat": "15.0000",
                "lon": "100.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "nl",
            "freq": "12,085",
            "location": {
                "lat": "52.5000",
                "lon": "5.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "ve",
            "freq": "9,588",
            "location": {
                "lat": "8.0000",
                "lon": "-66.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "kw",
            "freq": "7,520",
            "location": {
                "lat": "29.3375",
                "lon": "47.6581"
            }
        }
    },
    {
        "tweet": {
            "country": "sg",
            "freq": "7,215",
            "location": {
                "lat": "1.3667",
                "lon": "103.8000"
            }
        }
    },
    {
        "tweet": {
            "country": "pl",
            "freq": "6,996",
            "location": {
                "lat": "52.0000",
                "lon": "20.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ae",
            "freq": "6,858",
            "location": {
                "lat": "24.0000",
                "lon": "54.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ke",
            "freq": "6,510",
            "location": {
                "lat": "1.0000",
                "lon": "38.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "uy",
            "freq": "6,277",
            "location": {
                "lat": "-33.0000",
                "lon": "-56.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "pk",
            "freq": "5,664",
            "location": {
                "lat": "30.0000",
                "lon": "70.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "be",
            "freq": "5,542",
            "location": {
                "lat": "50.8333",
                "lon": "4.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "se",
            "freq": "5,385",
            "location": {
                "lat": "62.0000",
                "lon": "15.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sa",
            "freq": "5,347",
            "location": {
                "lat": "25.0000",
                "lon": "45.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gh",
            "freq": "5,330",
            "location": {
                "lat": "8.0000",
                "lon": "-2.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "nz",
            "freq": "5,207",
            "location": {
                "lat": "-41.0000",
                "lon": "174.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "pe",
            "freq": "4,884",
            "location": {
                "lat": "-10.0000",
                "lon": "-76.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ru",
            "freq": "4,313",
            "location": {
                "lat": "60.0000",
                "lon": "100.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ec",
            "freq": "3,989",
            "location": {
                "lat": "-2.0000",
                "lon": "-77.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "py",
            "freq": "3,786",
            "location": {
                "lat": "-23.0000",
                "lon": "-58.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cr",
            "freq": "3,776",
            "location": {
                "lat": "10.0000",
                "lon": "-84.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "kr",
            "freq": "3,065",
            "location": {
                "lat": "37.0000",
                "lon": "127.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "cn",
            "freq": "2,899",
            "location": {
                "lat": "35.0000",
                "lon": "105.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "do",
            "freq": "2,857",
            "location": {
                "lat": "19.0000",
                "lon": "-70.6667"
            }
        }
    },
    {
        "tweet": {
            "country": "eg",
            "freq": "2,846",
            "location": {
                "lat": "27.0000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ch",
            "freq": "2,740",
            "location": {
                "lat": "47.0000",
                "lon": "8.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "no",
            "freq": "2,541",
            "location": {
                "lat": "62.0000",
                "lon": "10.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "fi",
            "freq": "2,422",
            "location": {
                "lat": "64.0000",
                "lon": "26.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "dk",
            "freq": "2,408",
            "location": {
                "lat": "56.0000",
                "lon": "10.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gr",
            "freq": "2,280",
            "location": {
                "lat": "39.0000",
                "lon": "22.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cz",
            "freq": "2,199",
            "location": {
                "lat": "49.7500",
                "lon": "15.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "jm",
            "freq": "2,087",
            "location": {
                "lat": "18.2500",
                "lon": "-77.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "hk",
            "freq": "2,012",
            "location": {
                "lat": "22.2500",
                "lon": "114.1667"
            }
        }
    },
    {
        "tweet": {
            "country": "at",
            "freq": "1,958",
            "location": {
                "lat": "47.3333",
                "lon": "13.3333"
            }
        }
    },
    {
        "tweet": {
            "country": "pa",
            "freq": "1,884",
            "location": {
                "lat": "9.0000",
                "lon": "-80.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "rs",
            "freq": "1,756",
            "location": {
                "lat": "44.0000",
                "lon": "21.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gt",
            "freq": "1,679",
            "location": {
                "lat": "15.5000",
                "lon": "-90.2500"
            }
        }
    },
    {
        "tweet": {
            "country": "ug",
            "freq": "1,647",
            "location": {
                "lat": "1.0000",
                "lon": "32.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "vn",
            "freq": "1,483",
            "location": {
                "lat": "16.0000",
                "lon": "106.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "il",
            "freq": "1,482",
            "location": {
                "lat": "31.5000",
                "lon": "34.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "tt",
            "freq": "1,403",
            "location": {
                "lat": "11.0000",
                "lon": "-61.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "hu",
            "freq": "1,329",
            "location": {
                "lat": "47.0000",
                "lon": "20.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ni",
            "freq": "1,323",
            "location": {
                "lat": "13.0000",
                "lon": "-85.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tw",
            "freq": "1,285",
            "location": {
                "lat": "23.5000",
                "lon": "121.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bd",
            "freq": "1,273",
            "location": {
                "lat": "24.0000",
                "lon": "90.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "qa",
            "freq": "1,272",
            "location": {
                "lat": "25.5000",
                "lon": "51.2500"
            }
        }
    },
    {
        "tweet": {
            "country": "zw",
            "freq": "1,165",
            "location": {
                "lat": "-20.0000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bw",
            "freq": "1,096",
            "location": {
                "lat": "-22.0000",
                "lon": "24.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ua",
            "freq": "1,093",
            "location": {
                "lat": "49.0000",
                "lon": "32.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "lb",
            "freq": "1,088",
            "location": {
                "lat": "33.8333",
                "lon": "35.8333"
            }
        }
    },
    {
        "tweet": {
            "country": "cy",
            "freq": "1,035",
            "location": {
                "lat": "35.0000",
                "lon": "33.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ro",
            "freq": "1,011",
            "location": {
                "lat": "46.0000",
                "lon": "25.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "lk",
            "freq": "1,009",
            "location": {
                "lat": "7.0000",
                "lon": "81.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bh",
            "freq": 963,
            "location": {
                "lat": "26.0000",
                "lon": "50.5500"
            }
        }
    },
    {
        "tweet": {
            "country": "bs",
            "freq": 916,
            "location": {
                "lat": "24.2500",
                "lon": "-76.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "hr",
            "freq": 900,
            "location": {
                "lat": "45.1667",
                "lon": "15.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "tz",
            "freq": 888,
            "location": {
                "lat": "-6.0000",
                "lon": "35.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "zm",
            "freq": 876,
            "location": {
                "lat": "-15.0000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "om",
            "freq": 835,
            "location": {
                "lat": "21.0000",
                "lon": "57.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bb",
            "freq": 775,
            "location": {
                "lat": "13.1667",
                "lon": "-59.5333"
            }
        }
    },
    {
        "tweet": {
            "country": "na",
            "freq": 745,
            "location": {
                "lat": "-22.0000",
                "lon": "17.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gu",
            "freq": 713,
            "location": {
                "lat": "13.4667",
                "lon": "144.7833"
            }
        }
    },
    {
        "tweet": {
            "country": "ma",
            "freq": 712,
            "location": {
                "lat": "32.0000",
                "lon": "-5.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "hn",
            "freq": 686,
            "location": {
                "lat": "15.0000",
                "lon": "-86.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "sv",
            "freq": 656,
            "location": {
                "lat": "13.8333",
                "lon": "-88.9167"
            }
        }
    },
    {
        "tweet": {
            "country": "is",
            "freq": 612,
            "location": {
                "lat": "65.0000",
                "lon": "-18.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cm",
            "freq": 583,
            "location": {
                "lat": "6.0000",
                "lon": "12.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "np",
            "freq": 576,
            "location": {
                "lat": "28.0000",
                "lon": "84.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sd",
            "freq": 540,
            "location": {
                "lat": "15.0000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bg",
            "freq": 534,
            "location": {
                "lat": "43.0000",
                "lon": "25.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "lv",
            "freq": 531,
            "location": {
                "lat": "57.0000",
                "lon": "25.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ag",
            "freq": 493,
            "location": {
                "lat": "17.0500",
                "lon": "-61.8000"
            }
        }
    },
    {
        "tweet": {
            "country": "dz",
            "freq": 484,
            "location": {
                "lat": "28.0000",
                "lon": "3.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "jo",
            "freq": 482,
            "location": {
                "lat": "31.0000",
                "lon": "36.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bo",
            "freq": 462,
            "location": {
                "lat": "-17.0000",
                "lon": "-65.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "iq",
            "freq": 445,
            "location": {
                "lat": "33.0000",
                "lon": "44.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ba",
            "freq": 429,
            "location": {
                "lat": "44.0000",
                "lon": "18.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mv",
            "freq": 428,
            "location": {
                "lat": "3.2500",
                "lon": "73.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ci",
            "freq": 419,
            "location": {
                "lat": "8.0000",
                "lon": "-5.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sn",
            "freq": 418,
            "location": {
                "lat": "14.0000",
                "lon": "-14.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "si",
            "freq": 413,
            "location": {
                "lat": "46.0000",
                "lon": "15.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bn",
            "freq": 397,
            "location": {
                "lat": "4.5000",
                "lon": "114.6667"
            }
        }
    },
    {
        "tweet": {
            "country": "by",
            "freq": 385,
            "location": {
                "lat": "53.0000",
                "lon": "28.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ir",
            "freq": 381,
            "location": {
                "lat": "32.0000",
                "lon": "53.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ht",
            "freq": 376,
            "location": {
                "lat": "19.0000",
                "lon": "-72.4167"
            }
        }
    },
    {
        "tweet": {
            "country": "az",
            "freq": 354,
            "location": {
                "lat": "40.5000",
                "lon": "47.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "tn",
            "freq": 348,
            "location": {
                "lat": "34.0000",
                "lon": "9.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sk",
            "freq": 333,
            "location": {
                "lat": "48.6667",
                "lon": "19.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "mz",
            "freq": 330,
            "location": {
                "lat": "-18.2500",
                "lon": "35.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mm",
            "freq": 326,
            "location": {
                "lat": "22.0000",
                "lon": "98.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mq",
            "freq": 323,
            "location": {
                "lat": "14.6667",
                "lon": "-61.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "lc",
            "freq": 320,
            "location": {
                "lat": "13.8833",
                "lon": "-61.1333"
            }
        }
    },
    {
        "tweet": {
            "country": "mt",
            "freq": 318,
            "location": {
                "lat": "35.8333",
                "lon": "14.5833"
            }
        }
    },
    {
        "tweet": {
            "country": "rw",
            "freq": 301,
            "location": {
                "lat": "-2.0000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mw",
            "freq": 292,
            "location": {
                "lat": "-13.5000",
                "lon": "34.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mu",
            "freq": 286,
            "location": {
                "lat": "-20.2833",
                "lon": "57.5500"
            }
        }
    },
    {
        "tweet": {
            "country": "lt",
            "freq": 273,
            "location": {
                "lat": "56.0000",
                "lon": "24.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gp",
            "freq": 270,
            "location": {
                "lat": "16.2500",
                "lon": "-61.5833"
            }
        }
    },
    {
        "tweet": {
            "country": "kh",
            "freq": 260,
            "location": {
                "lat": "13.0000",
                "lon": "105.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ao",
            "freq": 251,
            "location": {
                "lat": "-12.5000",
                "lon": "18.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "lu",
            "freq": 243,
            "location": {
                "lat": "49.7500",
                "lon": "6.1667"
            }
        }
    },
    {
        "tweet": {
            "country": "ee",
            "freq": 240,
            "location": {
                "lat": "59.0000",
                "lon": "26.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "me",
            "freq": 232,
            "location": {
                "lat": "42.0000",
                "lon": "19.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mk",
            "freq": 219,
            "location": {
                "lat": "41.8333",
                "lon": "22.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mp",
            "freq": 215,
            "location": {
                "lat": "15.2000",
                "lon": "145.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "ge",
            "freq": 205,
            "location": {
                "lat": "42.0000",
                "lon": "43.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "fj",
            "freq": 201,
            "location": {
                "lat": "-18.0000",
                "lon": "175.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cu",
            "freq": 196,
            "location": {
                "lat": "21.5000",
                "lon": "-80.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ly",
            "freq": 191,
            "location": {
                "lat": "25.0000",
                "lon": "17.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tc",
            "freq": 188,
            "location": {
                "lat": "21.7500",
                "lon": "-71.5833"
            }
        }
    },
    {
        "tweet": {
            "country": "cd",
            "freq": 175,
            "location": {
                "lat": "0.0000",
                "lon": "25.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "al",
            "freq": 167,
            "location": {
                "lat": "41.0000",
                "lon": "20.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "kz",
            "freq": 164,
            "location": {
                "lat": "48.0000",
                "lon": "68.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mo",
            "freq": 158,
            "location": {
                "lat": "22.1667",
                "lon": "113.5500"
            }
        }
    },
    {
        "tweet": {
            "country": "af",
            "freq": 154,
            "location": {
                "lat": "33.0000",
                "lon": "65.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sz",
            "freq": 154,
            "location": {
                "lat": "-26.5000",
                "lon": "31.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "pr",
            "freq": 152,
            "location": {
                "lat": "18.2500",
                "lon": "-66.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "vc",
            "freq": 151,
            "location": {
                "lat": "13.2500",
                "lon": "-61.2000"
            }
        }
    },
    {
        "tweet": {
            "country": "gi",
            "freq": 146,
            "location": {
                "lat": "36.1833",
                "lon": "-5.3667"
            }
        }
    },
    {
        "tweet": {
            "country": "so",
            "freq": 140,
            "location": {
                "lat": "10.0000",
                "lon": "49.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ky",
            "freq": 129,
            "location": {
                "lat": "19.5000",
                "lon": "-80.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "aw",
            "freq": 121,
            "location": {
                "lat": "12.5000",
                "lon": "-69.9667"
            }
        }
    },
    {
        "tweet": {
            "country": "am",
            "freq": 120,
            "location": {
                "lat": "40.0000",
                "lon": "45.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bm",
            "freq": 118,
            "location": {
                "lat": "32.3333",
                "lon": "-64.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "as",
            "freq": 112,
            "location": {
                "lat": "-14.3333",
                "lon": "-170.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "et",
            "freq": 112,
            "location": {
                "lat": "8.0000",
                "lon": "38.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "re",
            "freq": 106,
            "location": {
                "lat": "-21.1000",
                "lon": "55.6000"
            }
        }
    },
    {
        "tweet": {
            "country": "mc",
            "freq": 105,
            "location": {
                "lat": "43.7333",
                "lon": "7.4000"
            }
        }
    },
    {
        "tweet": {
            "country": "mn",
            "freq": 101,
            "location": {
                "lat": "46.0000",
                "lon": "105.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "la",
            "freq": 97,
            "location": {
                "lat": "18.0000",
                "lon": "105.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mg",
            "freq": 94,
            "location": {
                "lat": "-20.0000",
                "lon": "47.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ls",
            "freq": 87,
            "location": {
                "lat": "-29.5000",
                "lon": "28.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "aq",
            "freq": 84,
            "location": {
                "lat": "-90.0000",
                "lon": "0.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cg",
            "freq": 84,
            "location": {
                "lat": "-1.0000",
                "lon": "15.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bj",
            "freq": 83,
            "location": {
                "lat": "9.5000",
                "lon": "2.2500"
            }
        }
    },
    {
        "tweet": {
            "country": "gd",
            "freq": 81,
            "location": {
                "lat": "12.1167",
                "lon": "-61.6667"
            }
        }
    },
    {
        "tweet": {
            "country": "sy",
            "freq": 77,
            "location": {
                "lat": "35.0000",
                "lon": "38.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "uz",
            "freq": 76,
            "location": {
                "lat": "41.0000",
                "lon": "64.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gm",
            "freq": 75,
            "location": {
                "lat": "13.4667",
                "lon": "-16.5667"
            }
        }
    },
    {
        "tweet": {
            "country": "vg",
            "freq": 75,
            "location": {
                "lat": "18.5000",
                "lon": "-64.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "ad",
            "freq": 73,
            "location": {
                "lat": "42.5000",
                "lon": "1.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "ml",
            "freq": 72,
            "location": {
                "lat": "17.0000",
                "lon": "-4.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ga",
            "freq": 71,
            "location": {
                "lat": "-1.0000",
                "lon": "11.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "kn",
            "freq": 71,
            "location": {
                "lat": "17.3333",
                "lon": "-62.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "bz",
            "freq": 68,
            "location": {
                "lat": "17.2500",
                "lon": "-88.7500"
            }
        }
    },
    {
        "tweet": {
            "country": "dm",
            "freq": 62,
            "location": {
                "lat": "15.4167",
                "lon": "-61.3333"
            }
        }
    },
    {
        "tweet": {
            "country": "lr",
            "freq": 62,
            "location": {
                "lat": "6.5000",
                "lon": "-9.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "vi",
            "freq": 61,
            "location": {
                "lat": "18.3333",
                "lon": "-64.8333"
            }
        }
    },
    {
        "tweet": {
            "country": "md",
            "freq": 60,
            "location": {
                "lat": "47.0000",
                "lon": "29.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "kg",
            "freq": 59,
            "location": {
                "lat": "41.0000",
                "lon": "75.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "kp",
            "freq": 57,
            "location": {
                "lat": "40.0000",
                "lon": "127.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "va",
            "freq": 54,
            "location": {
                "lat": "41.9000",
                "lon": "12.4500"
            }
        }
    },
    {
        "tweet": {
            "country": "pg",
            "freq": 51,
            "location": {
                "lat": "-6.0000",
                "lon": "147.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sr",
            "freq": 47,
            "location": {
                "lat": "4.0000",
                "lon": "-56.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gf",
            "freq": 46,
            "location": {
                "lat": "4.0000",
                "lon": "-53.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "to",
            "freq": 46,
            "location": {
                "lat": "-20.0000",
                "lon": "-175.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ye",
            "freq": 46,
            "location": {
                "lat": "15.0000",
                "lon": "48.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gy",
            "freq": 43,
            "location": {
                "lat": "5.0000",
                "lon": "-59.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "nc",
            "freq": 42,
            "location": {
                "lat": "-21.5000",
                "lon": "165.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "gn",
            "freq": 39,
            "location": {
                "lat": "11.0000",
                "lon": "-10.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tg",
            "freq": 39,
            "location": {
                "lat": "8.0000",
                "lon": "1.1667"
            }
        }
    },
    {
        "tweet": {
            "country": "sl",
            "freq": 38,
            "location": {
                "lat": "8.5000",
                "lon": "-11.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "ws",
            "freq": 37,
            "location": {
                "lat": "-13.5833",
                "lon": "-172.3333"
            }
        }
    },
    {
        "tweet": {
            "country": "bf",
            "freq": 35,
            "location": {
                "lat": "13.0000",
                "lon": "-2.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tj",
            "freq": 34,
            "location": {
                "lat": "39.0000",
                "lon": "71.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cv",
            "freq": 33,
            "location": {
                "lat": "16.0000",
                "lon": "-24.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gl",
            "freq": 29,
            "location": {
                "lat": "72.0000",
                "lon": "-40.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ne",
            "freq": 28,
            "location": {
                "lat": "16.0000",
                "lon": "8.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "pf",
            "freq": 26,
            "location": {
                "lat": "-15.0000",
                "lon": "-140.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bt",
            "freq": 25,
            "location": {
                "lat": "27.5000",
                "lon": "90.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "sc",
            "freq": 20,
            "location": {
                "lat": "-4.5833",
                "lon": "55.6667"
            }
        }
    },
    {
        "tweet": {
            "country": "cf",
            "freq": 19,
            "location": {
                "lat": "7.0000",
                "lon": "21.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mh",
            "freq": 19,
            "location": {
                "lat": "9.0000",
                "lon": "168.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ai",
            "freq": 18,
            "location": {
                "lat": "18.2500",
                "lon": "-63.1667"
            }
        }
    },
    {
        "tweet": {
            "country": "fk",
            "freq": 18,
            "location": {
                "lat": "-51.7500",
                "lon": "-59.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "fo",
            "freq": 18,
            "location": {
                "lat": "62.0000",
                "lon": "-7.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "mr",
            "freq": 17,
            "location": {
                "lat": "20.0000",
                "lon": "-12.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "vu",
            "freq": 17,
            "location": {
                "lat": "-16.0000",
                "lon": "167.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "bi",
            "freq": 16,
            "location": {
                "lat": "-3.5000",
                "lon": "30.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "dj",
            "freq": 15,
            "location": {
                "lat": "11.5000",
                "lon": "43.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "km",
            "freq": 14,
            "location": {
                "lat": "-12.1667",
                "lon": "44.2500"
            }
        }
    },
    {
        "tweet": {
            "country": "yt",
            "freq": 14,
            "location": {
                "lat": "-12.8333",
                "lon": "45.1667"
            }
        }
    },
    {
        "tweet": {
            "country": "li",
            "freq": 13,
            "location": {
                "lat": "47.1667",
                "lon": "9.5333"
            }
        }
    },
    {
        "tweet": {
            "country": "td",
            "freq": 12,
            "location": {
                "lat": "15.0000",
                "lon": "19.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sm",
            "freq": 11,
            "location": {
                "lat": "43.7667",
                "lon": "12.4167"
            }
        }
    },
    {
        "tweet": {
            "country": "pw",
            "freq": 10,
            "location": {
                "lat": "7.5000",
                "lon": "134.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "um",
            "freq": 10,
            "location": {
                "lat": "19.2833",
                "lon": "166.6000"
            }
        }
    },
    {
        "tweet": {
            "country": "ck",
            "freq": 9,
            "location": {
                "lat": "-21.2333",
                "lon": "-159.7667"
            }
        }
    },
    {
        "tweet": {
            "country": "er",
            "freq": 9,
            "location": {
                "lat": "15.0000",
                "lon": "39.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "sb",
            "freq": 9,
            "location": {
                "lat": "-8.0000",
                "lon": "159.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "gq",
            "freq": 8,
            "location": {
                "lat": "2.0000",
                "lon": "10.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "fm",
            "freq": 7,
            "location": {
                "lat": "6.9167",
                "lon": "158.2500"
            }
        }
    },
    {
        "tweet": {
            "country": "ms",
            "freq": 7,
            "location": {
                "lat": "16.7500",
                "lon": "-62.2000"
            }
        }
    },
    {
        "tweet": {
            "country": "tm",
            "freq": 6,
            "location": {
                "lat": "40.0000",
                "lon": "60.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "cc",
            "freq": 5,
            "location": {
                "lat": "-12.5000",
                "lon": "96.8333"
            }
        }
    },
    {
        "tweet": {
            "country": "gw",
            "freq": 4,
            "location": {
                "lat": "12.0000",
                "lon": "-15.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "nu",
            "freq": 4,
            "location": {
                "lat": "-19.0333",
                "lon": "-169.8667"
            }
        }
    },
    {
        "tweet": {
            "country": "bv",
            "freq": 3,
            "location": {
                "lat": "-54.4333",
                "lon": "3.4000"
            }
        }
    },
    {
        "tweet": {
            "country": "cx",
            "freq": 3,
            "location": {
                "lat": "-10.5000",
                "lon": "105.6667"
            }
        }
    },
    {
        "tweet": {
            "country": "hm",
            "freq": 3,
            "location": {
                "lat": "-53.1000",
                "lon": "72.5167"
            }
        }
    },
    {
        "tweet": {
            "country": "io",
            "freq": 3,
            "location": {
                "lat": "-6.0000",
                "lon": "71.5000"
            }
        }
    },
    {
        "tweet": {
            "country": "nf",
            "freq": 3,
            "location": {
                "lat": "-29.0333",
                "lon": "167.9500"
            }
        }
    },
    {
        "tweet": {
            "country": "gs",
            "freq": 2,
            "location": {
                "lat": "-54.5000",
                "lon": "-37.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "ki",
            "freq": 2,
            "location": {
                "lat": "1.4167",
                "lon": "173.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "wf",
            "freq": 2,
            "location": {
                "lat": "-13.3000",
                "lon": "-176.2000"
            }
        }
    },
    {
        "tweet": {
            "country": "nr",
            "freq": 1,
            "location": {
                "lat": "-0.5333",
                "lon": "166.9167"
            }
        }
    },
    {
        "tweet": {
            "country": "pm",
            "freq": 1,
            "location": {
                "lat": "46.8333",
                "lon": "-56.3333"
            }
        }
    },
    {
        "tweet": {
            "country": "sh",
            "freq": 1,
            "location": {
                "lat": "-15.9333",
                "lon": "-5.7000"
            }
        }
    },
    {
        "tweet": {
            "country": "st",
            "freq": 1,
            "location": {
                "lat": "1.0000",
                "lon": "7.0000"
            }
        }
    },
    {
        "tweet": {
            "country": "tv",
            "freq": 1,
            "location": {
                "lat": "-8.0000",
                "lon": "178.0000"
            }
        }
    }
]

def main():
    i=0
    for data in temp_data:
        temp_dic = {}
        temp_dic = data
        #print(temp_dic)
        i = i+1
        es.index(index='heatdata', doc_type='geo', id=i, body=temp_dic)
        print(i)
    return None
if __name__=="__main__":
    main()