import React, { useState } from 'react'
import { Link } from 'react-router-dom'

import axios from 'axios'

const Register = () => {

    const iniState = {
        email: '',
        username: '',
        password: '',
    }
    
    const [form, setForm] = React.useState(iniState)

    const handleChange = (event) => {

        setForm({ ...form, [event.target.name]: event.target.value })
    }

    const handleSubmit = async (event) => {
        event.preventDefault()
        console.log('FORM: ', form)

        setForm(iniState)
        
        const response = await axios.post('http://192.168.0.189:8000/auth/users/', form)
        console.log(response)

        
    }

    return (
        
        <div className="Main"> 
            <div className='login'>
                <form onSubmit={handleSubmit}>
                    <h2>Регистрация</h2>
                   
                    <input
                        type="email"
                        placeholder="email"
                        name="email"
                        id="email"
                        required
                        onChange={handleChange}
                    />

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
                        placeholder='Пароль'  
                        required 
                        onChange={handleChange}
                    />

                    <input 
                        type="password" 
                        placeholder='Повторите пароль' 
                        required
                        //добавить проверку пароля (пока не знаю как)
                        
                    />
                    
                    <button type='submit' >Зарегистрироваться</button>
                </form>
                <Link to="/login">
                        <p>Вход</p>
                </Link>
            </div>
        </div>
    )
}


export default Register