import axios from 'axios'
import { makeAutoObservable } from 'mobx'

export const currentUser = makeAutoObservable({
    user: {},
    isAuth: false,
    loading: false,
    logout() {
        this.isAuth = false
        localStorage.removeItem('token')
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
                'http://192.168.0.17:8000/auth/token/login',
                loginForm,
            )
            console.log(',response', response)
            localStorage.setItem('token', response.data.auth_token)
            this.user = loginForm
            this.setLoading()
            this.isAuth = true
        } catch (e) {
            console.log('err', e)
            this.setLoading()
        }
    },

    setLoading() {
        this.loading = !this.loading
    },
})
