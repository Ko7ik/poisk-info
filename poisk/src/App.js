import { Fragment, useEffect, useState } from 'react'
import {
    createBrowserRouter,
    createRoutesFromElements,
    Navigate,
    Route,
    RouterProvider,
} from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import LogForm from './pages/LogForm'
import MenuFC from './pages/MenuFC'
import MonitorFC from './pages/MonitorFC'
import RegForm from './pages/RegForm'
import { Tasks } from './pages/Task'
import TaskForm from './pages/TaskForm'
import { useRootStore } from './store'

const router1 = createBrowserRouter(
    createRoutesFromElements(
        <>
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
        </>,
    ),
)

const router2 = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="/login" element={<LogForm />}></Route>
            <Route path="/register" element={<RegForm />}></Route>
            <Route path="/*" element={<Navigate replace to="/login" />} />
        </>,
    ),
)

const App = observer(() => {
    const { currentUser } = useRootStore()

    useEffect(() => {
        currentUser.checkToken()
    }, [])

    return currentUser.isAuth ? (
        <div className="body">
            <RouterProvider router={router1} />
        </div>
    ) : (
        (console.log('isAuth = false, загрузка логина'),
        (<RouterProvider router={router2} />))
    )
})

export default App
