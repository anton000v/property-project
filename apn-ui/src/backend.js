import { getApiTokenUrl } from './variables'


export function getAuthToken(){
    console.log('Front login: ', process.env.VUE_APP_API_USERNAME);
    console.log('Front password: ', process.env.VUE_APP_API_PASS);
    let response;
    let params = JSON.stringify({
        username: process.env.VUE_APP_API_USERNAME,
        password: process.env.VUE_APP_API_PASS
    })

    var xhr = new XMLHttpRequest();
    xhr.open('POST', getApiTokenUrl, false);  // `false` makes the request synchronous
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.send(params);

    if (xhr.status === 200) {
        console.log(xhr);
      response = JSON.parse(xhr.response);
      console.log("Response: ", response);
      return response.token;
    }
}

