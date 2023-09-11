import React from 'react'
import { Link } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

const TasksCard = observer(({ task }) => {
    const { taskUser } = useRootStore()
    React.useEffect(() => {
        taskUser.success = false
        taskUser.unsuccess = false
    }, [])
    return (
        <div key={task.id_task_name} className="task-card">
            <div className="flex flex-col justify-start text-left gap-3">
                <h3 className="font-semibold">Задание № {task.id_task_name}</h3>
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
                <h3 className="status">{task.status}</h3>
                <Link
                    key={task.id_task_name}
                    to={`/tasks/${task.id_task_name}`}
                >
                    <button className="flex justify-center items-center gap-1 p-3 font-semibold ">
                        Посмотреть результаты
                    </button>
                </Link>
            </div>
        </div>
    )
})
export default TasksCard
