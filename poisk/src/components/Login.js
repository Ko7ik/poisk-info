import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'



const Login = () => {

    const iniState = {
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
        
        const response = await axios.post('http://192.168.0.17:8000/auth/token/login', form)
        console.log(response)
        localStorage.setItem('token', response.data.auth_token);
        
        

    }

    return (
        <div className="Main"> 
            <div className='login'>
                <form onSubmit={handleSubmit}>
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
                        placeholder='Пароль'  
                        required 
                        onChange={handleChange}
                    />
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
