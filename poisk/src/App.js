import React from 'react'
import { Route, Routes, Navigate } from 'react-router-dom'
//import Form from './components/Form'
import { FormFC } from './components/FormFC'
import MenuFC from './components/MenuFC'
import MonitorFC from './components/MonitorFC'
import Login from './components/Login'

function App() {


    let isAuth = true

    return isAuth ?  ( 
        <div className="body">
            <MenuFC/>
            <Routes>
                <Route path="/form" element={<FormFC />}></Route>
                <Route path="/monitor" element={<MonitorFC />}></Route>
                <Route path="/*" element={<Navigate replace to="/form"/>}/>
            </Routes>
        </div>
    )

    :  <Login />

}

export default App
