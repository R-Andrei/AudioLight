import React from 'react';
import './styles/App.css';

import { FaLongArrowAltRight, FaLongArrowAltLeft } from 'react-icons/fa';

import SpectrumList from './components/SpectrumList';

import Spectrum from './output/spectrum';
import Output from './output/output'

function App() {
  return (
    <div className="App">
      <div className="spectrum-wrapper">
        <div className="frequency-scale"><div><FaLongArrowAltLeft /><p>Lower frequencies</p></div><div><p>Higher frequencies</p><FaLongArrowAltRight /></div></div>
        <div className="spectrum">
          {Spectrum.data.map(color => {
            return <div className="spectrum-color" style={{ background: `hsl(${color.h}, ${color.s}%, ${color.l}%)`}} />
          })}
        </div>
      </div>
      <SpectrumList data={Output} />
    </div>
  );
}

export default App;
