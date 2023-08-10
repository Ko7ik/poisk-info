import React from 'react'
import { Link, Route, Routes } from 'react-router-dom'

//import Form from './components/Form'
import { FormFC } from './components/FormFC'
import Menu from './components/Menu'
import Monitor from './components/Monitor'



class App extends React.Component {
    render() {
        return (
            <div className="body">
                <Menu />

                <Routes>
                    <Route path="/" element={<FormFC />}></Route>
                    <Route path="/monitor" element={<Monitor />}></Route>
                </Routes>
            </div>
        )
    }
}



export default App
