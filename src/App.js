import React from 'react';
import './App.css';

import { FaLongArrowAltRight, FaLongArrowAltLeft } from 'react-icons/fa';

import SpectrumList from './SpectrumList';
import Spectrum from './spectrum';

import Output from './output'
import OutputOld from './output_old'
import OutputMe from './output_me'

function App() {
  console.log(Spectrum.data)
  return (
    <div className="App">
      <div className="spectrum-wrapper">
        <div className="frequency-scale"><div><FaLongArrowAltLeft /><p>Lower frequencies</p></div><div><p>Higher frequencies</p><FaLongArrowAltRight /></div></div>
        <div className="spectrum">
          {Spectrum.data.map(color => {
            return <div className="spectrum-color" style={{ background: `rgb(${color.r}, ${color.g}, ${color.b})` }} />
          })}
        </div>
      </div>
      <SpectrumList data={Output} />
      <SpectrumList data={OutputMe} />
      <SpectrumList data={OutputOld} />
      
    </div>
  );
}

export default App;
