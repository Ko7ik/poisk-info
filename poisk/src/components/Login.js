import React from 'react'
import { Link } from 'react-router-dom'

//import axios from 'axios'
import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

const Login = observer(() => {
    const { currentUser } = useRootStore()
    const [form, setForm] = React.useState()

    const handleChange = (event) => {
        setForm({ ...form, [event.target.name]: event.target.value })
    }

    const handleSubmit = async (form) => {
        console.log('FORM: ', form)
        await currentUser.login(form.username, form.password)
        console.log('login')
    }

    return (
        <div className="Main">
            <div className="login">
                <form /*onSubmit={handleSubmit}*/>
                    {/* <h2>{currentUser.user.username}</h2> */}
                    <h2>Вход</h2>
                    <input
                        type="text"
                        placeholder="Имя пользователя "
                        name="username"
                        id="username"
                        required
                        onChange={handleChange}
                    />

                    <input
                        type="password"
                        name="password"
                        placeholder="Пароль"
                        required
                        onChange={handleChange}
                    />
                    <button
                        type="button"
                        onClick={async () => handleSubmit(form)}
                    >
                        Войти
                    </button>
                </form>
                <Link to="/register">
                    <p>Регистрация</p>
                </Link>
            </div>
        </div>
    )
})

export default Login
