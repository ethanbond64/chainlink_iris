
function EventForm(){

    return (
        <div className={`mx-auto h-screen`}>
            <div className={`bg-gray-50 m-auto p-2.5 w-3/4 rounded shadow-md container h-screen`} >
                <div className={`h-30 mt-4 mb-4`} >
                    <input className={`w-1/6 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block`}
                        placeholder="Event Name" />
                    <button className={`bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded float-right inline-block`} >
                        Save
                    </button>
                </div>
                <textarea class="m-auto mt-4 mb-4 w-5/6 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none" rows="4"
                    placeholder="Event Description">
                </textarea>

                <h2 className={`font-semibold font-3xl`}>Start and End Dates</h2>
                <div className={`h-30 mt-4 mb-4`} >
                    <input className={`w-1/3 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block mr-6`} 
                        type="datetime-local" id="meeting-time"
                        name="meeting-time" value="2018-06-12T19:30" />
                    <input className={`w-1/3 float-left shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline inline-block mr-6`}
                        type="datetime-local" id="meeting-time"
                        name="meeting-time" value="2018-06-12T19:30" />
                </div>
                <br />
                <br />
                
                <h2 className={`font-semibold font-3xl`}>Data Policy</h2>
                <div>
                    <div class="mt-2">
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 1"/>
                                <span class="ml-2">Policy 1</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 2" />
                                <span class="ml-2">Policy 2</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="policy 3" />
                                <span class="ml-2">Policy 3</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="checkbox" class="form-checkbox" value="Custom" />
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