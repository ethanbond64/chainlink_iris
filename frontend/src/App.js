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

      <div className={`grid grid-cols-3 gap-4`}>
        <div className={`relative mb-6 p-2.5 rounded shadow-md h-60 bg-gray-100`}>
          <div className={`absolute rounded-t-lg inset-x-0 top-0 p-2.5 bg-indigo-900`}>
            header
          </div>
          <div>
            Description
          </div>
          <div class={`absolute rounded-b-lg inset-x-0 bottom-0 p-2.5 bg-white h-14`}>
            Buttons
          </div>
        </div>
        <div className={`mb-6 p-2.5 rounded shadow-md h-60 bg-gray-100`}>2</div>
        <div className={`mb-6 p-2.5 rounded shadow-md h-60 bg-gray-100`}>3</div>
        <div className={`mb-6 p-2.5 rounded shadow-md h-60 bg-gray-100`}>4</div>
      </div>

      <footer className={`text-center`}>
      </footer>
    </div>
  );
}

export default App;
