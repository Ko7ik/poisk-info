import React from 'react'
import { AiFillDelete, AiFillPlayCircle } from 'react-icons/ai'
import { Link } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

export const Tasks = observer(() => {
    const { taskUser } = useRootStore()
    const [MonitorState, setMonitorState] = React.useState([])
    // const [start, setStart] = React.useState(false)

    React.useEffect(() => {
        taskUser.success = false
        taskUser.unsuccess = false
        taskUser.getTaskList()
        //     axios
        //         .get('http://192.168.0.189:8000/api/task/', {
        //             headers: {
        //                 Authorization: 'Token ' + localStorage.getItem('token'),
        //             },
        //         })
        //         .then((data) => {
        //             setMonitorState(data.data)
        //         })
        //         .then((response) => console.log(response))

        //         .catch((err) => {
        //             console.log(err)
        //         })
    }, [])

    const onSubmit = async () => {
        await taskUser.start()
    }

    const content = taskUser.tasks.map((task) => (
        <div
            key={task.id}
            className="flex flex-col justify-between m-4 py-5 px-10 gap-2 bg-neutral-300 rounded-md text-neutral-950 "
        >
            <div
                title="Запустить поиск"
                className="flex flex-row justify-end items-right gap-5"
            >
                <button type="button" onClick={onSubmit}>
                    <AiFillPlayCircle
                        className="fill-neutral-800 hover:fill-neutral-600"
                        size={36}
                    />
                </button>
                <button type="button">
                    <AiFillDelete
                        className="fill-neutral-800 hover:fill-neutral-600"
                        size={36}
                    />
                </button>
            </div>
            <div className="flex flex-col justify-start text-left gap-3">
                <h3>Социальная сеть: {task.social_net}</h3>
                <p>
                    URL группы:{' '}
                    <a
                        className=" cursor-pointer text-slate-600 hover:text-slate-800 "
                        href={task.url_group}
                        target="_blank"
                        rel="noreferrer"
                    >
                        {task.url_group}{' '}
                    </a>
                </p>

                <p>Слова для поиска: {task.search_text}</p>
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
            <div className="flex justify-between items-center">
                <h3> Статус - {task.status}</h3>
                <Link to="/monitor">
                    <button
                        // onClick={taskUser.foundText(tasks.id)}
                        className="flex justify-center items-center gap-1 p-3 font-semibold bg-neutral-800 text-white rounded-md hover:bg-neutral-600"
                    >
                        Посмотреть результаты поиска
                    </button>
                </Link>
            </div>
        </div>
    ))

    return (
        <div className="Main">
            <div className=" flex flex-col grow">{content}</div>
        </div>
    )
})
