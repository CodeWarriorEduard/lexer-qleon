
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import ClearAllIcon from '@mui/icons-material/ClearAll';
import {IconButton } from '@mui/material';
import './Sidebar.styles.css'


export default function SideBar() {
  return (
    <div className='sidebar-container'>
      <h2>Options</h2>
      <List style={{marginTop: "40px"}}>
          {['Run Code', 'Clear All'].map((text, index) => (
            <ListItem key={text} disablePadding>
              <ListItemButton>
                <ListItemIcon>
                  <IconButton>
                    {index % 2 === 0 ? <PlayCircleIcon color="success" sx={{fontSize: "2.5rem"}}/> : <ClearAllIcon sx={{color:"red", fontSize: "2.5rem"}}/>}
                  </IconButton>
                </ListItemIcon>
                <ListItemText primary={text} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
    </div>
  );
}
