import axios from "axios"
import Header from "../components/Header/Header"
import { useEffect, useRef, useState } from "react"
import Showdown from "showdown";
import './Styles/Info.styles.css'
import { MoonLoader } from "react-spinners";
import Footer from "../components/Footer/Footer";


function Info() {
  const converter = new Showdown.Converter();
  const [data, setData] = useState();
  const [loading, setLoading] = useState(false);

  const infoHl = [
    "Tipos de datos",
    "Declaración de variables",
    "Comentarios",
    "Imprimir en pantalla",
    "Operaciones matemáticas básicas",
    "Condicionales",
    "Operadores lógicos y de comparación",
    "Funciones",
    "Ciclos"
  ];
 

  useEffect(() => { 
    fetchMd()
  }, [data]);

  useEffect(() => {
    setLoading(true);
    setTimeout(()=>{
      setLoading(false);
    },1300);
  }, [])

  const url = "https://raw.githubusercontent.com/CodeWarriorEduard/lexer-qleon/main/README.md"

  const fetchMd = () =>{
    axios.get(url)
    .then((response)=>{
      const htmlT = converter.makeHtml(response.data);
      setData(htmlT);
    })
    .catch(error =>{
      console.error(error)
    })
  }


  // const getOffset = (i) =>{
  //   const rect = i.getBoundingClientRect();
  //   return {
  //     left: rect.left + window.scrollX,
  //     top: rect.top + window.scrollY
  //   };
  // }

  const findWord = (e) => {  
    const elements = document.querySelectorAll('.info-data h2, .info-data h3');
    elements.forEach(element => {
      const text = element.innerHTML;
      if (text.includes(e)) {
        const offset = element.getBoundingClientRect();

        window.scrollTo(offset.left + window.scrollX, offset.top-80 + window.scrollY);
      }
    });
  };


  return (
    <div>
      {
        loading? (

          <div className='loading-container' style={{height:"100vh"}}>
          <h2>QLeon Project</h2>
          <MoonLoader  color={'#FFFFFF'} aria-label='Qleon Project' loading={loading}/>
          </div>
  
        ):(
          <div style={{backgroundColor:"#434242", paddingBottom: "20px"}}>
          <Header/>
          <div className=" info-content-container">
            
            <div className=" info-sidebar">
                <ul className="info-sidebar-content">
                {infoHl.map((el, index) => (
                   <li key={index} onClick={()=> findWord(el)}>{el}</li>
                    ))}
                </ul>
            </div>

          <div dangerouslySetInnerHTML={{__html: data}} style={{color:"black"}} className="info-data wrapper"></div>

          </div>
          <Footer/>
        </div>
        )
      }

    </div>
  )
}

export default Info