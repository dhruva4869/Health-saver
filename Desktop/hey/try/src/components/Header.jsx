import React, { useState } from 'react'
import { Link, NavLink } from "react-router-dom";
import { BsFillHouseFill, BsMenuButton } from "react-icons/bs"

function Header() {
  return (
    <header>

        {/* <Link to="/" className='logo'>
            <img src={logo} alt='ReactJS' style={{width:"50px", height: "50px", borderRadius:"50%", backgroundColor:"violet", objectFit:"cover"}} /> AniMan Haven
        </Link> */}
        <nav style={{display:"flex", overflow:"hidden", textOverflow:"ellipsis"}}>
            <NavLink to="/"><BsFillHouseFill size={19} /></NavLink>
            <p style={{ padding: "10px", textAlign: "right" }}>
                <NavLink to="/books"> Books &nbsp;</NavLink>
                <NavLink to="/about"> Explore &nbsp;</NavLink>
                <NavLink to="/info"> Photos &nbsp;</NavLink>
            </p>
            
        </nav>

    </header>
  )
}

export default Header