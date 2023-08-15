import React from 'react'
import { FaSearch } from 'react-icons/fa'
import { MdMonitorHeart } from 'react-icons/md'
import { Link } from 'react-router-dom'

function MenuFC(){
    return (
        <div className="menu">
            <div className="flexmenu">
                    <Link to="/form">
                        <div className="search">
                            <FaSearch color="#313131" size={28} />{' '}
                        </div>
                    </Link>
                    <Link to="/monitor">
                        <div className="monitor">
                            <MdMonitorHeart color="#313131" size={28} />
                        </div>
                    </Link>
            </div>
        </div>
    )
}

export default MenuFC
