// Использование фукциональной компоненты(FC)
import React from 'react'
import { useState } from 'react'
import { SiVk } from 'react-icons/si'

import axios from 'axios'

export const FormFC = () => {
    const [success, setSuccess] = useState(false)
    const [unsuccess, setUnsuccess] = useState(false)
    const iniState = {
        social_net: 1,
        url_group: '',
        search_text: '',
        user_id: localStorage.getItem('user_id'),
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

        const response = await axios
            .post('http://192.168.0.189:8000/api/task/', form, {
                headers: {
                    Authorization: 'Token ' + localStorage.getItem('token'),
                },
            })
            .catch((err) => {
                console.log(err)
                setUnsuccess(true)
            })
        console.log(response)
    }

    return (
        <div className="Main">
            <form onSubmit={handleSubmit}>
                <h1 className="text-base font-black uppercase mb-12 pb-5 border-b-4 border-zinc-700 border-dotted">
                    Создать новый запрос
                </h1>
                <label htmlFor="SocNet">Социальная сеть / мессенджер</label>
                <select name="social_net" onChange={handleChange} id="SocNet">
                    <option value={1} selected>
                        Вконтакте
                    </option>
                    <option value={2}>Telegram</option>
                </select>
                {/* <div className="radio">
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
                </div> */}
                <label htmlFor="url">URL</label>
                <input
                    id="url"
                    placeholder="https://..."
                    name="url_group"
                    value={form.url_group}
                    onChange={handleChange}
                />
                <textarea
                    placeholder="Ключевые слова"
                    name="search_text"
                    value={form.search_text}
                    onChange={handleChange}
                />

                <div className="mt-5">
                    {success && (
                        <p className="flex items-center gap-1 mb-5 font-semibold text-green-500">
                            Форма успешно отправлена
                        </p>
                    )}
                    {unsuccess && (
                        <p className="flex items-center gap-1 mb-5 font-semibold text-red-500">
                            Ошибка отправки формы
                        </p>
                    )}

                    <button type="submit">Запустить процесс</button>
                </div>
            </form>
        </div>
    )
}
