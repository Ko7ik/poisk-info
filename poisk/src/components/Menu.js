import React from 'react'
import { FaSearch } from 'react-icons/fa'
import { MdMonitorHeart } from 'react-icons/md'
import { Link } from 'react-router-dom'

class Menu extends React.Component {
    render() {
        return (
            <div className="menu">
                <Link to="/">
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
        )
    }
}

export default Menu