import logo from './logo.svg';
import './App.css';
import { StyleSheet, css } from 'aphrodite';
import {
  useRecoilState,
  useRecoilValue,
} from 'recoil';
import { deviceListState, authState} from './atoms.js';
import { getRecoil, setRecoil } from "recoil-nexus";

var auth_token = '';

var obj = {
  link: 'http://localhost:8000/token',
  object: {
    method: 'POST',
    headers: {
    },
    body: JSON.stringify({
      'username' : 'test',
      'password' : 'test'
    })
  }
}
fetch(obj.link, obj.object).then(response => setRecoil(authState, {token : response}));

var device_list_manager = {
  get_device_list: function () {
    var obj = {
      link: 'http://localhost:8001/devices',
      object: {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + getRecoil(authState).token,
          'Host': 'localhost:8001'
        }
      }
    }
    fetch(obj.link, obj)
    .then(response => {console.log('error'); console.log(response);})
      .then(response => response.json())
      .then(data => console.log(data));
  }
}

const MapComponent = (args) => {

  return <></>
}

const DeviceListComponent = (args) => {
  const deviceList = useRecoilValue(deviceListState);

  return <>
    {
      deviceList.devices.map((device) => {
        return <>
          <p>device.device_id</p>
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
  device_list_manager.get_device_list();
  return (
    <div className={css(AppStyles) + ' App'}>
    </div>
  );
}

export default App;
