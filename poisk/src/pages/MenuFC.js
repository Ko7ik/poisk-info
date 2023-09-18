import { FaSearch } from 'react-icons/fa'
import { MdMonitorHeart } from 'react-icons/md'
import { RiLogoutBoxFill } from 'react-icons/ri'
import { Link, Outlet } from 'react-router-dom'

import { observer } from 'mobx-react-lite'

import { useRootStore } from '../store'

const MenuFC = observer(() => {
    const { currentUser } = useRootStore()
    const onOut = async () => {
        await currentUser.logout()
        console.log('logout')
    }
    return (
        <>
            <div className="menu">
                <div className="flexmenu">
                    <Link to="/">
                        <div className="search" title="Запрос на поиск">
                            <FaSearch color="#AAB8CB" size={28} />{' '}
                        </div>
                    </Link>
                    <Link to="/tasks">
                        <div className="search" title="Список заданий">
                            <MdMonitorHeart color="#AAB8CB" size={28} />
                        </div>
                    </Link>
                    <div className="search" title="Выйти">
                        <RiLogoutBoxFill
                            color="#AAB8CB"
                            size={28}
                            onClick={onOut}
                        />
                    </div>
                </div>
            </div>
            <Outlet />
        </>
    )
})

export default MenuFC
