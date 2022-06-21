import logo from './logo.svg';
import './App.css';
import { StyleSheet, css } from 'aphrodite';
import {
  useRecoilState,
  useRecoilValue,
} from 'recoil';
import {deviceListState} from 'atoms'



const MapComponent = (args) => {

  return <></>
}

const DeviceListComponent = (args) => {
  const deviceList = useRecoilValue(deviceListState);

  return <>
    {
      deviceList.devices.map((device) => {
        return <>

        </>
      })
    }
  </>

}

const HorizontalSplit = (args) => {

  return <>
  </>
}

const DeviceInfoPanel = (args) => {

  return <></>
}

const VerticalSplit = (args) => {

  return <></>
}



const AppStyles = StyleSheet.create({

});

function App() {
  return (
    <div className={css(styles.wrapper) + ' App'}>
    </div>
  );
}

export default App;
