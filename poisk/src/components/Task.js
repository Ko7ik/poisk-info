import React from 'react'
import { AiFillPlayCircle } from 'react-icons/ai'
import { Link } from 'react-router-dom'

import axios from 'axios'
import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

export const Tasks = observer(() => {
    const { taskUser } = useRootStore()
    const [MonitorState, setMonitorState] = React.useState([])
    const [start, setStart] = React.useState(false)

    React.useEffect(() => {
        axios
            .get('http://192.168.0.189:8000/api/task/', {
                headers: {
                    Authorization: 'Token ' + localStorage.getItem('token'),
                },
            })
            .then((data) => {
                setMonitorState(data.data)
            })
            .then((response) => console.log(response))

            .catch((err) => {
                console.log(err)
            })
    }, [])

    const onSubmit = async () => {
        await taskUser.start()
    }

    // const Monitor = [localStorage.getItem('taskList')]
    // console.log(Monitor)
    const content = MonitorState.map((tasks) => (
        <div
            key={tasks.id}
            className="flex flex-col grow justify-start items-center m-5 p-4 gap-2 bg-slate-200 rounded-md text-slate-950 "
        >
            <div className="flex flex-row justify-center items-center gap-2 ">
                <button type="button" onClick={onSubmit}>
                    <AiFillPlayCircle size={36} />
                </button>
            </div>
            <div className="lex flex-col justify-start text-left gap-3">
                <h3>Социальная сеть {tasks.social_net}</h3>
                <p>URL группы: {tasks.url_group}</p>
                <p>Слова для поиска: {tasks.search_text}</p>
            </div>
            <div className="mt-5">
                {taskUser.unsuccess && (
                    <p className="flex justify-center items-center mb-2 py-3 mx-3 font-semibold text-red-500 bg-red-100 rounded-md">
                        Ошибка запуска парсера
                    </p>
                )}
                {taskUser.success && (
                    <p className="flex justify-center items-center mb-2 py-3 mx-3 font-semibold text-green-500 bg-green-100 rounded-md">
                        Поиск завершен
                    </p>
                )}
            </div>
            <Link to="/monitor">
                <button
                    // onClick={taskUser.foundText(tasks.id)}
                    className="flex items-center justify-center gap-1 p-3 font-semibold bg-neutral-800 text-white"
                >
                    Посмотреть результаты поиска
                </button>
            </Link>
        </div>
    ))

    return (
        <div className="Main2">
            <div>{content}</div>
        </div>
    )
})
