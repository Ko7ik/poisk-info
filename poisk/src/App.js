import { Fragment, useEffect } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

// import Login from './components/Login'
import LogForm from './components/FormValid/LogForm'
import RegForm from './components/FormValid/RegForm'
import TaskForm from './components/FormValid/TaskForm'
import MenuFC from './components/MenuFC'
import MonitorFC from './components/MonitorFC'
//import Register from './components/Register'
import { Tasks } from './components/Task'
import { useRootStore } from './store'

const App = observer(() => {
    const { currentUser } = useRootStore()
    useEffect(() => {
        currentUser.checkToken()
    }, [])

    console.log(currentUser.isAuth)

    return currentUser.isAuth ? (
        <div className="body">
            {console.log('isAuth = true, загрузка формы')}
            <Routes>
                <Route
                    path="/form"
                    element={
                        <Fragment>
                            <MenuFC />
                            <TaskForm />
                        </Fragment>
                    }
                />
                <Route
                    path="/tasks"
                    element={
                        <Fragment>
                            <MenuFC />
                            <Tasks />
                        </Fragment>
                    }
                />
                <Route path="/monitor" element={<MonitorFC />}></Route>
                <Route path="/*" element={<Navigate replace to="/form" />} />
            </Routes>
        </div>
    ) : (
        (console.log('isAuth = false, загрузка логина'),
        (
            <Routes>
                <Route path="/login" element={<LogForm />}></Route>
                <Route path="/register" element={<RegForm />}></Route>
                <Route path="/*" element={<Navigate replace to="/login" />} />
            </Routes>
        ))
    )
})

export default App
