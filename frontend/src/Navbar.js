import logo from './imgs/IrisLogoBetter.png';

function Navbar() {

    return (
        <div className={`relative w-full h-30 mb-10`}>
            <img src={logo} className={`h-30`} alt="Iris Logo" />
            <div className={`mt-8 absolute inset-y-0 right-0`}>
                <a className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`}>
                    New Event +
                </a>
                <a className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`}>
                    Help
                </a>
                <div className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white mr-4`} >
                    About
                </div>
            </div>
            {/* <Link to="/" ><img src={logo} alt="Chia No Code Logo" /></Link> */}
        </div>
    );
}

export default Navbar;