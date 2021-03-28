<template>

  <!-- <div :if="dataReady"> -->
  <!-- <div id="searchComponent" :class="{'collapsed' : !isExtendedSearchActivated}" class="flex flex-wrap"> -->
  <div class="flex flex-wrap">

    <div class="w-full md: text-center">
      <div class="flex">
        <div class="w-1/2 md:w-1/3 m-auto md:m-0">
          <router-link :to="{name:'map-search'}">
            <div
                class=" h-full group bg-myHeaderColor border border-myOrange md:border-myPageBackground  flex rounded-md cursor-pointer transition duration-500 transform translate-y-1 hover:-translate-y-1 hover:shadow-xl hover:border-myMint-300">
              <div class="m-auto">
                <div class="flex">
                  <GoogleMapsIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                  <p class="text-white pl-2 text-base p-2">Поиск по карте</p>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
      >
        <div class="px-4 py-5 flex-auto" ref='searchComponent'>


          <div class="flex flex-col-reverse flex-wrap md:flex-row">
            <div class="w-1/3 hidden md:block">


            </div>
            <div class="w-full md:w-1/3 pt-5 md:pt-0 justify-center  text-center">
              <!-- <div class="flex group cursor-pointer transition duration-500"

              > -->
              <div
                  ref="searchButton"
                  v-on:click="search"
                  class="inline-block text-white p-3 text-center items-center justify-center shadow-lg rounded-full transition duration-500 transform bg-myHeaderColor hover:text-myMint-300 cursor-pointer">
                <div>
                  <HomeSearchIcon title="Принудительный поиск"/>
                </div>
              </div>
              <!-- <div class="m-auto bg-myHeaderColor text-white p-1 -ml-2 rounded-r-lg">
                  По карте
              </div> -->
              <!-- </div> -->
            </div>
            <div class="w-full md:w-1/3">
              <p class="text-gray-500 font-bold">Ищем</p>
              <router-link :to="{name:'search-buildings'}">
                <span class="px-2 transition duration-300 cursor-pointer"
                      :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':showBuildings}">Новострои</span>
              </router-link>
              <router-link :to="{name:'search-flats'}">
                <span class="px-2 transition duration-300 cursor-pointer "
                      :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':showFlats}">Квартиры в них</span>
              </router-link>
            </div>
            <!-- <div class="w-full md:w-1/3">
                <p class="-my-4 text-sm">Попробуйте менее занудный</p>
                <router-link :to="{name:'map-search'}">
                <div  class="my-4 h-full group bg-myHeaderColor flex rounded-lg cursor-pointer transition duration-500 transform hover:translate-y-1 hover:shadow-xl">
                    <div class="m-auto">
                    <div class="flex">
                        <GoogleMapsIcon class="m-auto text-white transition duration-500 group-hover:text-myMint-300"/>
                        <p class="text-white pl-2 text-base p-2">Поиск по карте</p>
                    </div>
                    </div>
                </div>
                </router-link>
            </div> -->
          </div>


          <div class="flex flex-wrap -mx-3">
            <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
              <label
                  class="hidden text-xs md:text-sm lg:text-base md:block text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Административные районы
              </label>
              <label
                  class="block text-xs md:text-sm lg:text-base md:hidden text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Админ. районы
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                    @selectClose="search"
                    :dbValueKey="administrativeDistrictsBaseVariables.dbValueKey"
                    :fieldChoiceText="administrativeDistrictsBaseVariables.choiceText"
                    :dictKey="administrativeDistrictsBaseVariables.dictKey"
                    :apiAddress="administrativeDistrictsBaseVariables.fullApiAddress"
                    :sendParamName="administrativeDistrictsBaseVariables.sendParamName"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Выберите админ. районы"
                />
              </div>
            </div>
            <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Застройщики
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                    @selectClose="search"
                    :dbValueKey="developersBaseVariables.dbValueKey"
                    :fieldChoiceText="developersBaseVariables.choiceText"
                    :dictKey="developersBaseVariables.dictKey"
                    :apiAddress="developersBaseVariables.fullApiAddress"
                    :sendParamName="developersBaseVariables.sendParamName"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Выберите застройщиков"
                />
              </div>
            </div>
          </div>
          <div class="flex flex-wrap -mx-3">
            <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="inline-full-name">
                Районы
              </label>
              <div class="w-full">
                <div name="field" class="w-full">
                  <MultipleSelect
                      @selectClose="search"
                      @select="checkToShowMicroDistricts"
                      @remove="checkToHideMicroDistricts"
                      @removeAll="setDefaultDistrictsChoosen"
                      :dbValueKey="districtsBaseVariables.dbValueKey"
                      :extraInformationField="districtsBaseVariables.extraInformationText"
                      :fieldChoiceText="districtsBaseVariables.choiceText"
                      :dictKey="districtsBaseVariables.dictKey"
                      :sendParamName="districtsBaseVariables.sendParamName"
                      :apiAddress="districtsBaseVariables.fullApiAddress"
                      :trackEveryUpdate="true"
                      :addAction="addFindParam"
                      :removeAction="removeFindParam"
                      :removeKeyAction="removeFindParamKey"
                      placeholder="Выберите районы"
                  />
                </div>
              </div>
            </div>
            <!-- <div class=""> -->
            <div class="w-full md:w-1/2 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="inline-full-name">
                Районы
              </label>
              <div class="w-full">
                <div name="field" class="w-full">
                  <MultipleSelect
                      @selectClose="search"
                      @select="checkToShowMicroDistricts"
                      @remove="checkToHideMicroDistricts"
                      @removeAll="setDefaultDistrictsChoosen"
                      :dbValueKey="districtsBaseVariables.dbValueKey"
                      :extraInformationField="districtsBaseVariables.extraInformationText"
                      :fieldChoiceText="districtsBaseVariables.choiceText"
                      :dictKey="districtsBaseVariables.dictKey"
                      :sendParamName="districtsBaseVariables.sendParamName"
                      :apiAddress="districtsBaseVariables.fullApiAddress"
                      :trackEveryUpdate="true"
                      :addAction="addFindParam"
                      :removeAction="removeFindParam"
                      :removeKeyAction="removeFindParamKey"
                      placeholder="Выберите микрорайон"
                  />
                </div>
              </div>
            </div>
            <!-- </div> -->
          </div>
          <div class="flex flex-wrap -mx-3">
            <div class="w-full md:w-2/4 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Улицы
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                    @selectClose="search"
                    :dbValueKey="streetsBaseVariables.dbValueKey"
                    :fieldChoiceText="streetsBaseVariables.choiceText"
                    :dictKey="streetsBaseVariables.dictKey"
                    :apiAddress="streetsBaseVariables.fullApiAddress"
                    :sendParamName="streetsBaseVariables.sendParamName"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Выберите улицы"
                />
              </div>
            </div>
            <div class="w-full md:w-2/4 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Метро
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                    @selectClose="search"
                    :dbValueKey="metroBaseVariables.dbValueKey"
                    :fieldChoiceText="metroBaseVariables.choiceText"
                    :dictKey="metroBaseVariables.dictKey"
                    :apiAddress="metroBaseVariables.fullApiAddress"
                    :sendParamName="metroBaseVariables.sendParamName"
                    :extraInformationField="metroBaseVariables.extraInformationText"
                    :addAction="addFindParam"
                    :removeAction="removeFindParam"
                    :removeKeyAction="removeFindParamKey"
                    placeholder="Выберите метро"
                />
              </div>
            </div>
          </div>
          <TransitionDownRide>
            <div class="flex flex-wrap -mx-3 pt-3 md:pt-6"
                 v-if="isSaltovkaDistrictChoosen || isSevernayaSaltovkaDistrictChoosen">
              <div class='w-1/2'></div>
              <div class="w-full md:w-1/2 grid grid-cols-2">
                <TransitionDownRide>
                  <div class="w-full text-sm lg:text-base px-3 mb-3 md:mb-0 " v-if="isSaltovkaDistrictChoosen">
                    <label
                        class="block text-xs md:text-sm lg:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4"
                        for="grid-last-name">
                      Салтовка
                    </label>
                    <div name="field" class="w-full">
                      <MultipleSelect
                          @selectClose="search"
                          :dbValueKey="saltovkaMicroDistrictsBaseVariables.dbValueKey"
                          :fieldChoiceText="saltovkaMicroDistrictsBaseVariables.choiceText"
                          :dictKey="saltovkaMicroDistrictsBaseVariables.dictKey"
                          :apiAddress="saltovkaMicroDistrictsBaseVariables.fullApiAddress"
                          :sendParamName="saltovkaMicroDistrictsBaseVariables.sendParamName"
                          :addAction="addFindParam"
                          :removeAction="removeFindParam"
                          :removeKeyAction="removeFindParamKey"
                          placeholder="Выберите микрорайоны"
                      />
                    </div>
                  </div>
                </TransitionDownRide>
                <TransitionDownRide>
                  <div class="w-full px-3 pt-3 md:pt-6" v-if="isSevernayaSaltovkaDistrictChoosen">
                    <label
                        class="hidden text-xs md:text-sm lg:text-base md:block text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4"
                        for="grid-last-name">
                      Северная Салтовка.
                    </label>
                    <label
                        class="block text-xs md:text-sm lg:text-base md:hidden text-sm md:text-base text-gray-500 md:font-bold md:text-left mb-1 md:mb-0 pr-4"
                        for="grid-last-name">
                      Северная Салт.
                    </label>
                    <div class="w-full">
                      <MultipleSelect
                          @selectClose="search"
                          :dbValueKey="severnayaSaltovkaMicroDistrictsBaseVariables.dbValueKey"
                          :fieldChoiceText="severnayaSaltovkaMicroDistrictsBaseVariables.choiceText"
                          :dictKey="severnayaSaltovkaMicroDistrictsBaseVariables.dictKey"
                          :apiAddress="severnayaSaltovkaMicroDistrictsBaseVariables.fullApiAddress"
                          :sendParamName="severnayaSaltovkaMicroDistrictsBaseVariables.sendParamName"
                          :addAction="addFindParam"
                          :removeAction="removeFindParam"
                          :removeKeyAction="removeFindParamKey"
                          placeholder="Микрорайоны"
                      />
                    </div>
                  </div>
                </TransitionDownRide>
              </div>
            </div>
          </TransitionDownRide>
          <div class="flex flex-wrap -mx-3 ">
            <!-- <div class="w-full md:w-2/4 px-3 pt-3 md:pt-6">
              <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                Улицы
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                @selectClose="search"
                :dbValueKey="streetsBaseVariables.dbValueKey"
                :fieldChoiceText="streetsBaseVariables.choiceText"
                :dictKey="streetsBaseVariables.dictKey"
                :apiAddress="streetsBaseVariables.fullApiAddress"
                :sendParamName="streetsBaseVariables.sendParamName"
                :addAction="addFindParam"
                :removeAction="removeFindParam"
                :removeKeyAction="removeFindParamKey"
                placeholder="Выберите улицы"
                />
              </div>
            </div> -->
            <!-- <div class="w-full md:w-1/4 px-3 pt-3 md:pt-6">
             <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
               Класс
             </label>
             <div name="field" class="w-full">
                 <MultipleSelect
                 @selectClose="search"
                 :dbValueKey="theClassBaseVariables.dbValueKey"
                 :fieldChoiceText="theClassBaseVariables.choiceText"
                 :dictKey="theClassBaseVariables.dictKey"
                 :apiAddress="theClassBaseVariables.fullApiAddress"
                 :sendParamName="theClassBaseVariables.sendParamName"
                 :addAction="addFindParam"
                 :removeAction="removeFindParam"
                 :removeKeyAction="removeFindParamKey"
                 placeholder="Эконом, комфорт..."
                 />
               </div>
           </div> -->
          </div>
          <div class="flex flex-wrap -mx-3 ">
            <!-- <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
              <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                Метро
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                @selectClose="search"
                :dbValueKey="metroBaseVariables.dbValueKey"
                :fieldChoiceText="metroBaseVariables.choiceText"
                :dictKey="metroBaseVariables.dictKey"
                :apiAddress="metroBaseVariables.fullApiAddress"
                :sendParamName="metroBaseVariables.sendParamName"
                :extraInformationField="metroBaseVariables.extraInformationText"
                :addAction="addFindParam"
                :removeAction="removeFindParam"
                :removeKeyAction="removeFindParamKey"
                placeholder="Выберите метро"
                />
              </div>
            </div> -->
            <!-- <div class="w-full md:w-2/6 lg:1/5 px-3 pt-3 md:pt-6">
              <label class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                Время от метро
              </label>
              <div class="w-full">
                <div class="grid grid-cols-8 justify-center items-center">
                  <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    До
                  </div>
                  <div class="col-span-5">
                    <vInputSearch
                      @valueChanged="search"
                      :addAction="addFindParam"
                      :removeAction="removeFindParam"
                      :sendParamName="timeFromMetroBaseVariables.sendParamName"
                      :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                  <div class="text-xs md:text-sm lg:text-base col-span-2">
                    мин.
                  </div>
                </div>
              </div>
            </div> -->
            <!-- <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
              <label class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4" for="grid-last-name">
                Застройщики
              </label>
              <div name="field" class="w-full">
                <MultipleSelect
                  @selectClose="search"
                  :dbValueKey="developersBaseVariables.dbValueKey"
                  :fieldChoiceText="developersBaseVariables.choiceText"
                  :dictKey="developersBaseVariables.dictKey"
                  :apiAddress="developersBaseVariables.fullApiAddress"
                  :sendParamName="developersBaseVariables.sendParamName"
                  :addAction="addFindParam"
                  :removeAction="removeFindParam"
                  :removeKeyAction="removeFindParamKey"
                  placeholder="Выберите застройщиков"
                />
              </div>
            </div> -->
          </div>


          <div class="flex flex-wrap -mx-3" v-if="showFlats">
            <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Кол-во комнат
              </label>
              <div class="w-4/5 md:w-full m-auto">
                <div class="grid grid-cols-5 md:grid-cols-6 justify-center items-center">
                  <!-- <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    от
                  </div> -->
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="roomsBaseVariables.sendParamNameFrom"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                  <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    -
                  </div>
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="roomsBaseVariables.sendParamNameTo"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full md:w-2/6 lg:1/5 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Этаж
              </label>
              <div class="w-4/5 md:w-full m-auto">
                <div class="grid grid-cols-5 md:grid-cols-6 justify-center items-center">
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="floorBaseVariables.sendParamNameFrom"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                  <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    -
                  </div>
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="floorBaseVariables.sendParamNameTo"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full md:w-2/6 lg:2/5 px-3 pt-3 md:pt-6">
              <label
                  class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                  for="grid-last-name">
                Цена ($)
              </label>
              <div class="w-4/5 md:w-full m-auto">
                <div class="grid grid-cols-5 md:grid-cols-6 justify-center items-center">
                  <!-- <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    от
                  </div> -->
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="priceBaseVariables.sendParamNameFrom"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                  <div class="col-span-1 text-xs md:text-sm lg:text-base">
                    -
                  </div>
                  <div class="col-span-2">
                    <vInputSearch
                        @valueChanged="search"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="priceBaseVariables.sendParamNameTo"
                        :removeKeyAction="removeFindParamKey"
                    />
                  </div>
                </div>
              </div>

            </div>
          </div>


          <div class="flex w-full">
            <div class="m-auto w-3/5 pt-6 border-b-2 border-myHeaderColor opacity-25"></div>
          </div>
          <div class="flex pt-3 pb-4">
            <div class="w-1/2" v-if="showBuildings">
              <div class="text-gray-500 font-bold" :class="{'text-myMint-300' : sallableOnlyActivated.value}">
                <span class="text-sm">Только с квартирами в продаже</span>

              </div>
              <div>
                <toggle-button @change="updateSallableOnly" :sync="true" v-model="sallableOnlyActivated.value"
                               color="#00A480"/>
              </div>
            </div>

            <div class="w-1/2 justify-center" :class="{'w-full':showFlats}">
              <div class="text-gray-500 font-bold" :class="{'text-myMint-300' : isExtendedSearchActivated}">
                <span class="text-sm">Расширенный поиск</span>
              </div>
              <div>
                <toggle-button :sync="true" v-model="isExtendedSearchActivated" color="#00A480"/>
              </div>
            </div>

            <!-- <div class="w-1/3">
                <p class="text-gray-500 font-bold">Что ищем?</p>
                <div class=''>
                  <router-link :to="{name:'search-buildings'}">
                    <span class="px-2 transition duration-300 cursor-pointer" :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':showBuildings}">Новострои</span>
                  </router-link>
                  <router-link :to="{name:'search-flats'}">
                    <span class="px-2 transition duration-300 cursor-pointer " :class="{'border-b-2 border-myMint-400 font-bold text-myMint-400':showFlats}">Квартиры в них</span>
                  </router-link>
                </div>
            </div> -->
          </div>
          <div>
            <!-- <ExtendedSearchTransition> -->
            <div v-show="isExtendedSearchActivated" class="pt-3 md:pt-6">
              <div class="flex flex-wrap -mx-3 mb-3 md:mb-6">
                <div class="w-full md:w-1/4 px-3">
                  <label
                      class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Номера домов
                  </label>
                  <div class="w-full">
                    <MultipleTaggingSelect
                        @tagsChange="search"
                        @activateExtendedSearch="isExtendedSearchActivated=true"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :sendParamName="houseNumberSendParamName"
                        :removeKeyAction="removeFindParamKey"
                        :isForExtendedSearch="true"
                        tagPlaceHolder="enter чтобы добавить к поиску"
                        placeholder="№"
                    />
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Класс
                  </label>
                  <div name="field" class="w-full">
                    <MultipleSelect
                        @selectClose="search"
                        @activateExtendedSearch="isExtendedSearchActivated=true"
                        :dbValueKey="theClassBaseVariables.dbValueKey"
                        :fieldChoiceText="theClassBaseVariables.choiceText"
                        :dictKey="theClassBaseVariables.dictKey"
                        :apiAddress="theClassBaseVariables.fullApiAddress"
                        :sendParamName="theClassBaseVariables.sendParamName"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :removeKeyAction="removeFindParamKey"
                        :isForExtendedSearch="true"
                        placeholder="Выберите класс"
                    />
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Этажность
                  </label>
                  <div class="w-4/5 md:w-full m-auto">
                    <div class="flex  justify-center items-center">
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="numberOfStoreysBaseVariables.sendParamNameFrom"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                      <div class="px-2 text-xs md:text-sm lg:text-base">
                        -
                      </div>
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="numberOfStoreysBaseVariables.sendParamNameTo"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Высота потолка
                  </label>
                  <div class="w-4/5 md:w-full m-auto">
                    <div class="flex  justify-center items-center">
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="roomHeightBaseVariables.sendParamNameFrom"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                      <div class="px-2 text-xs md:text-sm lg:text-base">
                        -
                      </div>
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="roomHeightBaseVariables.sendParamNameTo"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex flex-wrap -mx-3 mb-3 md:mb-6">
                <div class="w-full md:w-1/4 px-3">
                  <label
                      class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Стены
                  </label>
                  <div class="w-full">
                    <MultipleSelect
                        @selectClose="search"
                        @activateExtendedSearch="isExtendedSearchActivated=true"
                        :dbValueKey="wallsTypeBaseVariables.dbValueKey"
                        :fieldChoiceText="wallsTypeBaseVariables.choiceText"
                        :dictKey="wallsTypeBaseVariables.dictKey"
                        :apiAddress="wallsTypeBaseVariables.fullApiAddress"
                        :sendParamName="wallsTypeBaseVariables.sendParamName"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :removeKeyAction="removeFindParamKey"
                        :isForExtendedSearch="true"
                        placeholder="Выберите стены"
                    />
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Утепление стен
                  </label>
                  <div name="field" class="w-full">
                    <MultipleSelect
                        @selectClose="search"
                        @activateExtendedSearch="isExtendedSearchActivated=true"
                        :dbValueKey="warmingBaseVariables.dbValueKey"
                        :fieldChoiceText="warmingBaseVariables.choiceText"
                        :dictKey="warmingBaseVariables.dictKey"
                        :apiAddress="warmingBaseVariables.fullApiAddress"
                        :sendParamName="warmingBaseVariables.sendParamName"
                        :addAction="addFindParam"
                        :removeAction="removeFindParam"
                        :removeKeyAction="removeFindParamKey"
                        :isForExtendedSearch="true"
                        placeholder="Выберите утепление"
                    />
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base text-gray-500 font-bold md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Отопление
                  </label>
                  <div name="field" class="w-full">
                    <div class="">
                      <MultipleSelect
                          @selectClose="search"
                          @activateExtendedSearch="isExtendedSearchActivated=true"
                          :dbValueKey="heatingBaseVariables.dbValueKey"
                          :fieldChoiceText="heatingBaseVariables.choiceText"
                          :dictKey="heatingBaseVariables.dictKey"
                          :apiAddress="heatingBaseVariables.fullApiAddress"
                          :sendParamName="heatingBaseVariables.sendParamName"
                          :addAction="addFindParam"
                          :removeAction="removeFindParam"
                          :removeKeyAction="removeFindParamKey"
                          :isForExtendedSearch="true"
                          placeholder="Выберите отопление"
                      />
                    </div>
                  </div>
                </div>
                <div class="w-full md:w-1/4 px-3  border-l rounded">
                  <label
                      class="block text-xs md:text-sm lg:text-base  font-bold text-gray-500  md:text-left mb-1 md:mb-0 pr-4"
                      for="grid-last-name">
                    Высота потолка
                  </label>
                  <div class="w-4/5 md:w-full m-auto">
                    <div class="flex  justify-center items-center">
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="roomHeightBaseVariables.sendParamNameFrom"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                      <div class="px-2 text-xs md:text-sm lg:text-base">
                        -
                      </div>
                      <div class="">
                        <vInputSearch
                            @valueChanged="search"
                            @activateExtendedSearch="isExtendedSearchActivated=true"
                            :addAction="addFindParam"
                            :removeAction="removeFindParam"
                            :sendParamName="roomHeightBaseVariables.sendParamNameTo"
                            :removeKeyAction="removeFindParamKey"
                            :isForExtendedSearch="true"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </div>
            <!-- </ExtendedSearchTransition> -->
          </div>
        </div>
        <!-- <button v-on:click="search" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
          п о и с к
        </button> -->
      </div>
    </div>
  </div>
  <!-- </div> -->
</template>

<script>
import MultipleSelect from './v-multiple-select';
import MultipleTaggingSelect from './v-multiple-tagging-select';
import {
  saltovkaDBKey,
  severnayaSaltovkaDBKey,
  houseNumberSendParamName,
  streetsBaseVariables,
  districtsBaseVariables,
  administrativeDistrictsBaseVariables,
  saltovkaMicroDistrictsBaseVariables,
  severnayaSaltovkaMicroDistrictsBaseVariables,
  developersBaseVariables,
  metroBaseVariables,
  theClassBaseVariables,
  timeFromMetroBaseVariables,
  floorBaseVariables,
  roomsBaseVariables,
  priceBaseVariables,
  numberOfStoreysBaseVariables,
  roomHeightBaseVariables,
  wallsTypeBaseVariables,
  heatingBaseVariables,
  warmingBaseVariables
} from '../variables.js';
import {mapMutations, mapActions, mapGetters} from 'vuex'
import HomeSearchIcon from 'vue-material-design-icons/HomeSearch';
import GoogleMapsIcon from 'vue-material-design-icons/GoogleMaps';
import {addHashToLocation} from '../utils.js'
import TransitionDownRide from '../transitions/downRide'
import {ToggleButton} from 'vue-js-toggle-button'
// import ExtendedSearchTransition from '../transitions/extendedSearch'
// import searchComponentTransition from '../transitions/searchComponent'\
import smoothHeight from 'vue-smooth-height';
import vInputSearch from './v-input-search' ;

export default {
  components: {
    MultipleSelect,
    MultipleTaggingSelect,
    HomeSearchIcon,
    TransitionDownRide,
    ToggleButton,
    vInputSearch,
    GoogleMapsIcon,

    // ExtendedSearchTransition,
    // searchComponentTransition
  },
  // В data только импортированные константные переменные
  data() {
    return {
      saltovkaDBKey: saltovkaDBKey,
      severnayaSaltovkaDBKey: severnayaSaltovkaDBKey,
      houseNumberSendParamName: houseNumberSendParamName,
      streetsBaseVariables: streetsBaseVariables,
      districtsBaseVariables: districtsBaseVariables,
      administrativeDistrictsBaseVariables: administrativeDistrictsBaseVariables,
      saltovkaMicroDistrictsBaseVariables: saltovkaMicroDistrictsBaseVariables,
      severnayaSaltovkaMicroDistrictsBaseVariables: severnayaSaltovkaMicroDistrictsBaseVariables,
      developersBaseVariables: developersBaseVariables,
      metroBaseVariables: metroBaseVariables,
      theClassBaseVariables: theClassBaseVariables,
      timeFromMetroBaseVariables: timeFromMetroBaseVariables,
      floorBaseVariables: floorBaseVariables,
      roomsBaseVariables: roomsBaseVariables,
      priceBaseVariables: priceBaseVariables,
      numberOfStoreysBaseVariables: numberOfStoreysBaseVariables,
      roomHeightBaseVariables: roomHeightBaseVariables,
      wallsTypeBaseVariables: wallsTypeBaseVariables,
      heatingBaseVariables: heatingBaseVariables,
      warmingBaseVariables: warmingBaseVariables,
      dataReady: false,
      isExtendedSearchActivated: false,

      sallableOnlyActivated: {
        'key': 'sallable_only',
        'value': false
      },
    }
  },
  // computed: {
  //     allBuildings(){
  //         console.log(this.$store.getters.allBuildings)
  //         return this.$store.getters.allBuildings;
  //     }
  // },
  // computed: {
  //     ...mapGetters(['allBuildings','buildingsCount'])
  //     },
  watch: {
    $route: "updateBuildings",

    // (value){
    // alert()
    // if(value){
    //   this.addFindParam({'key':this.sallableOnlyActivated.key,'value':this.sallableOnlyActivated.value})
    // }
    // else{
    //   this.removeFindParamKey(this.sallableOnlyActivated.key)
    // }
    // this.search()
    // }
  },
  // beforeRouteUpdate(){
  //   this.updateBuildings()
  // },
  // created () {
  //    this.setInitialData()
  //  },
  methods: {
    ...mapMutations([
      // 'removeStreet',
      // 'addStreet'
      'addFindParam',
      'removeFindParam',
      'updateFindParams',
      'removeFindParamKey',
      'updateShowFlatsOnly',
      // 'updateSaleOnlyActivated',
    ]),
    ...mapActions([
      'searchBuildings',
      'checkToShowMicroDistricts',
      'checkToHideMicroDistricts',
      'setDefaultDistrictsChoosen',
      'searchFlats'
      // 'addStreet',
      // 'removeStreet',
    ]),
    search() {
      // alert('se')
      // alert(this.activeFindParams)
      // console.log('\tSEARCH')
      // alert(findParams)
      // const qs = require('qs')
      // this.searchBuildings(findParams)
      // console.log('ACTIVE FIND PARAMS BEFORE ROUTER REPLACE')
      // console.log(this.activeFindParams)

      // const template = {distict:["2",1]}
      // this.$store.dispatch('updateFindParams')
      // .then(() =>
      // this.$router.replace({name: 'search-page', query:this.activeFindParams})
      if (this.$route.path == '/') {
        this.removeFindParamKey('page')
        this.$router.replace({name: 'search-buildings', query: this.activeFindParams})
      } else {
        // this.addHashToLocation(this.activeFindParams)
        this.removeFindParamKey('page')
        this.callAddHashToLocation()
        this.updateBuildings()
      }
      // this.$router.replace({name:'search-page', query:})
      // this.$router.replace({name: 'search-page', query:template})
    },
    visualSearchButtonTrigger() {
      // this.$refs.searchButton.classList.add("rotate-90");
      this.$refs.searchButton.classList.add("translate-y-1");
      this.$refs.searchButton.classList.add("text-myMint-300");
      setTimeout(() => {
        // this.$refs.searchButton.classList.remove("rotate-90");
        this.$refs.searchButton.classList.remove("translate-y-1");
        this.$refs.searchButton.classList.remove("text-myMint-300");
      }, 400);
    },
    updateBuildings() {
      // if('page' in this.activeFindParams){
      //   alert()
      //   this.removeFindParamKey('page')
      // }
      if (this.showFlats) {
        this.searchFlats(this.activeFindParams)
      } else if (this.searchBuildings) {
        this.searchBuildings(this.activeFindParams)
      }
      this.visualSearchButtonTrigger()
    },
    callAddHashToLocation() {
      addHashToLocation(this.activeFindParams, this.$route.path)
    },
    updateSallableOnly(newValueDict) {
      console.log('\tNEW VALUE: ', newValueDict)
      if (newValueDict.value) {
        this.addFindParam({'key': this.sallableOnlyActivated.key, 'value': true})
      } else {
        this.removeFindParamKey(this.sallableOnlyActivated.key)
      }
      this.search()
    },
    // updateExtendedSearch(newValueDict){
    //     // console.log('\tNEW VALUE: ', newValueDict)
    //     if(newValueDict.value){
    //       this.addFindParam({'key':extendedSearchActivatedBaseVariables.sendParamName,'value': true})
    //     }
    //     else{
    //       this.removeFindParamKey(extendedSearchActivatedBaseVariables.sendParamName)
    //     }
    //     this.callAddHashToLocation()
    // },
    setInitialData() {
      if (this.sallableOnlyActivated.key in this.activeFindParams) {
        this.sallableOnlyActivated.value = true
      }
      // if(extendedSearchActivatedBaseVariables.sendParamName in this.activeFindParams){
      //   this.isExtendedSearchActivated = true
      // }
      this.callAddHashToLocation()
    },
    async prepareData() {
      // await this.updateBuildings()
    }
  },
  computed: {
    ...mapGetters([
      'activeFindParams',
      'isSaltovkaDistrictChoosen',
      'isSevernayaSaltovkaDistrictChoosen',

      'selectedStreets',
      'selectedDistricts',
      'selectedAdministrativeDistricts',
      'selectedHouseNumbers',
      'selectedDevelopers',
      'selectedSaltovkaMicroDistricts',
      'selectedSevernayaSaltovkaMicroDistricts',
      'showFlatsOnly',
      // 'isSaleOnlyActivated',
    ]),
    showFlats: function () {
      if (this.$route.name == 'search-flats') {
        return true
      }
      return false
    },
    showBuildings: function () {
      if (this.$route.name == 'search-buildings' || this.$route.name == 'home') {
        return true
      }
      return false
    }
  },
  mounted() {

    this.$smoothElement({
      el: this.$refs.searchComponent,
      hideOverflow: true
    })
    this.setInitialData()
  },
  mixins: [
    smoothHeight
  ],

}

</script>


<style scoped>

</style>
