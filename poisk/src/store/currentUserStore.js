import axios from 'axios'
import { makeAutoObservable } from 'mobx'

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
            const response = await axios.post(
                'http://192.168.43.150:8000/api/auth/token/login/',
                loginForm,
            )
            const resp = await axios.get(
                'http://192.168.43.150:8000/api/auth/users/',
                {
                    headers: {
                        Authorization: 'Token ' + response.data.auth_token,
                    },
                },
            )
            console.log('response', response)
            console.log('resp', resp)
            localStorage.setItem('token', response.data.auth_token)
            localStorage.setItem('user_id', resp.data[0].id)
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
            const response = await axios.get(
                'http://192.168.43.150:8000/api/validate-token/',
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
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
