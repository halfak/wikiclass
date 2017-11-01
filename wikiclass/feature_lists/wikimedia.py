# The following Qids represent items in Wikidata for all Wikimedia Projects
# E.g. "English Wikipedia", "German Wiktionary", etc.
PROJECT_QIDS = {
    "Q328", "Q8447", "Q8449", "Q10000", "Q11913", "Q11918", "Q11920", "Q11921",
    "Q12237", "Q14380", "Q17985", "Q30239", "Q38288", "Q45041", "Q48183",
    "Q48952", "Q53464", "Q58172", "Q58209", "Q58215", "Q58251", "Q58255",
    "Q58679", "Q58781", "Q60786", "Q60799", "Q60819", "Q60856", "Q79633",
    "Q79636", "Q155214", "Q169514", "Q175482", "Q177837", "Q181163",
    "Q190551", "Q191168", "Q191769", "Q192582", "Q199693", "Q199698",
    "Q199700", "Q199864", "Q199913", "Q200060", "Q200180", "Q200183",
    "Q200386", "Q202472", "Q203488", "Q206855", "Q207260", "Q208533",
    "Q221444", "Q225594", "Q226150", "Q427715", "Q511754", "Q547271",
    "Q565074", "Q571001", "Q588620", "Q595628", "Q714826", "Q718394",
    "Q722040", "Q722243", "Q728945", "Q766705", "Q824297", "Q837615",
    "Q841208", "Q842341", "Q844491", "Q845993", "Q846630", "Q846871",
    "Q848046", "Q848525", "Q848974", "Q856881", "Q874555", "Q875631",
    "Q877583", "Q877685", "Q925661", "Q928808", "Q940309", "Q950058",
    "Q966609", "Q1034940", "Q1047829", "Q1047851", "Q1055841", "Q1058430",
    "Q1066461", "Q1067878", "Q1071918", "Q1110233", "Q1116066", "Q1132977",
    "Q1147071", "Q1148240", "Q1154741", "Q1154766", "Q1178461", "Q1190962",
    "Q1211233", "Q1249553", "Q1287192", "Q1291627", "Q1377618", "Q1378484",
    "Q1444686", "Q1551807", "Q1574617", "Q1585232", "Q1648786", "Q1754193",
    "Q1961887", "Q1968379", "Q1975217", "Q2029239", "Q2073394", "Q2081526",
    "Q2091593", "Q2111591", "Q2328409", "Q2349453", "Q2374285", "Q2402143",
    "Q2587255", "Q2602203", "Q2732019", "Q2742472", "Q2744155", "Q2913253",
    "Q2983979", "Q2996321", "Q2998037", "Q3025527", "Q3025736", "Q3026819",
    "Q3046353", "Q3111179", "Q3112631", "Q3123304", "Q3180091", "Q3180306",
    "Q3181422", "Q3181928", "Q3239456", "Q3311132", "Q3432470", "Q3477935",
    "Q3486726", "Q3568035", "Q3568038", "Q3568039", "Q3568040", "Q3568041",
    "Q3568042", "Q3568043", "Q3568044", "Q3568045", "Q3568046", "Q3568048",
    "Q3568049", "Q3568051", "Q3568053", "Q3568054", "Q3568056", "Q3568059",
    "Q3568060", "Q3568061", "Q3568062", "Q3568063", "Q3568065", "Q3568066",
    "Q3568069", "Q3696028", "Q3753095", "Q3756269", "Q3756562", "Q3757068",
    "Q3807895", "Q3826575", "Q3913095", "Q3913160", "Q3944107", "Q3957795",
    "Q4077512", "Q4097773", "Q4107346", "Q4115441", "Q4115463", "Q4210231",
    "Q4296423", "Q4372058", "Q4614845", "Q4783991", "Q4925786", "Q5652665",
    "Q6112922", "Q6125437", "Q6167360", "Q6587084", "Q7102897", "Q8042979",
    "Q8075204", "Q8558395", "Q8558731", "Q8558960", "Q8559119", "Q8559737",
    "Q8560590", "Q8561147", "Q8561277", "Q8561332", "Q8561415", "Q8561491",
    "Q8561552", "Q8561582", "Q8561662", "Q8561870", "Q8562097", "Q8562272",
    "Q8562481", "Q8562502", "Q8562529", "Q8562927", "Q8563136", "Q8563393",
    "Q8563536", "Q8563635", "Q8563685", "Q8563863", "Q8564352", "Q8565254",
    "Q8565447", "Q8565463", "Q8565476", "Q8565518", "Q8565742", "Q8565801",
    "Q8565913", "Q8566298", "Q8566311", "Q8566347", "Q8566503", "Q8568150",
    "Q8568791", "Q8569511", "Q8569757", "Q8569782", "Q8569951", "Q8570048",
    "Q8570353", "Q8570425", "Q8570791", "Q8571143", "Q8571427", "Q8571487",
    "Q8571809", "Q8571840", "Q8571954", "Q8572132", "Q8572199", "Q8575385",
    "Q8575467", "Q8575674", "Q8575782", "Q8575885", "Q8575930", "Q8576190",
    "Q8576237", "Q8576395", "Q8577029", "Q8582589", "Q8582909", "Q8669146",
    "Q8927872", "Q8937989", "Q12265494", "Q13230970", "Q13231253", "Q13358221",
    "Q14948450", "Q18508969", "Q20442276", "Q20726662", "Q20789766",
    "Q22013259", "Q22676953", "Q23948717", "Q26235862", "Q27102215",
    "Q28970868", "Q28971705", "Q29048035", "Q52", "Q1162302", "Q22001373",
    "Q22001374", "Q22001375", "Q22001376", "Q22001378", "Q22001379",
    "Q22116890", "Q28065753", "Q151", "Q21999841", "Q21999967", "Q22000234",
    "Q22000281", "Q22000307", "Q22000362", "Q22000399", "Q22000456",
    "Q22000473", "Q22000495", "Q22000859", "Q22000915", "Q22000929",
    "Q22000974", "Q367", "Q5725285", "Q21281261", "Q21281262", "Q21281263",
    "Q21281264", "Q21281265", "Q21281266", "Q21281267", "Q21281268",
    "Q21281269", "Q21281270", "Q21281271", "Q21281272", "Q21281273",
    "Q21281274", "Q21281275", "Q21281276", "Q21281277", "Q21281278",
    "Q21281280", "Q21281281", "Q21281283", "Q21281284", "Q21281286",
    "Q21281287", "Q21281288", "Q21281289", "Q21281290", "Q21281291",
    "Q21281293", "Q21281294", "Q24576293", "Q964", "Q15977310", "Q16735592",
    "Q22002881", "Q22002884", "Q22002898", "Q22002911", "Q22002932",
    "Q22002935", "Q22002946", "Q22002964", "Q22002978", "Q22712353",
    "Q24575986", "Q24577055", "Q369", "Q15156406", "Q15156541", "Q15156648",
    "Q15156667", "Q15281537", "Q15298974", "Q15298977", "Q15522295",
    "Q15618752", "Q15634506", "Q16515025", "Q16735590", "Q18198097",
    "Q19822573", "Q19826831", "Q20726423", "Q20726429", "Q21205461",
    "Q22004646", "Q22004659", "Q22004676", "Q22004684", "Q22004694",
    "Q22004943", "Q24577644", "Q24577645", "Q24577646", "Q24577647",
    "Q24577648", "Q24577649", "Q24577650", "Q24577651", "Q24577653",
    "Q24577655", "Q24577656", "Q24577657", "Q24577658", "Q24577659",
    "Q24577660", "Q24577661", "Q24577663", "Q24577664", "Q24577665",
    "Q24577666", "Q24577669", "Q24577671", "Q24577672", "Q24577673",
    "Q24577674", "Q24577676", "Q24577678", "Q24577680", "Q24577681",
    "Q24577682", "Q24577683", "Q24577684", "Q24577685", "Q24577686",
    "Q24577688", "Q24577690", "Q24577691", "Q24577692", "Q24577693",
    "Q24577695", "Q24577696", "Q24577697", "Q28861316", "Q263", "Q22001380",
    "Q22001381", "Q22001382", "Q22001383", "Q22001385", "Q22001387",
    "Q22808092", "Q24880555", "Q370", "Q14325227", "Q17601812", "Q19826572",
    "Q19826574", "Q19963683", "Q20671724", "Q24237997", "Q24238011",
    "Q24238014", "Q24238015", "Q24238016", "Q24238019", "Q24238020",
    "Q24238021", "Q24238022", "Q24238023", "Q24238024", "Q27910728",
    "Q373", "Q565", "Q5726840", "Q1063116", "Q13679", "Q2013", "Q483279",
    "Q465"}
