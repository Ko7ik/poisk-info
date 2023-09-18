import { makeAutoObservable } from 'mobx'

import {
    getTaskListAPI,
    MonitAPI,
    startAPI,
    taskListAPI,
} from '../components/api/api'

export const taskUser = makeAutoObservable({
    tasks: [],
    results: [],
    isAuth: false,
    loading: false,
    success: false,
    unsuccess: false,

    async taskList(net, url, text) {
        console.log('создать задание')
        try {
            const taskForm = {
                social_net: net,
                url_source: url,
                search_text: text,
                user_id: localStorage.getItem('user_id'),
            }
            console.log(taskForm)
            const response = await taskListAPI(taskForm)
            console.log('task', response)
            this.success = true
        } catch (e) {
            console.log('err', e)
            this.unsuccess = true
        }
    },

    async getTaskList() {
        console.log('получение списка тасков')
        this.setLoading()
        try {
            const response = await getTaskListAPI()
            this.tasks = [...response.data]
            this.setLoading()
        } catch (e) {
            console.log('ошибка получения списка тасков', e)
            this.setLoading()
        }
    },

    async start() {
        console.log('запустить парсер')
        try {
            const response = await startAPI()
            console.log('Состояние', response)
            this.success = true
        } catch (e) {
            console.log('err', e)
            this.unsuccess = true
        }
    },

    async foundText() {
        console.log('получение результатов тасков')
        this.setLoading()
        try {
            const response = await MonitAPI()
            this.results = [...response.data]
            this.setLoading()
        } catch (e) {
            console.log('ошибка получения результатов', e)
            this.setLoading()
        }
    },

    setLoading() {
        this.loading = !this.loading
    },
})
