import React from 'react'
import { Link } from 'react-router-dom'

const Login = () => {
    return (
        <div className="Main"> 
            <div className='login'>
                <form>
                    <h2>Вход</h2>
                    <input type="text" placeholder='Логин' required />
                    <input type="password" placeholder='Пароль' required />
                    <button type='submit'>Войти</button>
                </form>
                <Link to="/register">
                        <p>Регистрация</p>
                </Link>
            </div>
        </div>
    )
}

export default Login