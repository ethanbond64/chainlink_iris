import React, { useState, useEffect } from "react";
import EventCard from "./EventCard";

function App() {

  let cards = [1,2,3,4];


  return (
    <div>
      {/* <Navbar tab="events" /> */}


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
