import { Box} from "@mui/material"
import EditorC from "../Editor/EditorC"
import './MainContent.styles.css'

function MainContent() {
  return (
    <Box sx={{display: "flex", height: "88vh"}}>
      <EditorC/>
    </Box>
  )
}

export default MainContent