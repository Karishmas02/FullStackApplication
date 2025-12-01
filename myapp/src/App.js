import React from 'react';
import { BrowserRouter, Routes, Route,Link } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import Dashboard from './Dashboard';

function App() {
  return (
    <BrowserRouter>
    <Link to="/reg">Register</Link>
    <Link to="/login">Login</Link>
    <Link to="/">Dashboard</Link>
      <Routes>
        <Route path='/' element={<Dashboard/>}/>
        <Route path="/reg" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
