import { Fragment, useEffect } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import LogForm from './pages/LogForm'
import MenuFC from './pages/MenuFC'
import MonitorFC from './pages/MonitorFC'
import RegForm from './pages/RegForm'
import { Tasks } from './pages/Task'
import TaskForm from './pages/TaskForm'
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
