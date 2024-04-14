import axios from 'axios'
import { useState } from 'react'


function MainContent() {
  const url = process.env.BACKEND;
  const [text, setText] = useState('');
  const [output, setOutput] = useState('');

  const updateText = (e) =>{
    const Ntext = e.target.value; //Quito los saltos de linea.
    setText(Ntext);
   
  }

  const run = ()=>{
    axios.post(url, null, {
      params: {
          code: text
      }
  })
    .then (function (response){
      setOutput(() =>{
        return response.data.map((el, index)=>{
          return(
            <>
            
              <p class = "tabLin">{`Line Content ${index+1}:`}</p>
                {el.map((token, idx) =><p class="tabTok" key={idx}>{token}</p>)}
              <br />
            </>
          )
        })
      })
    })

  }
  console.log(text.length)

  return (
        <div className='main-content-container'>
            <div className='wrapper maincontent'>
                <h3>Write Qleon Code Here</h3>
                <button onClick={run} disabled={text.length === 0}>Run Lexer</button>
                <textarea name="qleon-code" id="qleon-code" cols="30" rows="10" onChange={(e)=>(updateText(e))}></textarea>
                <p style={{marginTop:"20px"}}>OUTPUT</p>
                {
                 
                 output.length >0?( // Terminar 
                  <div className="output-terminal">{"LEXEMA:"}
                  <br />
                  <br />
                  {output}
                  </div> 
                  
                  ):(
                  <div className="output-terminal">Please write something before running!</div>     
                  )                 
                }
            </div>
        </div>
  )
}

export default MainContent