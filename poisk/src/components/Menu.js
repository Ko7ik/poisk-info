import React from "react";
import {FaSearch} from 'react-icons/fa'
import {MdMonitorHeart} from 'react-icons/md'

class Menu extends React.Component {
    
    

    render(){
        
        return(
            <div className="menu">
               <div className="search" ><FaSearch color='#313131' size={28} /> </div> 
               <div className="monitor"><MdMonitorHeart color='#313131' size={28} /></div> 

            </div>
        )
    }
}

export default Menu

