import React from 'react'

import axios from 'axios'

const apiUrl = 'http://192.168.0.17:8000/found_data/'

function MonitorFC() {
    const [MonitorState, setMonitorState] = React.useState([])

    React.useEffect(() => {
        axios
            .get(apiUrl, {
                headers: { Authorization: localStorage.getItem('token') },
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

    const content = MonitorState.map((monitor) => (
        <div key={monitor.id} className="ContentBlock">
            <h3>Публикация №{monitor.id_post}</h3>
            <p>{monitor.img}</p>
            <h3>Время публикации: {monitor.date_post}</h3>
            <p>Текст: {monitor.found_text}</p>
        </div>
    ))

    return (
        <div className="Main2">
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
