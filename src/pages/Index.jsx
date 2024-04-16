import { useEffect, useState } from 'react'
import { MoonLoader } from 'react-spinners';
import Header from '../components/Header/Header';
import Options from '../components/Options/Options';
import MainContent from '../components/MainContent/MainContent';
import Footer from '../components/Footer/Footer';

function Index() {
  document.documentElement.lang = 'es';

  useEffect(() => { 
    document.title = 'QLeon';
    return () => {
      document.title = 'QLeon';
    };
  }, []);

  useEffect(() => {
    const favicon = document.querySelector('link[rel="icon"]');
    favicon.href = 'logo.png';
  }, []); 


  useEffect(() => {
    const metaTag = document.createElement('meta');
    metaTag.setAttribute('name', 'google');
    metaTag.setAttribute('content', 'notranslate');
    document.head.appendChild(metaTag);
    return () => {
      document.head.removeChild(metaTag);
    };
  }, []); 

    const [loading, setLoading] = useState(false);

    useEffect(() => {
      setLoading(true);
      setTimeout(()=>{
        setLoading(false);
      },1300);
    }, [])
    
  
    return (
      <div class = "principal" style={{height:"100vh"}}>
        {
          loading ?(
              <div className='loading-container'>
                <h2>QLeon Project</h2>
                <MoonLoader  color={'#FFFFFF'} aria-label='Qleon Project' loading={loading}/>
              </div>
          ):(
            <>
              <Header/>
              <Options/>
              <MainContent/>
              <Footer/>
            </>
          )
        }
      </div>
    )
}

export default Index