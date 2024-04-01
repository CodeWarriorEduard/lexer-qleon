import logo from "./../../assets/logo2.png";

function Header() {
  return (
    <>
    
    <header>
        <div className="wrapper header-content">
            <img src={logo} alt="project-logo"/>
            <nav>
                <p>INFO</p>
            </nav>
        </div>
    </header>

    </>
  )
}

export default Header