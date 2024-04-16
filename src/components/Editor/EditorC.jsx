import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import ClearAllIcon from '@mui/icons-material/ClearAll';
import {IconButton } from '@mui/material';
import './Sidebar.styles.css'
import Editor, {loader} from '@monaco-editor/react';
import './Editor.styles.css'
import { Box, Tab } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';



function EditorC() {

  const [text, setText] = useState('');
  const [output, setOutput] = useState('');
  const url = process.env.BACKEND;

  loader.init().then((monaco) =>{
    monaco.editor.defineTheme("qleon", {
      base: "vs",
      inherit: true,
      rules: [],
      colors: {
        "editor.foreground": "#CCCCCC", // Color del texto
        "editor.background": "#FFFF", // Color de fondo del editor
        "editorCursor.foreground": "#F3EFE0", // Color del cursor
        "editor.lineHighlightBackground": "#333333", // Color de fondo para la línea resaltada
        "editorLineNumber.foreground": "#FFFFFF", // Color de los números de línea
        "editor.selectionBackground": "#666666", // Color de fondo para la selección activa
        "editor.inactiveSelectionBackground": "#666666", // Color de fondo para la selección inactiva
      },
    });
    monaco.editor.setTheme("qleon");
  })

  const run = ()=>{
    console.log("Gola")
    axios.post(url, null, {
      params: {
          code: text
      }
  })
      .then(function (response) {
        console.log(response)
        setOutput(() => {
          return response.data.map((el, index) => {
            return (
              <>
                <p className="tabLin">{`Content of Line ${index + 1}:`}</p>
                {
                  el.length > 0 ? el.map((token, idx) => (<p className="tabTok" key={idx}> {token}</p>)) :
                  <p className="tabTok">Line Empty </p>
                }
                <br />
              </>
            )
          })
        })
      })
  }

  const handleEditorChange = (value) =>{
    const Ntext = value; //Quito los saltos de linea.
    setText(Ntext);
  }



  return (
    <div className='main-content'>

    <div className='sidebar-container'>
          <h2>Options</h2>
          <List style={{marginTop: "40px"}}>
              {['Run Code'].map((text, index) => (
                <ListItem key={text} disablePadding>
                  <ListItemButton onClick={run}>
                    <ListItemIcon >
                      <IconButton >
                        {<PlayCircleIcon sx={{fontSize: "2.5rem"}} className='run-btn'/>}
                      </IconButton>
                    </ListItemIcon>
                    <ListItemText primary={text} />
                  </ListItemButton>
                </ListItem>
              ))}
            </List>
        </div>

      <div className='et-container'>
            <div className='editor-container grid-el'>
            <Box>
              <Tab label="Qleon Code" style={{backgroundColor:"#222222", borderTopLeftRadius: "10px", color:"white"}}/>
            </Box>
            <Editor height="60vh" width="autosize"theme='qleon' onChange={handleEditorChange}/>
            </div>
            <div className='terminal-container grid-el'>
              <Box>
                <Tab label="Output" style={{backgroundColor:"#222222", borderTopLeftRadius: "10px", color:"white"}}/>
              </Box>
              {       
                output.length >0?( // Terminar 
                <div className="terminal-impl">{"LEXEMA:"}
                <br />
                <br />
                {output}
                </div> 
                
                ):(
                <div className="terminal-impl">Please write something before running!</div>     
                )                 
              }     
      </div>
    </div>

    </div>
  )
}

export default EditorC