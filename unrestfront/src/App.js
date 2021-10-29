// import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route } from "react-router-dom";

import Order from "./Components/Order/index";

function App() {
  return (
    <div className="App">
      <div>
        <h1>UnrestPH System</h1>
        <Router>
          <Route path="/" exact component={Order} />
        </Router>
      </div>
    </div>
  );
}

export default App;
