import React, { useEffect, useState } from 'react'
import { Form, Navigate, Route, Routes } from 'react-router-dom'

import { FormFC } from './components/FormFC'
import RegForm from './components/FormValid/RegForm'
import MenuFC from './components/MenuFC'
import MonitorFC from './components/MonitorFC'
//import Login from './components/Login'
import Register from './components/Register'

function App() {
    const [isAuth, setIsAuth] = useState(false)

    useEffect(() => {
        const TrueToken = localStorage.getItem('token')
        console.log(localStorage.getItem('token') + ' Токен в локал сторанж')
        console.log(TrueToken + ' значение токена TrueToken')

        if (TrueToken === 'null') {
            setIsAuth(false)
            console.log('значение нул')
        }
        if (TrueToken) {
            setIsAuth(true)
            console.log('токен есть')
        }

        console.log(isAuth)
    }, [])

    //проверка из стора

    return isAuth ? (
        <div className="body">
            {console.log('isAuth = true, загрузка формы')}
            <MenuFC />
            <Routes>
                <Route path="/form" element={<FormFC />}></Route>
                <Route path="/monitor" element={<MonitorFC />}></Route>
                <Route path="/*" element={<Navigate replace to="/form" />} />
            </Routes>
        </div>
    ) : (
        (console.log('isAuth = false, загрузка логина'),
        (
            <Routes>
                <Route path="/login" element={<RegForm />}></Route>
                <Route path="/register" element={<Register />}></Route>
                <Route path="/*" element={<Navigate replace to="/login" />} />
            </Routes>
        ))
    )
}

export default App
