import axios from 'axios'

const api = 'http://192.168.43.150:8000'

async function loginFormAPI(loginForm) {
    return axios.post(api + '/api/auth/token/login/', loginForm)
}

async function loginIDAPI(token) {
    return axios.get(api + '/api/auth/users/', {
        headers: {
            Authorization: 'Token ' + token,
        },
    })
}

async function checkTokenAPI() {
    return axios.get(api + '/api/validate-token/', {
        headers: {
            Authorization: 'Token ' + localStorage.getItem('token'),
        },
    })
}

async function taskListAPI(taskForm) {
    return axios.post(api + '/api/task/', taskForm, {
        headers: {
            Authorization: 'Token ' + localStorage.getItem('token'),
        },
    })
}

async function getTaskListAPI() {
    return axios.get(api + '/api/task/', {
        headers: {
            Authorization: 'Token ' + localStorage.getItem('token'),
        },
    })
}

async function startAPI() {
    return axios.post(api + '/api/parser_run/', {
        headers: {
            Authorization: 'Token ' + localStorage.getItem('token'),
        },
    })
}

async function RegAPI(data) {
    return axios.post(api + '/api/auth/users/', data)
}

async function MonitAPI(data) {
    return axios.get(api + `/api/found_data/`, {
        headers: {
            Authorization: 'Token ' + localStorage.getItem('token'),
        },
    })
}

export { loginFormAPI, loginIDAPI, checkTokenAPI }
export { taskListAPI, getTaskListAPI, startAPI, MonitAPI }

export { RegAPI }
