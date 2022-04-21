import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';
import { MoralisProvider } from 'react-moralis';
ReactDOM.render(
  <React.StrictMode>
    <MoralisProvider
      serverUrl="https://hwh9jntrogn6.usemoralis.com:2053/server" //FILL THIS IN
      appId="UaqFEkYjZetuOvuMIPi7JD8MNHYn7m8coEfGjeSP" //FILL THIS IN
    >
    <App />
    </MoralisProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
