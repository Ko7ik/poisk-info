import React from 'react'
import { IoIosArrowDropleftCircle } from 'react-icons/io'
import { Link } from 'react-router-dom'

import axios from 'axios'

const apiUrl = 'http://192.168.43.151:8000/api/found_data/'

function MonitorFC() {
    const [MonitorState, setMonitorState] = React.useState([])

    React.useEffect(() => {
        axios
            .get(apiUrl, {
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

    console.log(MonitorState)

    const content = MonitorState.map((monitor, index) => (
        <div key={index.id_found_data} className="ContentBlock">
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
            <div className="content">{content}</div>
            {content.length === 0 && <p>Not</p>}
        </div>
    )
}

export default MonitorFC

//         <div className="Main">
//            {MonitorState.map(monitor => {
//             return (
//                 <div key={monitor.id}>
//                     <p>{monitor.email}</p>
//                 </div>
//             );
//            })}
//         </div>
