import { makeObservable, observable, action } from 'mobx'; 

  
class TokenStore { 
  token = null; 
  
  
  constructor() { 
    makeObservable(this, { 
      token: observable, 
      setToken: action, 
      getToken: action, 
    }); 
  } 
  
  setToken(token) { 
    this.token = token; 
  } 
  
  getToken() { 
    return this.token; 
  } 
} 
  
export const tokenStore = new TokenStore();
