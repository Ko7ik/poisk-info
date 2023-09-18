import { useEffect } from 'react'
import ReactLoading from 'react-loading'
import { SkeletonTheme } from 'react-loading-skeleton'
import {
    createBrowserRouter,
    createRoutesFromElements,
    Route,
    RouterProvider,
} from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import LogForm from './pages/LogForm'
import MenuFC from './pages/MenuFC'
import MonitorFC from './pages/MonitorFC'
import PageNotFound from './pages/PageNotFound'
import RegForm from './pages/RegForm'
import { Tasks } from './pages/Task'
import TaskForm from './pages/TaskForm'
import { useRootStore } from './store'

const router1 = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="/" element={<MenuFC />}>
                <Route index element={<TaskForm />} />
                <Route path="tasks" element={<Tasks />} />
            </Route>

            <Route path="/tasks/:id" element={<MonitorFC />}></Route>
            <Route path="*" element={<PageNotFound />} />
        </>,
    ),
)

const router2 = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="/" element={<LogForm />}></Route>
            <Route path="/register" element={<RegForm />}></Route>
            <Route path="*" element={<PageNotFound />} />
        </>,
    ),
)

const App = observer(() => {
    const { currentUser } = useRootStore()

    useEffect(() => {
        currentUser.checkToken()
    }, [])
    if (currentUser.isLoading) {
        return (
            <div className="loading">
                <ReactLoading
                    type="bars"
                    color="#fff"
                    height={100}
                    width={50}
                />
            </div>
        )
    }
    if (!currentUser.isLoading) {
        return currentUser.isAuth ? (
            <SkeletonTheme baseColor="#3B4250" highlightColor="#7F8490">
                <div className="body">
                    <RouterProvider router={router1} />
                </div>
            </SkeletonTheme>
        ) : (
            (console.log('isAuth = false, загрузка логина'),
            (<RouterProvider router={router2} />))
        )
    }
})

export default App
