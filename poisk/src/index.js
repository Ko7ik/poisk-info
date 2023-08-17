import React from 'react'
import * as ReactDOMClient from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { rootStore, RootStoreProvider } from "./store";
import App from './App'

import './css/main.css'

const app = ReactDOMClient.createRoot(document.getElementById('app'))
app.render(
    <RootStoreProvider store={rootStore}>
    <BrowserRouter>
        <App />
    </BrowserRouter>,
    </RootStoreProvider>
)
