import { createContext, useContext } from 'react'

import { currentUser } from './currentUserStore'
//import { monitorStore } from "./MonitorStore";

export const rootStore = { currentUser /*monitorStore*/ }

export const RootStoreContext = createContext({ rootStore })

export const useRootStore = () => useContext(RootStoreContext)

export const RootStoreProvider = ({ store, children }) => {
    return (
        <RootStoreContext.Provider value={store}>
            {children}
        </RootStoreContext.Provider>
    )
}
