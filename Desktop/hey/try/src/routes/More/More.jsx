import React from 'react'
import p1 from "./p1.jpeg"
import p2 from "./p2.jpeg"
import p3 from "./p3.jpeg"
import pt from "./pt.jpeg"
import pm from "./pm.jpeg"
import pmm from "./pmm.jpeg"
import pmmm from "./pmmm.jpeg"



function More() {
  return (
    <div>
      <h1>Photos</h1>
      <div class="two_in_a_row">
        <div class="image-container">
          <img src={p1} alt="Image 1" />
        </div>
        <div class="image-container">
          <img src={p2} alt="Image 2" />
        </div>
      </div>
      <img src={p3} alt='Image 3' style={{borderRadius:"10px", paddingTop:"20px"}}/>
      <img src={pt} alt='Image 3' style={{borderRadius:"10px", paddingTop:"20px", justifyContent:"center"}}/>
      <img src={pmmm} alt='Image 3' style={{borderRadius:"10px", paddingTop:"20px"}}/>

      <div class="two_in_a_row">
        <div class="image-container">
          <img src={pm} alt="Image 1" />
        </div>
        <div class="image-container">
          <img src={pmm} alt="Image 2" />
        </div>
      </div>



    </div>
  )
}

export default More