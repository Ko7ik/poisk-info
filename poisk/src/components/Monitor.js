import React from "react";
import axios from "axios";

const baseUrl = "http://192.168.0.189:8000/found_data/"

class Monitor extends React.Component  {
    constructor(props) {
        super(props)

        axios.get(baseUrl).then((res)=>{
            this.setState({foundData:res.data.data})
        })
        this.state = {
            foundData:[]
        }
    }

    render() {
        return(
            <div className="Main">
               <h3>{this.state.foundData.url_groupe} {this.state.foundData.date}</h3>
                <p>{this.state.foundData.found_text}</p>
                
            </div>
        )
    }
}

export default Monitor

//