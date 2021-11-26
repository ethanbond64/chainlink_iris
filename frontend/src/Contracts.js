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
    

    return (
        <div className={`mt-4`}>
            <div>Contracts for event # {event_id}</div>
            {
                contracts.map(() =>
                    <Contract {...Contract} />
                )
            }
        </div>
    );

}

export default Contracts;