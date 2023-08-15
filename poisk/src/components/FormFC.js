// Использование фукциональной компоненты(FC)
import React from 'react'
import { SiVk } from 'react-icons/si'

import axios from 'axios'

export const FormFC = () => {
    const iniState = {
        //public: false,
        //person: false,
        url_groupe: '',
        search_string: '',
        //+ токен
    }
    // спользование хука useState для хранения состояния
    const [form, setForm] = React.useState(iniState)

    const handleChange = (event) => {
        // ...form  - деструктуризация, добавляем старые значения, и добавляем(заменяем) новыми
        setForm({ ...form, [event.target.name]: event.target.value })
    }

    const handleSubmit = async (event) => {
        event.preventDefault()
        console.log('FORM: ', form)

        //отчищаем форму
        setForm(iniState)

        const response = await axios.post('http://192.168.0.189:8000/search_data/', form)
        console.log(response)
    }

    return (
        <div className="Main">
            <form onSubmit={handleSubmit}>
                <div className="ico">
                    <SiVk size={42} />
                </div>
                <label htmlFor="SocNet">Социальная сеть / мессенджер</label>
                <select name="SocialNetwork" id="SocNet">
                    <option value="vk">Вконтакте </option>
                    <option value="tg">...? </option>
                    <option value="ok">...? </option>
                </select>
                <div className="radio">
                    <label htmlFor="fid-1">Паблик</label>
                    <label htmlFor="fid-2">Пользователь</label>
                    <input
                        id="fid-1"
                        type="radio"
                        name="public"
                        value="public"
                        checked={form.radio === 'public' ? true : false}
                        onChange={handleChange}
                    />
                    <input
                        id="fid-2"
                        type="radio"
                        name="person"
                        value="user"
                        checked={form.radio === 'user' ? true : false}
                        onChange={handleChange}
                    />
                </div>
                <input
                    placeholder="URL"
                    name="url_groupe"
                    value={form.url_groupe}
                    onChange={handleChange}
                />
                <textarea
                    placeholder="Ключевые слова"
                    name="search_string"
                    value={form.search_string}
                    onChange={handleChange}
                />

                <button type="submit">Запустить процесс</button>
            </form>
        </div>
    )
}
