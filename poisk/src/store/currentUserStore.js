import { makeAutoObservable } from 'mobx'

import { checkTokenAPI, loginFormAPI, loginIDAPI } from '../components/api/api'

export const currentUser = makeAutoObservable({
    user: {},
    isAuth: false,
    loading: false,
    unsuccess: false,
    checkAuth: false,
    isLoading: true,
    logout() {
        this.isAuth = false
        localStorage.removeItem('token')
        localStorage.removeItem('user_id')
    },
    async login(login, pass) {
        console.log('start login')
        this.setLoading()
        try {
            const loginForm = {
                username: login,
                password: pass,
            }
            const response = await loginFormAPI(loginForm)
            const resp = await loginIDAPI(response.data.auth_token)
            localStorage.setItem('token', response.data.auth_token)
            localStorage.setItem('user_id', resp.data[0].id)
            console.log(resp)
            this.user = loginForm
            this.setLoading()
            this.isAuth = true
            this.checkAuth = true
        } catch (e) {
            console.log('err', e)
            this.setLoading()
            this.unsuccess = true
        }
    },

    async checkToken() {
        console.log('start check')
        this.setLoading()
        try {
            const response = await checkTokenAPI()
            console.log('check ', response)
            this.setLoading()
            this.checkAuth = true
            this.isAuth = true
            this.isLoading = false
        } catch (e) {
            console.log('checkErr', e)
            this.setLoading()
            localStorage.removeItem('token')
            localStorage.removeItem('user_id')
            this.isLoading = false
        }
    },

    setLoading() {
        this.loading = !this.loading
    },
})
