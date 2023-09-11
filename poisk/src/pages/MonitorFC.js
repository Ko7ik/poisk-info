import React from 'react'
import { IoIosArrowDropleftCircle } from 'react-icons/io'
import { Link, useParams } from 'react-router-dom'

import axios from 'axios'

function MonitorFC() {
    const [MonitorState, setMonitorState] = React.useState([])
    const { id_task } = useParams()

    React.useEffect(() => {
        axios
            .get(
                `http://192.168.43.151:8000/api/found_data/id_task/${id_task}`,
                {
                    headers: {
                        Authorization: 'Token ' + localStorage.getItem('token'),
                    },
                },
            )
            .then((data) => {
                setMonitorState(data.data)
            })
            .then((response) => console.log(response))

            .catch((err) => {
                console.log(err)
            })
    }, [id_task])

    console.log(MonitorState)

    const content = MonitorState.map((monitor, index) => (
        <div key={index.id.id_found_data} className="ContentBlock">
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
            {id_task}
            <Link to="/tasks">
                <div className="backmenu">
                    <IoIosArrowDropleftCircle size={36} color="#D0D8E4" />
                </div>
            </Link>
            <div className="content">{content}</div>
            {content.length === 0 && (
                <div className="no-data">
                    <img src="img/no_data.png" width="300" alt="" />
                    <h3>Нет данных</h3>
                </div>
            )}
        </div>
    )
}

export default MonitorFC
