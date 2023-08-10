// Использование фукциональной компоненты(FC)
import React from 'react'
import { SiVk } from 'react-icons/si'

import axios from 'axios'

export const FormFC = () => {
    const iniState = {
        radio: false,
        url: '',
        keywords: '',
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

        const response = await axios.post('https://reqres.in/api/users', form)

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
                        name="radio"
                        value="public"
                        checked={form.radio === 'public' ? true : false}
                        onChange={handleChange}
                    />
                    <input
                        id="fid-2"
                        type="radio"
                        name="radio"
                        value="user"
                        checked={form.radio === 'user' ? true : false}
                        onChange={handleChange}
                    />
                </div>
                <input
                    placeholder="URL"
                    name="url"
                    value={form.url}
                    onChange={handleChange}
                />
                <textarea
                    placeholder="Ключевые слова"
                    name="keywords"
                    value={form.keywords}
                    onChange={handleChange}
                />

                <button type="submit">Запустить процесс</button>
            </form>
        </div>
    )
}
