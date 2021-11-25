import React, { useState, useEffect } from "react";
import EventCard from "./EventCard";

function App() {

  let cards = [1,2,3,4];


  return (
    <div>
      {/* <Navbar tab="events" /> */}
      <ul className={`flex mb-6 mt-4`}>
        <li className={`mr-3`}>
          <div className={`inline-block border rounded py-1 px-3 bg-indigo-900 text-white`} href="/">
            New event
          </div>
        </li>
      </ul>

      <div className={`grid grid-cols-3 gap-4`}>
        {
          cards.map(() => 
            <EventCard name={`Header Prop`} description={`a paragraph`} id={1} />
          )
        }
      </div>

      <footer className={`text-center`}>
      </footer>
    </div>
  );
}

export default App;
