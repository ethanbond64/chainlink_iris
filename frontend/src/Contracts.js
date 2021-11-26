import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import Contract from "./Contract";

function Contracts() {

    const [contracts, setContracts] = useState([]);

    const { event_id } = useParams();

    useEffect(() => {
        fetch(`http://localhost:8000/get/contracts/${event_id}`, {
            // mode: 'no-cors',
            method: 'GET',
            headers: {
                Accept: 'application/json',
            },
        }).then(response => {
            if (response.ok) {
                response.json().then(json => {
                    console.log(json.contracts);
                    setContracts(json.contracts);
                });
            }
        });
    }, []);

    // Create contracts
    function generateContract(){
        fetch(`http://localhost:8000/new/contract`, {
            // mode: 'no-cors',
            method: 'POST',
            headers: {
                Accept: 'application/json',
            },
        }).then(response => {
            if (response.ok) {
                response.json().then(json => {
                    console.log(json.contracts);
                    setContracts(json.contracts);
                });
            }
        });
    }
    

    return (
        <div className={`mt-4`}>
            <h2 className={`font-semibold font-xxl ml-3`}>Contracts for event # {event_id}</h2>
            <button className={`bg-indigo-700 hover:bg-indigo-900 ml-3 mt-6 mb-4 text-white font-bold py-2 px-4 rounded inline-block`}>
                Generate New Contract
            </button>
            {
                contracts.map(() =>
                    <Contract {...Contract} />
                )
            }
        </div>
    );

}

export default Contracts;