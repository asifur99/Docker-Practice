import React from 'react';
import axios from 'axios';

import './App.css';

export default class Person extends React.Component {
    state = {
        person: []
    }

    componentDidMount() {
        axios.get('http://localhost:5000/users').then(res => {
            console.log(res.data);
        })
    }

    render() {
        return (
            <div className="App-header2">
                "Person No help"
            </div>
        )
    }
}