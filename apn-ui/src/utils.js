export function addHashToLocation(paramsDict, currentPath) {
    // console.log('aaaaaaaaaaaaaaaaa')
    // console.log(currentPath)
    const qs = require('qs');
    const q = qs.stringify(paramsDict, {arrayFormat: 'repeat'})
    if(q.length > 0){
      history.replaceState(
        {},
        null,
        '#' + currentPath + '?' + q
        )
    }
    else{
      history.pushState(
        {},
        null,
        '#' + currentPath,
        )
    }
  }

export function stringToInt(n) {
    let num = parseInt(n)
    if(isNaN(num)){
        return -1
    }
    return num
}