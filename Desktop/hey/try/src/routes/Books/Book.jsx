import React from 'react'
import imm from "./book1.png"

function Book() {
  return (
    <div>
      <h1>दाई उपन्यास </h1>
      <div style={{ display: 'flex', justifyContent:"center" }}>
      <img src={imm} width="70%" height={500} style={{ borderRadius: '5px' }} />
      <br/>
      <p style={{paddingLeft:"5%"}}><button><a href='https://drive.google.com/file/d/1cj5GYhUSx7XZHmz2M9kMVHudFXq46_i1/view?usp=sharing' target='_blank' style={{cursor:"pointer"}}>Click Here to download</a></button></p>
      <br/><br/><br/>
      </div>
      <br/><br/>
    </div>
  )
}

export default Book