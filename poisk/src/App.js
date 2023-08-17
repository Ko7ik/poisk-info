import React from 'react'
import { Route, Routes, Navigate } from 'react-router-dom'
import { FormFC } from './components/FormFC'
import MenuFC from './components/MenuFC'
import MonitorFC from './components/MonitorFC'
import Login from './components/Login'
import Register from './components/Register'
import { useEffect, useState } from 'react';



function App() {

    const [isAuth, setIsAuth] = useState(false)

    useEffect(() => {

        let TrueToken = localStorage.getItem('token')
        console.log(localStorage.getItem('token') + " Токен в локал сторанж")
        console.log(TrueToken + " значение токена TrueToken")

        if (TrueToken === "null") {
            setIsAuth(false)
            console.log('значение нул')
        }
        if (TrueToken) {
            setIsAuth(true)
            console.log('токен есть')
        }

        console.log(isAuth)

    }, []);




    return isAuth ? (
        <div className="body">
            {console.log("isAuth = true, загрузка формы")}
            <MenuFC />
            <Routes>
                <Route path="/form" element={<FormFC />}></Route>
                <Route path="/monitor" element={<MonitorFC />}></Route>
                <Route path="/*" element={<Navigate replace to="/form" />} />
            </Routes>
        </div>


    ) : (

        console.log("isAuth = false, загрузка логина"),
        <Routes>
            <Route path="/login" element={
              
                    <Login />
    
            }></Route>
            <Route path="/register" element={<Register />}></Route>
            <Route path="/*" element={<Navigate replace to="/login" />} />
        </Routes>
    )

}

export default App
