import { render } from '@testing-library/react';
import React, { Component } from 'react';
import ChartComponent from './ChartComponent'
import axios from 'axios';
import {Line, line, Scatter} from 'react-chartjs-2';
const API_URL = 'http://localhost:8000';


export default class Graph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            chart:null,
            data:[], 
            isLoaded: false};
        this.getCountry = this.getCountry.bind(this);

    }

    getCountry(countryName) {
        this.setState({isLoading: true});

        const url = `${API_URL}/api/get-country/`;
        const data = {country:countryName};
        console.log("about ot make request");
        axios.post(url, data).then(response => this.setState({data: response.data, isLoaded: true}));
    }
    componentDidMount() {
        this.getCountry('China');


    }
    render() {
        if (!this.state.isLoaded) {
            return <p>Loading the state</p>;
        }
        var temp = this.state.data;
        //console.log(temp.data[0]);
        var test = [0, 1, 2, 3];
        //console.log(test);
        return (<ChartComponent chartData={temp} />);
                //return (<ChartComponent chartData = {this.state.data}/>);
    }
}