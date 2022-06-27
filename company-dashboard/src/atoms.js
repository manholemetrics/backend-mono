import {
    atom,
} from 'recoil';

export const deviceListState = atom({
    key: 'textState', // unique ID (with respect to other atoms/selectors)
    default: {
        devices : []
    }, // default value (aka initial value)
});

export const selectedDeviceState = atom({
    key : 'selectedDeviceState',
    default : {

    },
});

export const authState = atom({
    key : 'authState',
    default : {
        token : ''
    }
});