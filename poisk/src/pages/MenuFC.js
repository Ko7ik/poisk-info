import { FaSearch } from 'react-icons/fa'
import { MdMonitorHeart } from 'react-icons/md'
import { RiLogoutBoxFill } from 'react-icons/ri'
import { Link } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

const MenuFC = observer(() => {
    const { currentUser } = useRootStore()
    const onOut = async () => {
        await currentUser.logout()
        console.log('logout')
    }
    return (
        <div className="menu">
            <div className="flexmenu">
                <Link to="/login"></Link>
                <Link to="/form">
                    <div className="search" title="Запрос на поиск">
                        <FaSearch color="#313131" size={28} />{' '}
                    </div>
                </Link>
                <Link to="/tasks">
                    <div className="search" title="Список заданий">
                        <MdMonitorHeart color="#313131" size={28} />
                    </div>
                </Link>
                <div className="search" title="Выйти">
                    <RiLogoutBoxFill
                        color="#313131"
                        size={28}
                        onClick={onOut}
                    />
                </div>
            </div>
        </div>
    )
})

export default MenuFC
