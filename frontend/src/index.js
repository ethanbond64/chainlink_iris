import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import history from './utils/History';
import './styles/index.css';
import App from './App';
import reportWebVitals from './utils/reportWebVitals';
import logo from './imgs/IrisLogoBetter.png';

function Routing() {
  return (
    <Router history={history}>
      <div className={`lg:container lg:mx-auto h-screen`}>
        <div className={`relative w-full h-30 mb-10`}>
          <Link to="/" ><img src={logo} className={`h-30`}  alt="Iris Logo" /></Link>
          <div className={`mt-8 absolute inset-y-0 right-0`}>
            <a className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`}>
              New Event +
            </a>
            <a className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`}>
              Help
            </a>
            <div className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`} >
              About
            </div>
          </div>
          {/* <Link to="/" ><img src={logo} alt="Chia No Code Logo" /></Link> */}
        </div>
        <Routes>
          <Route exact path="/" element={<App />} />
        </Routes>
      </div>
    </Router>
    );
  }

ReactDOM.render(
  <React.StrictMode>
    <Routing />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
