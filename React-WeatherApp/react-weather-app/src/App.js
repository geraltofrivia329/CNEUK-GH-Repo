import {useState} from 'react';
import CurrentWeather from './components/current-weather/current-weather';
import './App.css';
import Search from './components/search/search';
import { WEATHER_API_URL, WEATHER_API_KEY } from './api';

function App() {

  const [currentWeather, setCurrentWEather] = useState(null);
  const [forecast, setForecast] = useState(null);


  const handleOnSearchChange = (searchData) =>{
    const [lat, lon] = searchData.value.split(" "); 
    let latitude = lat.replace(/,/g, '');
    let longitude = lon.replace(/,/g, '');

    const currentWeatherFetch = fetch(`${WEATHER_API_URL}/weather?lat={lat}&lon={lon}&appid=${WEATHER_API_KEY}`)
    const forecastFetch = fetch(`${WEATHER_API_URL}/weather?lat={lat}&lon={lon}&appid=${WEATHER_API_KEY}`)

    Promise.all([currentWeatherFetch, forecastFetch])
      .then(async (response) => {
        const weatherResponse = await response[0].json();
        const forecastResponse = await response[1].json();

        setCurrentWEather({city:searchData.label , ...weatherResponse});
        setForecast({city: searchData.label, ...forecastResponse})

      })
      .catch((err) => console.log(err));
  }

  console.log(currentWeather);
  console.log(forecast);
  
  return (
    <div className="container">
      <Search onSearchChange={handleOnSearchChange} />
      {currentWeather && <CurrentWeather data = {currentWeather} />}
    </div>
  );
}

export default App;
