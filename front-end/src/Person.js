import React from 'react';
import axios from 'axios';

import './App.css';

export default class Person extends React.Component {
    state = {
        person: []
    }

    componentDidMount() {
        axios.get('http://localhost:5000/users').then(res => {
            this.person = res.data.data;
        })
    }

    render() {
        return (
            <div className="App-header2">
                Random Person is: {this.person[Math.random() * 5]}
            </div>
        )
    }
}