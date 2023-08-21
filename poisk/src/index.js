import * as ReactDOMClient from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'

import App from './App'
import { rootStore, RootStoreProvider } from './store'

import './css/main.css'
import './css/index.css'

const app = ReactDOMClient.createRoot(document.getElementById('app'))
app.render(
    <RootStoreProvider store={rootStore}>
        <BrowserRouter>
            <App />
        </BrowserRouter>
        ,
    </RootStoreProvider>,
)
