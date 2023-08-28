import { createContext, useContext } from 'react'

import { currentUser } from './currentUserStore'
import { taskUser } from './taskStore'

//import { monitorStore } from "./MonitorStore";

export const rootStore = { currentUser, taskUser }

export const RootStoreContext = createContext({ rootStore })

export const useRootStore = () => useContext(RootStoreContext)

export const RootStoreProvider = ({ store, children }) => {
    return (
        <RootStoreContext.Provider value={store}>
            {children}
        </RootStoreContext.Provider>
    )
}
