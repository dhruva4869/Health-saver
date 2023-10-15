import React from 'react'
import im from "./hm.jpeg"

function Home() {
  return (
    <div>
        <h1 style={{color:"MediumVioletRed"}}> Keshav Gyawali </h1>
        <p> This is for memories of Keshav Gyawali </p>
        <p> Keshav Gyawali was a beloved figure, cherished by all who had the privilege of knowing him. </p>
        <p> His Hobbies were mainly: 
          <ul style={{color:"green"}}>
            <li>Teaching</li>
            <li>Social Work</li>
            <li>Playing Chess</li>
            <li>Reading</li>
            <li>Writing</li>
          </ul>
          <span style={{color:"red"}}>He has also written many books including some novels like <span style={{color:"blue"}}>दाई उपन्यास, रनेनी भौजू |</span> </span>
        </p>
        <img src={im} width="100%" height="300"/>
        <p> He was a social worker at the polictical party <a href='https://cpnuml.org/' target="_blank">UML</a></p>
    </div>
  )
}

export default Home;