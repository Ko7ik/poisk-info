import React from "react";
import axios from "axios";

const apiUrl = 'http://192.168.0.189:8000/found_data/';

function MonitorFC() {

    const [MonitorState, setMonitorState] = React.useState([]);
    
    React.useEffect(() => {
        
        axios
            .get(apiUrl)
            .then((data => {
                setMonitorState (data.data)
            }))

      .catch((err) => {
        console.log(err)});
    }, []);
  

    console.log (MonitorState)
 
    const content = MonitorState.map((monitor) => 
        <div key={monitor.id} className="ContentBlock">
            <h3>Публикация №{monitor.id_post}</h3>
            <img src={monitor.image}/>
            <h3>Время публикации: {monitor.time}</h3>
            <p>Текст:{monitor.text}</p>
        </div> 
    )

  return (
        <div className="Main2">
           <div>
                {content} 
            </div>
        </div>
    );
}


export default MonitorFC