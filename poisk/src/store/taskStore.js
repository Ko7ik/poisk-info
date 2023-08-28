import axios from 'axios'
import { makeAutoObservable } from 'mobx'

export const taskUser = makeAutoObservable({
    tasks: [],
    isAuth: false,
    loading: false,
    success: false,
    unsuccess: false,

    async taskList(net, url, text) {
        console.log('создать задание')
        this.setLoading()
        try {
            const taskForm = {
                social_net: net,
                url_group: url,
                search_text: text,
                user_id: localStorage.getItem('user_id'),
            }
            console.log(taskForm)
            const response = await axios.post(
                'http://192.168.0.189:8000/api/task/',
                taskForm,
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
            console.log('task', response)
            // this.task = taskForm
            this.success = true
            this.setLoading()
        } catch (e) {
            console.log('err', e)
            this.setLoading()
            this.unsuccess = true
        }
    },

    async getTaskList() {
        console.log('получение списка тасков')
        this.setLoading()
        try {
            const response = await axios.get(
                'http://192.168.0.189:8000/api/task/',
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
            console.log('task', response)
            this.setLoading()
        } catch (e) {
            console.log('оштбка получения списка тасков', e)
            this.setLoading()
        }
    },

    async start() {
        console.log('запустить парсер')
        this.setLoading()
        try {
            const response = await axios.post(
                'http://192.168.0.189:8000/api/parser_run/',
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
            console.log('Состояние', response)
            // this.task = taskForm
            this.success = true
            this.setLoading()
        } catch (e) {
            console.log('err', e)
            this.setLoading()
            this.unsuccess = true
        }
    },

    async foundText(id) {
        console.log('получение списка тасков')
        this.setLoading()
        try {
            // const foundData = {
            //     social_net: id,
            // }
            const response = await axios.get(
                'http://192.168.0.189:8000/api/task/', //+ id
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
            console.log('task', response)
            this.task = response.data.data
            this.setLoading()
        } catch (e) {
            console.log('ошибка получения списка тасков', e)
            this.setLoading()
        }
    },

    setLoading() {
        this.loading = !this.loading
    },
})
