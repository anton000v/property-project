export const baseApiAddress = "http://127.0.0.1:8000/api/"
// export const baseBackendAddress = 'http://127.0.0.1:8000'
export const saltovkaDBValue = 'sal'
export const severnayaSaltovkaDBValue = 'ses'

export const saltovkaDBKey = 'saltovka_db_value'
export const severnayaSaltovkaDBKey = 'severnaya_saltovka_db_value'
export const houseNumberSendParamName = 'house_number'


// export const houseNumberBaseVariables = {
//     fullApiAddress: baseApiAddress + "get-streets/" ,
//     dictKey:'streets',
//     choiceText:'street_ru',
//     dbValueKey:'id',
//     sendParamName: 'street',
// }



export const streetsBaseVariables = {
    fullApiAddress: baseApiAddress + "get-streets/" ,
    dictKey:'streets',
    choiceText:'street_ru',
    dbValueKey:'id',
    sendParamName: 'street',
}

export const districtsBaseVariables = {
    fullApiAddress: baseApiAddress + "get-districts/",
    dictKey:'districts',
    choiceText:'text_value',
    dbValueKey:'db_value',
    sendParamName: 'district',
    // Дополнительный
    extraInformationText:'direction',
}

export const administrativeDistrictsBaseVariables = {
    fullApiAddress:baseApiAddress + "get-administrative-districts/",
    dictKey:'administrative_districts',
    choiceText:'administrative_dist_ru',
    dbValueKey:'id',
    sendParamName: 'administrative_district'
}

export const saltovkaMicroDistrictsBaseVariables = {
    fullApiAddress:baseApiAddress + 'get-saltovka-micro-districts/',
    dictKey: 'saltovka_micro_districts',
    choiceText: 'text_value',
    dbValueKey: 'db_value',
    sendParamName: 'saltovka_micro_district'
}

export const severnayaSaltovkaMicroDistrictsBaseVariables = {
    fullApiAddress:baseApiAddress + 'get-severnaya-saltovka-micro-districts/',
    dictKey: 'severnaya_saltovka_micro_districts',
    choiceText: 'text_value',
    dbValueKey: 'db_value',
    sendParamName: 'severnaya_saltovka_micro_district'
}

export const developersBaseVariables = {
    fullApiAddress:baseApiAddress + 'get-developers/',
    dictKey: 'developers',
    choiceText: 'developer_name',
    dbValueKey: 'id',
    sendParamName: 'developer'
}

export const metroBaseVariables = {
    fullApiAddress: baseApiAddress + "get-metro/",
    dictKey:'metro',
    choiceText:'text_value',
    dbValueKey:'db_value',
    sendParamName: 'metro',
    // Дополнительный
    extraInformationText:'line',
}

export const theClassBaseVariables = {
    fullApiAddress: baseApiAddress + "get-classes/",
    dictKey:'classes',
    choiceText:'text_value',
    dbValueKey:'db_value',
    sendParamName: 'the_class',
}

export const timeFromMetroBaseVariables = {
    sendParamName: 'time_from_metro',
}

// saltovkaDBKey:'saltovka_db_value',
// severnayaSaltovkaDBKey:'severnaya_saltovka_db_value',

// getStreetsApiAddress:"get-streets/" ,
// streetsDictKey:'streets',
// streetsChoiceText:'street_ru',
// streetsSearchKey:'id',

// getDistrictsApiAddress:"get-districts/",
// districtDictKey:'districts',
// districtChoiceText:'text_value',
// districtExtraInformation:'direction',
// districtsSearchKey:'db_value',

// getAdministrativeDistrictsApiAddress:"get-administrative-districts/",
// administrativeDistrictsDictKey:'administrative_districts',
// administrativeDistrictsChoiceText:'administrative_dist_ru',
// administrativeDistrictsSearchKey:'id',

// houseNumberSearchKey: 'house_number',

// microDistrictsChoiceText: 'text_value',
// microDistrictsSearchKey: 'db_value',
// getSaltovkaMicroDistrictsApiAddress: 'get-saltovka-micro-districts/',
// saltovkaMicroDistrictsDictKey: 'saltovka_micro_districts',
// getSevernayaSaltovkaMicroDistrictsApiAddress: 'get-severnaya-saltovka-micro-districts/',
// severnayaSaltovkaMicroDistrictsDictKey: 'severnaya_saltovka_micro_districts',

// getDevelopersApiAddress: 'get-developers/',
// developersDictKey: 'developers',
// developersChoiceText: 'developer_name',
// developersSearchKey: 'id',