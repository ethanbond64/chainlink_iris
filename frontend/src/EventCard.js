import { Link } from "react-router-dom";

function EventCard(props) {


    return (
        <div className={`relative mb-6 p-2.5 rounded shadow-md h-60 bg-gray-100`}>
            <div className={`absolute rounded-t-lg inset-x-0 top-0 p-2.5 bg-indigo-900 text-white font-bold`}>
                {props.name}
            </div>
            {props.description}
            <div class={`absolute rounded-b-lg inset-x-0 bottom-0 p-2.5 bg-white h-14`}>
                <div className={`grid grid-cols-3 gap-4`}>
                    <a className={`inline-block border rounded py-1 px-3 bg-blue-400 text-white`} href={`localhost:8000/stream/${props.id}`}>
                        Stream
                    </a>
                    <a className={`inline-block border rounded py-1 px-3 bg-blue-400 text-white`} href={`localhost:8000/timebox`}>
                        Time Auth
                    </a>
                    <div className={`inline-block border rounded py-1 px-3 bg-blue-400 text-white`} >
                        <Link to={`/contracts/${props.id}`}>Contracts</Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default EventCard;
