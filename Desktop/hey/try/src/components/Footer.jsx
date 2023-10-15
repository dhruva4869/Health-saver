import React from 'react'
import { BsFacebook, BsGithub, BsLinkedin, BsReddit, BsTwitter } from "react-icons/bs"

function Footer() {
  return (
    <footer style={{padding:"10px"}}>
        &copy; Copyright { new Date().getFullYear() } <br /> <br /> 
        <div style={{display:"inline-flex", alignItems:"center"}}>
          <a href='https://twitter.com/home' target='_blank'><BsTwitter size={30} style={{display:"inline-block", width:"30px", padding:"20px"}} /></a>
          <a href='https://reddit.com' target='_blank'><BsReddit size={30} style={{display:"inline-block", width:"30px", padding:"20px"}}/></a>
          <a href='https://facebook.com' target='_blank'><BsFacebook size={30} style={{display:"inline-block", width:"30px", padding:"20px"}}/></a>
        </div>
    </footer>
  )
}

export default Footer