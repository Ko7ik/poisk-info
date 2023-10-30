import React from 'react'
import { FaRegFolderOpen } from 'react-icons/fa'
import { IoIosArrowDropleftCircle } from 'react-icons/io'
import { Link } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { ResultsSkeleton } from '../components/CardSkeleton'
import { useRootStore } from '../store'

const MonitorFC = observer(() => {
    const { taskUser } = useRootStore()
    // const { id_task } = useParams()

    React.useEffect(() => {
        taskUser.foundText()
    }, [])

    const content = taskUser.results.map((monitor) => (
        <div key={monitor.id_found_data} className="ContentBlock">
            <h3 className="text-xl font-bold normal-case">
                Публикация №{monitor.id_post}
            </h3>
            <div className="flex flex-row flex-wrap gap-4">
                {monitor.img !== null &&
                    monitor.img.map((image, ind) => {
                        return (
                            <div key={ind}>
                                <img src={image} width="300" alt="" />
                            </div>
                        )
                    })}
            </div>
            <h3 className="text-xl font-bold normal-case">
                Время публикации: {monitor.date_post}
            </h3>
            <p>Текст: {monitor.found_text}</p>
        </div>
    ))

    console.log('content', content)

    return (
        <div className="Monitor-layout">
            <Link to="/tasks">
                <div className="backmenu">
                    <IoIosArrowDropleftCircle size={36} color="#D0D8E4" />
                </div>
            </Link>

            <div className="content">
                <div>{taskUser.loading && <ResultsSkeleton cards={4} />}</div>
                {content}
                {content.length === 0 && (
                    <div className="no-data">
                        <FaRegFolderOpen size="10em" />
                        <h3>Нет данных</h3>
                    </div>
                )}
            </div>
        </div>
    )
})

export default MonitorFC
