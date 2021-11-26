import React, { useState, useEffect } from "react";
import EventCard from "./EventCard";

function App() {

  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/get/events", {
      // mode: 'no-cors',
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    }).then(response => {
      if (response.ok) {
        response.json().then(json => {
          console.log(json.events);
          setEvents(json.events);
        });
      }
    });
  }, []);

  return (
    <div>
      <div className={`grid grid-cols-3 gap-4`}>
        {events.map((event) => 
            <EventCard name={event.name} description={event.about} id={event.id} />
        )}
      </div>
      <footer className={`text-center`}>
      </footer>
    </div>
  );
}

export default App;
