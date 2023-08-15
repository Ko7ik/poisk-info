import React from 'react'
import { Link } from 'react-router-dom'

const Register = () => {
    return (
        <div className="Main"> 
            <div className='login'>
                <form>
                    <h2>Регистрация</h2>
                    <input type="text" placeholder='Логин' required />
                    <input type="password" placeholder='Пароль' required />
                    <button type='submit'>Войти</button>
                </form>
                <Link to="/register">
                        <p>Вход</p>
                </Link>
            </div>
        </div>
    )
}

export default Register