import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './Login'
import Register from './Register'
import Dashboard from './Dashboard'

const Main = () => {
  return (
    <div>

        <BrowserRouter>
        <Routes>
            <Route path='/' element={<Register/>}/>
            <Route path='/log' element={<Login/>}/>
            
            <Route path='/dashboard' element={<Dashboard/>}/>
        </Routes>
        </BrowserRouter>
    </div>
  )
}

export default Main