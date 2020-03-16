import React from 'react';
import './App.css';

import { FaLongArrowAltRight, FaLongArrowAltLeft } from 'react-icons/fa';

import SpectrumList from './SpectrumList';

import Spectrum from './spectrum';
// import Output from './output'
// import OutputOld from './output_old'
import OutputMe from './output_me'

function App() {
  return (
    <div className="App">
      <div className="spectrum-wrapper">
        <div className="frequency-scale"><div><FaLongArrowAltLeft /><p>Lower frequencies</p></div><div><p>Higher frequencies</p><FaLongArrowAltRight /></div></div>
        <div className="spectrum">
          {Spectrum.data.map(color => {
            console.log('h', color.h, 's', color.s, 'l', color.l);
            return <div className="spectrum-color" style={{ background: `hsl(${color.h}, ${color.s}%, ${color.l}%)` }} />
          })}
        </div>
      </div>
      {/* <SpectrumList data={Output} /> */}
      <SpectrumList data={OutputMe} />
      {/* <SpectrumList data={OutputOld} /> */}
      
    </div>
  );
}

export default App;
