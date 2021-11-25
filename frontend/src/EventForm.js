import React, { useState } from "react";
import { Link } from "react-router-dom";


function deepCopy(obj) {
    return JSON.parse(JSON.stringify(obj));
}

function convertDate(date) {
    date.setMinutes(date.getMinutes() - date.getTimezoneOffset());
    return date.toISOString().slice(0, -1);
}

function addHours(date,x) {
    date.setHours(date.getHours() + x);
    return date;
}

function EventForm(){
    const now = new Date();

    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [start, setStart] = useState(convertDate(now));
    const [end, setEnd] = useState(convertDate(addHours(now,3)));
    const [dataPolicy, setDataPolicy] = useState([]);

    function onChangeName(e) {
        setName(e.target.value);
    }

    function onChangeDescription(e) {
        setDescription(e.target.value);
    }

    function onChangeStart(e) {
        setStart(e.target.value);
    }

    function onChangeEnd(e) {
        setEnd(e.target.value);
    }


    function onChangePolicy(e) {

        console.log(e.target.checked);
        console.log(e.target.value);
        let policyCopy = deepCopy(dataPolicy);

        if (e.target.checked) {
            policyCopy.push(e.target.value);

        } else {
            let index = policyCopy.indexOf(e.target.value);
            if (index > -1) {
                policyCopy.splice(index, 1);
            }
        }

        setDataPolicy(policyCopy);

    }

    function saveEvent() {
        console.log("name: ", name);
        console.log("desc: ",description);
        console.log("start: ", start);
        console.log("end: ", end);
        console.log("policy: ",dataPolicy);
    }

    return (
        <div className={`mx-auto h-screen`}>
            <div className={`bg-gray-50 m-auto p-2.5 w-3/4 rounded shadow-md container h-screen`} >
                <div className={`h-30 mt-4 mb-4`} >
                    <input className={`w-1/6 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block`}
                        placeholder="Event Name" onChange={onChangeName} />
                    <button className={`bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded float-right inline-block`} 
                        onClick={saveEvent} >
                        <Link to="/" onClick={saveEvent} >Save</Link>
                    </button>
                </div>
                <textarea class="m-auto mt-4 mb-4 w-5/6 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none" rows="4"
                    placeholder="Event Description" onChange={onChangeDescription}>
                </textarea>

                <h2 className={`font-semibold font-3xl`}>Start and End Dates</h2>
                <div className={`h-30 mt-4 mb-4`} >
                    <input className={`w-1/3 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block mr-6`} 
                        type="datetime-local" value={start} onChange={onChangeStart} />
                    <input className={`w-1/3 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block mr-6`}
                        type="datetime-local" value={end} onChange={onChangeEnd} />
                </div>
                <br />
                <br />
                
                <h2 className={`font-semibold font-3xl`}>Data Policy</h2>
                <div>
                    <div class="mt-2">
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 1" onChange={onChangePolicy} />
                                <span class="ml-2">Policy 1</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 2" onChange={onChangePolicy} />
                                <span class="ml-2">Policy 2</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 3" onChange={onChangePolicy} />
                                <span class="ml-2">Policy 3</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="Custom" onChange={onChangePolicy} />
                                <span class="ml-2">Custom</span>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default EventForm;