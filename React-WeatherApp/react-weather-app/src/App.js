import CurrentWeather from './components/current-weather/current-weather';
import './App.css';
import Search from './components/search/search';

function App() {

  const handleOnSearchChange = (searchData) =>{
    const [lat, lon] = searchData.value.split(" "); 
  }


  return (
    <div className="container">
      <Search onSearchChange={handleOnSearchChange} />
      <CurrentWeather />
    </div>
  );
}

export default App;
