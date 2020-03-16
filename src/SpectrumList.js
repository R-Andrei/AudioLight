import React from 'react';


const Spectrum = ({data}) => (
    <div className="songs">
        {data.data.map(song => {
          const { name, duration, average_frequency, converted_frequency, ahsl, hsl } = song;
          console.log(ahsl, ahsl.h, ahsl.s, ahsl.l);
          return <div className="song">
            <div className="song-header"><h3>{name}</h3></div>

            <div className="description duration"><p>Duration: </p></div>
            <div className="data duration"><p>{duration}</p></div>

            <div className="description average-frequency"><p>Average frequency: </p></div>
            <div className="data average-frequency"><p>{average_frequency}</p></div>

            <div className="description converted-frequency"><p>Converted frequency: </p></div>
            <div className="data converted-frequency"><p>{converted_frequency}</p></div>

            <div className="description average-color"><p>Average color: </p></div>
            <div className="data average-color"><div style={{ background: `hsl(${ahsl.h}, ${ahsl.s}%, ${ahsl.l}%)`}} /></div>

            <div className="song-spectrum">
              {hsl.map(color => {
                return <div className="spectrum-color" style={{ background: `hsl(${color.h}, ${color.s}%, ${color.l}%)` }} />
              })}
            </div>
          </div>
        })}
      </div>
);

export default Spectrum;