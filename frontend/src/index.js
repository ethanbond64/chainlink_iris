import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import history from './utils/History';
import './styles/index.css';
import App from './App';
import reportWebVitals from './utils/reportWebVitals';
import Navbar from './Navbar';
import EventForm from './EventForm';
import Contracts from './Contracts';

function Routing() {
  return (
    <Router history={history}>
      <div className={`lg:container lg:mx-auto h-screen`}>
        <Navbar/>
        <Routes>
          <Route exact path="/" element={<App />} />
          <Route exact path="/create" element={<EventForm />} />
          <Route exact path="/contracts/:event_id" element={<Contracts />} />
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
