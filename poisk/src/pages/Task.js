import React from 'react'

import { observer } from 'mobx-react-lite'

import { CardSkeleton } from '../components/CardSkeleton'
import TasksCard from '../components/TaskCard'
import { useRootStore } from '../store'

import 'react-loading-skeleton/dist/skeleton.css'

export const Tasks = observer(() => {
    const { taskUser } = useRootStore()

    React.useEffect(() => {
        taskUser.getTaskList()
    }, [])

    const content = taskUser.tasks.map((task) => (
        <TasksCard task={task} key={task.id} />
    ))

    return (
        <div className="Main">
            <div className=" grid grid-cols-3 grow">
                {taskUser.loading && <CardSkeleton cards={6} />}

                {content}
                {content.length === 0 && (
                    <div className="no-data">
                        <h3>Нет заданий</h3>
                    </div>
                )}
            </div>
        </div>
    )
})

export default Tasks
