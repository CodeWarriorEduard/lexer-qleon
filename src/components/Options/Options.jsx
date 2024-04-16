import './Options.styles.css'
import GitHubIcon from '@mui/icons-material/GitHub';
import InfoIcon from '@mui/icons-material/Info';
import { FormControl, IconButton, InputLabel, MenuItem, Select } from '@mui/material';
import Info from '../../pages/Info';
import { Link } from 'react-router-dom';






function Options() {
  return (
    <div className="options-container">
        <nav className="wrapper options-content">
                <FormControl className='dropdown' size='small' >
                    <InputLabel style={{color:"white"}}>File</InputLabel> {/* Pasar al css */}
                    <Select label="File"  id="file-select" style={{border: "2px solid white"}}>
                        <MenuItem style={{color: "black"}}>Export to ".txt"</MenuItem>
                    </Select>
                </FormControl>
                <div className="options-btn">
                  <a href="https://github.com/CodeWarriorEduard/lexer-qleon/" target='_blank'> {/* Ver si se puede mejorar esta solución*/}
                  <IconButton >
                        <GitHubIcon className='btn-option' style={{ color: 'purple' }} sx={{fontSize:"2.5rem"}}/> 
                  </IconButton>
                  </a>
                  <Link to={"/info"}>
                    <IconButton LinkComponent={Info}>
                        <InfoIcon className='btn-option' sx={{fontSize:"2.5rem"}}/>
                    </IconButton>
                  </Link>
                </div>
        </nav>
    </div>
  )
}

export default Options