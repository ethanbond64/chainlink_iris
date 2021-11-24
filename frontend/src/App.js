import React, { useState, useEffect } from "react";

function App() {
  return (
    <div>
      {/* <Navbar tab="events" /> */}
      <ul className={`flex mb-6 mt-4`}>
        <li className={`mr-3`}>
          <div className={`inline-block border border-blue-500 rounded py-1 px-3 bg-blue-500 text-white`} href="/">
            New event
          </div>
        </li>
      </ul>
      <footer className={`text-center`}>
      </footer>
    </div>
  );
}

export default App;
