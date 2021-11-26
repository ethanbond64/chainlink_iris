
function Contract(props) {

    return (
        <div className={`mb-6 p-2.5 rounded shadow-md w-full`}>
            {/* <img src={coinIcon} alt="Coin icon" className={`inline mt-1 align-top`} /> */}
            <div className={`ml-4 inline-block`}>
                <span className="font-semibold" >Name: </span>
                <br />
                <span className="font-semibold">Puzzlehash: </span>
                <br />
                <span className="font-semibold">Address: </span>
                <br />
                <span className="font-semibold">Created On: </span>
                <br />
                <span className="font-semibold">Amount: </span>
            </div>
            <div className={`ml-4 inline-block`}>
                <span>{props.name}</span>
                <br />
                <span></span>
                <br />
                <span></span>
                <br />
                <span>{props.created_on}</span>
                <br />
                <span></span>
            </div>
            <button className={`bg-red-500 hover:bg-red-700 ml-3 mt-6 text-white font-bold py-2 px-4 rounded float-right inline-block`}>
                Delete
            </button>
            <button className={`bg-indigo-700 hover:bg-indigo-900 ml-3 mt-6 text-white font-bold py-2 px-4 rounded float-right inline-block`}>
                View Source
            </button>
            <button className={`bg-indigo-700 hover:bg-indigo-900 ml-3 mt-6 text-white font-bold py-2 px-4 rounded float-right inline-block`}>
                Deploy
            </button>

        </div>
    );
}


export default Contract;