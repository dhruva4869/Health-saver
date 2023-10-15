import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from './routes/Home/Home';
import Book from './routes/Books/Book';
import Explore from './routes/Explore/Explore';
import More from './routes/More/More';


function App() {

  return (
    <>
      <div className="no-select-img">
      <Router>
        <Header />
          <Routes>
            <Route path='/' element={<Home /> } />
            <Route path='books' element={<Book />} />
            <Route path='about' element={<Explore />} />
            <Route path='info' element={<More />} />
          </Routes>
        <Footer />
      </Router>
    </div>
    </>
  )
}

export default App
