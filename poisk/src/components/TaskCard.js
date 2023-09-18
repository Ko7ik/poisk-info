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
            <div className="flex flex-col justify-start text-left gap-5">
                <h3 className="status">{task.status}</h3>
                <h3 className="font-bold">Задание № {task.id_task_name}</h3>
                <div>
                    <h3 className="font-semibold">Социальная сеть: </h3>
                    <h3 className="words">{task.social_net}</h3>
                </div>
                <p>
                    <p className="font-semibold">URL:</p>
                    <a
                        className=" source "
                        href={task.url_source}
                        target="_blank"
                        rel="noreferrer"
                    >
                        {task.url_source}{' '}
                    </a>
                </p>
                <div>
                    <p className="font-semibold">Слова для поиска: </p>
                    <p className="words">{task.search_text}</p>
                </div>
            </div>
            <Link key={task.id_task_name} to={`/tasks/${task.id_task_name}`}>
                <button className="flex justify-center mt-10 items-center gap-1 p-3 font-semibold ">
                    Посмотреть результаты
                </button>
            </Link>
        </div>
    )
})
export default TasksCard
