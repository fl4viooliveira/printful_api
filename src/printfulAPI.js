
// s_key = 'xk7ov0my-t9vm-70z6:y491-2uyygexkkq6r' 
// key = base64.b64encode(bytes(s_key, 'utf-8'))
// keyDecoded = key.decode('ascii')
// header = {'Authorization': 'Basic ' + keyDecoded}

let secretKey = 'xk7ov0my-t9vm-70z6:y491-2uyygexkkq6r';
let key = atob(bytes(secretKey, 'utf-8'));
let keyDecoded = key.btoa('ascii');
let header = {'Authorization': 'Basic' + keyDecoded};



const apiURL = `https://api.printful.com/sync/products${header}`

export const getData = async () => {
  try {
    const response = await fetch(apiURL);
    if (response.ok) {
      const jsonResponse = await response.json();
      console.log(jsonResponse)
    }
    throw new Error(`Request Failed`);
  } catch(error) {
    console.log(`Oops! ${error}!`)
  };
}
