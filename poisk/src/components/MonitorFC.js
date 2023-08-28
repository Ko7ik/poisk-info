import React from 'react'
import { IoIosArrowDropleftCircle } from 'react-icons/io'
import { Link } from 'react-router-dom'

import axios from 'axios'

const apiUrl = 'http://192.168.0.189:8000/api/found_data/'

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
        <div key={index.id} className="ContentBlock">
            <h3 className="text-xl font-bold normal-case">
                Публикация №{monitor.id_post}
            </h3>
            <div className="flex flex-row flex-wrap gap-4">
                {monitor.img.map((image, ind) => {
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

    return (
        <div className="flex flex-row justify-between gap-3">
            <Link to="/task">
                <div className="backmenu">
                    <IoIosArrowDropleftCircle size={36} />
                </div>
            </Link>
            <div className="content">{content}</div>
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
