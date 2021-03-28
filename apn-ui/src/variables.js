export const baseBackendAddress = 'http://127.0.0.1:8000/'
export const baseApiAddress = baseBackendAddress + "api/"
export const saltovkaDBValue = 'sal'
export const severnayaSaltovkaDBValue = 'ses'

export const saltovkaDBKey = 'saltovka_db_value'
export const severnayaSaltovkaDBKey = 'severnaya_saltovka_db_value'
export const houseNumberSendParamName = 'house_number'
export const getApiTokenUrl = baseBackendAddress + 'api-token-auth/'

// export const houseNumberBaseVariables = {
//     fullApiAddress: baseApiAddress + "get-streets/" ,
//     dictKey:'streets',
//     choiceText:'street_ru',
//     dbValueKey:'id',
//     sendParamName: 'street',
// }

export const buildingsBaseVariables = {
    fullApiAddress: baseApiAddress + "buildings/"
}

export const flatsBaseVariables = {
    fullApiAddress: baseApiAddress + "flats/"
}

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

export const numberOfStoreysBaseVariables = {
    sendParamNameFrom: 'number_of_storeys_from',
    sendParamNameTo: 'number_of_storeys_to'
}
export const roomHeightBaseVariables = {
    sendParamNameFrom: 'room_height_from',
    sendParamNameTo: 'room_height_to'
}
export const wallsTypeBaseVariables = {
    sendParamName : 'walls_type'
}
export const warmingBaseVariables = {
    sendParamName : 'warming'
}
export const heatingBaseVariables = {
    sendParamName : 'heating'
}
export const parkingBaseVariables = {
    sendParamName : 'parking'
}

// For flats
export const floorBaseVariables = {
    sendParamNameFrom: 'floor_from',
    sendParamNameTo: 'floor_to'
}

export const roomsBaseVariables = {
    sendParamNameFrom: 'rooms_from',
    sendParamNameTo: 'rooms_to'
}
export const priceBaseVariables = {
    sendParamNameFrom: 'price_from',
    sendParamNameTo: 'price_to'
}
export const totalAreaBaseVariables = {
    sendParamNameFrom: 'total_area_from',
    sendParamNameTo: 'total_area_to'
}

export const livingAreaBaseVariables = {
    sendParamNameFrom: 'living_area_from',
    sendParamNameTo: 'living_area_to'
}

export const kitchenAreaBaseVariables = {
    sendParamNameFrom: 'kitchen_area_from',
    sendParamNameTo: 'kitchen_area_to'
}

// export const extendedSearchActivatedBaseVariables = {
//     sendParamName: 'extended',
// }
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