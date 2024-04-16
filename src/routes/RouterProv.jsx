import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Index from '../pages/Index';
import Info from '../pages/Info';


function RouterProv(){
    
    const routes = createBrowserRouter([
        {path:"/",
        Component:Index,
        },
        {path:"/info",
        Component:Info,
        },
    ]);
    
    return(
       <RouterProvider router={routes}></RouterProvider>
    )
}


export default RouterProv