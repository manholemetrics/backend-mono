import {
    atom,
} from 'recoil';

const deviceListState = atom({
    key: 'textState', // unique ID (with respect to other atoms/selectors)
    default: {
        devices : []
    }, // default value (aka initial value)
});

const selectedDeviceState = atom({
    key : 'selectedDeviceState',
    default : {

    },
})