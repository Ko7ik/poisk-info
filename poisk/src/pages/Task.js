import React from 'react'
import { AiFillPlayCircle } from 'react-icons/ai'

import { observer } from 'mobx-react-lite'

import TasksCard from '../components/TaskCard'
import { useRootStore } from '../store'

export const Tasks = observer(() => {
    const { taskUser } = useRootStore()

    React.useEffect(() => {
        taskUser.getTaskList()
    }, [])

    const onSubmit = async () => {
        await taskUser.start()
    }

    const content = taskUser.tasks.map((task) => (
        <TasksCard task={task} key={task.id} />
    ))

    return (
        <div className="Main">
            <div className=" flex flex-col grow">
                <div
                    title="Запустить поиск"
                    className="flex flex-row justify-start items-center gap-5"
                >
                    <button type="button" onClick={onSubmit}>
                        <AiFillPlayCircle
                            className="fill-white hover:fill-neutral-400"
                            size={36}
                        />
                    </button>
                </div>
                {taskUser.loading}
                {content}
            </div>
        </div>
    )
})

export default Tasks
