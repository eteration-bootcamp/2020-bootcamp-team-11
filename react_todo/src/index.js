import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import createReducer from './reducers'
import App from './components/App'
import * as serviceWorker from './serviceWorker';

const store = createStore(
    createReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)

serviceWorker.unregister();