import { render } from '@testing-library/react';
import React, { Component } from 'react';
import ChartComponent from './ChartComponent'
import axios from 'axios';
import moment from 'moment';
import Select from 'react-select';
import ToggleButton from 'react-bootstrap/ToggleButton'
import Dropdown from 'react-bootstrap/Dropdown'
import DropdownButton from 'react-bootstrap/DropdownButton'
import 'bootstrap/dist/css/bootstrap.min.css';

import {Line, line, Scatter} from 'react-chartjs-2';
import { useParams } from "react-router-dom"
const API_URL = 'https://ec2-3-17-109-193.us-east-2.compute.amazonaws.com:8000';





export default class Graph extends React.Component {
    constructor(props) {
        super(props);
        this.selectedRef = React.createRef();
        this.state = {
            case : null,
            death : null,
	    open : null,
            low : null,
	    selectedSymbol : null,
	    symbolOptions : [
		{'label': 'SPY', 'value': 'SPY'}
	    ],
	    selectedName : null,
            options: [
                {'label': 'Afghanistan', 'value': 'Afghanistan'}, {'label': 'Albania', 'value': 'Albania'}, {'label': 'Algeria', 'value': 'Algeria'}, {'label': 'Andorra', 'value': 'Andorra'}, {'label': 'Angola', 'value': 'Angola'}, {'label': 'Antigua and Barbuda', 'value': 'Antigua and Barbuda'}, {'label': 'Argentina', 'value': 'Argentina'}, {'label': 'Armenia', 'value': 'Armenia'}, {'label': 'Australia', 'value': 'Australia'}, {'label': 'Austria', 'value': 'Austria'}, {'label': 'Azerbaijan', 'value': 'Azerbaijan'}, {'label': 'Bahamas', 'value': 'Bahamas'}, {'label': 'Bahrain', 'value': 'Bahrain'}, {'label': 'Bangladesh', 'value': 'Bangladesh'}, {'label': 'Barbados', 'value': 'Barbados'}, {'label': 'Belarus', 'value': 'Belarus'}, {'label': 'Belgium', 'value': 'Belgium'}, {'label': 'Belize', 'value': 'Belize'}, {'label': 'Benin', 'value': 'Benin'}, {'label': 'Bhutan', 'value': 'Bhutan'}, {'label': 'Bolivia', 'value': 'Bolivia'}, {'label': 'Bosnia and Herzegovina', 'value': 'Bosnia and Herzegovina'}, {'label': 'Botswana', 'value': 'Botswana'}, {'label': 'Brazil', 'value': 'Brazil'}, {'label': 'Brunei', 'value': 'Brunei'}, {'label': 'Bulgaria', 'value': 'Bulgaria'}, {'label': 'Burkina Faso', 'value': 'Burkina Faso'}, {'label': 'Burma', 'value': 'Burma'}, {'label': 'Burundi', 'value': 'Burundi'}, {'label': 'Cabo Verde', 'value': 'Cabo Verde'}, {'label': 'Cambodia', 'value': 'Cambodia'}, {'label': 'Cameroon', 'value': 'Cameroon'}, {'label': 'Canada', 'value': 'Canada'}, {'label': 'Central African Republic', 'value': 'Central African Republic'}, {'label': 'Chad', 'value': 'Chad'}, {'label': 'Chile', 'value': 'Chile'}, {'label': 'China', 'value': 'China'}, {'label': 'Colombia', 'value': 'Colombia'}, {'label': 'Comoros', 'value': 'Comoros'}, {'label': 'Congo (Brazzaville)', 'value': 'Congo (Brazzaville)'}, {'label': 'Congo (Kinshasa)', 'value': 'Congo (Kinshasa)'}, {'label': 'Costa Rica', 'value': 'Costa Rica'}, {'label': "Cote d'Ivoire", 'value': "Cote d'Ivoire"}, {'label': 'Croatia', 'value': 'Croatia'}, {'label': 'Cuba', 'value': 'Cuba'}, {'label': 'Cyprus', 'value': 'Cyprus'}, {'label': 'Czechia', 'value': 'Czechia'}, {'label': 'Denmark', 'value': 'Denmark'}, {'label': 'Diamond Princess', 'value': 'Diamond Princess'}, {'label': 'Djibouti', 'value': 'Djibouti'}, {'label': 'Dominica', 'value': 'Dominica'}, {'label': 'Dominican Republic', 'value': 'Dominican Republic'}, {'label': 'Ecuador', 'value': 'Ecuador'}, {'label': 'Egypt', 'value': 'Egypt'}, {'label': 'El Salvador', 'value': 'El Salvador'}, {'label': 'Equatorial Guinea', 'value': 'Equatorial Guinea'}, {'label': 'Eritrea', 'value': 'Eritrea'}, {'label': 'Estonia', 'value': 'Estonia'}, {'label': 'Eswatini', 'value': 'Eswatini'}, {'label': 'Ethiopia', 'value': 'Ethiopia'}, {'label': 'Fiji', 'value': 'Fiji'}, {'label': 'Finland', 'value': 'Finland'}, {'label': 'France', 'value': 'France'}, {'label': 'Gabon', 'value': 'Gabon'}, {'label': 'Gambia', 'value': 'Gambia'}, {'label': 'Georgia', 'value': 'Georgia'}, {'label': 'Germany', 'value': 'Germany'}, {'label': 'Ghana', 'value': 'Ghana'}, {'label': 'Greece', 'value': 'Greece'}, {'label': 'Grenada', 'value': 'Grenada'}, {'label': 'Guatemala', 'value': 'Guatemala'}, {'label': 'Guinea', 'value': 'Guinea'}, {'label': 'Guinea-Bissau', 'value': 'Guinea-Bissau'}, {'label': 'Guyana', 'value': 'Guyana'}, {'label': 'Haiti', 'value': 'Haiti'}, {'label': 'Holy See', 'value': 'Holy See'}, {'label': 'Honduras', 'value': 'Honduras'}, {'label': 'Hungary', 'value': 'Hungary'}, {'label': 'Iceland', 'value': 'Iceland'}, {'label': 'India', 'value': 'India'}, {'label': 'Indonesia', 'value': 'Indonesia'}, {'label': 'Iran', 'value': 'Iran'}, {'label': 'Iraq', 'value': 'Iraq'}, {'label': 'Ireland', 'value': 'Ireland'}, {'label': 'Israel', 'value': 'Israel'}, {'label': 'Italy', 'value': 'Italy'}, {'label': 'Jamaica', 'value': 'Jamaica'}, {'label': 'Japan', 'value': 'Japan'}, {'label': 'Jordan', 'value': 'Jordan'}, {'label': 'Kazakhstan', 'value': 'Kazakhstan'}, {'label': 'Kenya', 'value': 'Kenya'}, {'label': 'Korea. South', 'value': 'Korea. South'}, {'label': 'Kosovo', 'value': 'Kosovo'}, {'label': 'Kuwait', 'value': 'Kuwait'}, {'label': 'Kyrgyzstan', 'value': 'Kyrgyzstan'}, {'label': 'Laos', 'value': 'Laos'}, {'label': 'Latvia', 'value': 'Latvia'}, {'label': 'Lebanon', 'value': 'Lebanon'}, {'label': 'Lesotho', 'value': 'Lesotho'}, {'label': 'Liberia', 'value': 'Liberia'}, {'label': 'Libya', 'value': 'Libya'}, {'label': 'Liechtenstein', 'value': 'Liechtenstein'}, {'label': 'Lithuania', 'value': 'Lithuania'}, {'label': 'Luxembourg', 'value': 'Luxembourg'}, {'label': 'MS Zaandam', 'value': 'MS Zaandam'}, {'label': 'Madagascar', 'value': 'Madagascar'}, {'label': 'Malawi', 'value': 'Malawi'}, {'label': 'Malaysia', 'value': 'Malaysia'}, {'label': 'Maldives', 'value': 'Maldives'}, {'label': 'Mali', 'value': 'Mali'}, {'label': 'Malta', 'value': 'Malta'}, {'label': 'Marshall Islands', 'value': 'Marshall Islands'}, {'label': 'Mauritania', 'value': 'Mauritania'}, {'label': 'Mauritius', 'value': 'Mauritius'}, {'label': 'Mexico', 'value': 'Mexico'}, {'label': 'Moldova', 'value': 'Moldova'}, {'label': 'Monaco', 'value': 'Monaco'}, {'label': 'Mongolia', 'value': 'Mongolia'}, {'label': 'Montenegro', 'value': 'Montenegro'}, {'label': 'Morocco', 'value': 'Morocco'}, {'label': 'Mozambique', 'value': 'Mozambique'}, {'label': 'Namibia', 'value': 'Namibia'}, {'label': 'Nepal', 'value': 'Nepal'}, {'label': 'Netherlands', 'value': 'Netherlands'}, {'label': 'New Zealand', 'value': 'New Zealand'}, {'label': 'Nicaragua', 'value': 'Nicaragua'}, {'label': 'Niger', 'value': 'Niger'}, {'label': 'Nigeria', 'value': 'Nigeria'}, {'label': 'North Macedonia', 'value': 'North Macedonia'}, {'label': 'Norway', 'value': 'Norway'}, {'label': 'Oman', 'value': 'Oman'}, {'label': 'Pakistan', 'value': 'Pakistan'}, {'label': 'Panama', 'value': 'Panama'}, {'label': 'Papua New Guinea', 'value': 'Papua New Guinea'}, {'label': 'Paraguay', 'value': 'Paraguay'}, {'label': 'Peru', 'value': 'Peru'}, {'label': 'Philippines', 'value': 'Philippines'}, {'label': 'Poland', 'value': 'Poland'}, {'label': 'Portugal', 'value': 'Portugal'}, {'label': 'Qatar', 'value': 'Qatar'}, {'label': 'Romania', 'value': 'Romania'}, {'label': 'Russia', 'value': 'Russia'}, {'label': 'Rwanda', 'value': 'Rwanda'}, {'label': 'Saint Kitts and Nevis', 'value': 'Saint Kitts and Nevis'}, {'label': 'Saint Lucia', 'value': 'Saint Lucia'}, {'label': 'Saint Vincent and the Grenadines', 'value': 'Saint Vincent and the Grenadines'}, {'label': 'Samoa', 'value': 'Samoa'}, {'label': 'San Marino', 'value': 'San Marino'}, {'label': 'Sao Tome and Principe', 'value': 'Sao Tome and Principe'}, {'label': 'Saudi Arabia', 'value': 'Saudi Arabia'}, {'label': 'Senegal', 'value': 'Senegal'}, {'label': 'Serbia', 'value': 'Serbia'}, {'label': 'Seychelles', 'value': 'Seychelles'}, {'label': 'Sierra Leone', 'value': 'Sierra Leone'}, {'label': 'Singapore', 'value': 'Singapore'}, {'label': 'Slovakia', 'value': 'Slovakia'}, {'label': 'Slovenia', 'value': 'Slovenia'}, {'label': 'Solomon Islands', 'value': 'Solomon Islands'}, {'label': 'Somalia', 'value': 'Somalia'}, {'label': 'South Africa', 'value': 'South Africa'}, {'label': 'South Sudan', 'value': 'South Sudan'}, {'label': 'Spain', 'value': 'Spain'}, {'label': 'Sri Lanka', 'value': 'Sri Lanka'}, {'label': 'Sudan', 'value': 'Sudan'}, {'label': 'Suriname', 'value': 'Suriname'}, {'label': 'Sweden', 'value': 'Sweden'}, {'label': 'Switzerland', 'value': 'Switzerland'}, {'label': 'Syria', 'value': 'Syria'}, {'label': 'Taiwan*', 'value': 'Taiwan*'}, {'label': 'Tajikistan', 'value': 'Tajikistan'}, {'label': 'Tanzania', 'value': 'Tanzania'}, {'label': 'Thailand', 'value': 'Thailand'}, {'label': 'Timor-Leste', 'value': 'Timor-Leste'}, {'label': 'Togo', 'value': 'Togo'}, {'label': 'Trinidad and Tobago', 'value': 'Trinidad and Tobago'}, {'label': 'Tunisia', 'value': 'Tunisia'}, {'label': 'Turkey', 'value': 'Turkey'}, {'label': 'Uganda', 'value': 'Uganda'}, {'label': 'Ukraine', 'value': 'Ukraine'}, {'label': 'United Arab Emirates', 'value': 'United Arab Emirates'}, {'label': 'United Kingdom', 'value': 'United Kingdom'}, {'label': 'Uruguay', 'value': 'Uruguay'}, {'label': 'Uzbekistan', 'value': 'Uzbekistan'}, {'label': 'Vanuatu', 'value': 'Vanuatu'}, {'label': 'Venezuela', 'value': 'Venezuela'}, {'label': 'Vietnam', 'value': 'Vietnam'}, {'label': 'West Bank and Gaza', 'value': 'West Bank and Gaza'}, {'label': 'Yemen', 'value': 'Yemen'}, {'label': 'Zambia', 'value': 'Zambia'}, {'label': 'Zimbabwe', 'value': 'Zimbabwe'}, {'label': 'US', 'value': 'US'}, {'label': 'Cruise Ship', 'value': 'Cruise Ship'}, {'label': 'Guadeloupe', 'value': 'Guadeloupe'}, {'label': 'Reunion', 'value': 'Reunion'}, {'label': 'Martinique', 'value': 'Martinique'}, {'label': 'French Guiana', 'value': 'French Guiana'}, {'label': 'Mayotte', 'value': 'Mayotte'}, {'label': 'Bahamas. The', 'value': 'Bahamas. The'}, {'label': 'Cape Verde', 'value': 'Cape Verde'}, {'label': 'East Timor', 'value': 'East Timor'}, {'label': 'Gambia. The', 'value': 'Gambia. The'}, {'label': 'Greenland', 'value': 'Greenland'}, {'label': 'Guam', 'value': 'Guam'}, {'label': 'Guernsey', 'value': 'Guernsey'}, {'label': 'Jersey', 'value': 'Jersey'}, {'label': 'Puerto Rico', 'value': 'Puerto Rico'}, {'label': 'Republic of the Congo', 'value': 'Republic of the Congo'}, {'label': 'The Bahamas', 'value': 'The Bahamas'}, {'label': 'The Gambia', 'value': 'The Gambia'}, {'label': 'Aruba', 'value': 'Aruba'}, {'label': 'occupied Palestinian territory', 'value': 'occupied Palestinian territory'}, {'label': 'Cayman Islands', 'value': 'Cayman Islands'}, {'label': 'Curacao', 'value': 'Curacao'}, {'label': 'Mainland China', 'value': 'Mainland China'}, {'label': 'Iran (Islamic Republic of)', 'value': 'Iran (Islamic Republic of)'}, {'label': 'Republic of Korea', 'value': 'Republic of Korea'}, {'label': 'Others', 'value': 'Others'}, {'label': 'UK', 'value': 'UK'}, {'label': 'Hong Kong SAR', 'value': 'Hong Kong SAR'}, {'label': 'Taipei and environs', 'value': 'Taipei and environs'}, {'label': 'Czech Republic', 'value': 'Czech Republic'}, {'label': 'Viet Nam', 'value': 'Viet Nam'}, {'label': 'Macao SAR', 'value': 'Macao SAR'}, {'label': 'Russian Federation', 'value': 'Russian Federation'}, {'label': 'Republic of Moldova', 'value': 'Republic of Moldova'}, {'label': 'Faroe Islands', 'value': 'Faroe Islands'}, {'label': 'Saint Martin', 'value': 'Saint Martin'}, {'label': 'Channel Islands', 'value': 'Channel Islands'}, {'label': 'Gibraltar', 'value': 'Gibraltar'}, {'label': 'Saint Barthelemy', 'value': 'Saint Barthelemy'}, {'label': 'South Korea', 'value': 'South Korea'}, {'label': 'Hong Kong', 'value': 'Hong Kong'}, {'label': 'Taiwan', 'value': 'Taiwan'}, {'label': 'Palestine', 'value': 'Palestine'}, {'label': 'Macau', 'value': 'Macau'}, {'label': 'St. Martin', 'value': 'St. Martin'}, {'label': 'Vatican City', 'value': 'Vatican City'}, {'label': 'Republic of Ireland', 'value': 'Republic of Ireland'}, {'label': ' Azerbaijan', 'value': ' Azerbaijan'}, {'label': 'North Ireland', 'value': 'North Ireland'}, {'label': 'Ivory Coast', 'value': 'Ivory Coast'}
                
              ],
            countryParam: null,
            chart:null,
            data:[], 
	    stockRawData:[],
            isLoaded: false};
        this.getCountry = this.getCountry.bind(this);
        this.handleChange = this.handleChange.bind(this);
	this.handleStockChange = this.handleStockChange.bind(this);

    }
    
    handleChange (e) {
        this.setState({ selectedName : e.value}, () => {
            //console.log("hi" +this.state.selectedName);
            this.getCountry(this.state.selectedName, this.state.selectedSymbol);
        });
         //this prints the selected option
      }
    handleStockChange (e) {
	this.setState({ selectedSymbol : e.value}, () => {
	    this.getCountry(this.state.selectedName, this.state.selectedSymbol);
	});
    }
    convToPointCase(val) {
        var json = []
        var temp = val;
        var reduced = temp.reduce(function(allDates, date) {
            if (allDates.some(function(e) {
                return e.date === date.date
              })) {
              allDates.filter(function(e) {
                return e.date === date.date
              })
              [0].cases += + date.cases
            } else {
              allDates.push({
                date: date.date,
                cases: +date.cases
              })
            }
            return allDates
        }, []);
        for (var j = 0; j < reduced.length; j++) {
            var jsonObj = {x: moment(reduced[j].date), y: reduced[j].cases};
            json.push(jsonObj);
        }
        return json
        this.setState( {
            chart: {
                datasets: [
                    {
                        label: 'stats',
                        data: json,
                        pointBackgroundColor: "rgba(0,0,0)",
                    }
                ]
            },
        })
     
    }
    convToPointDeath(val) {
        var json = [];
        var temp = val;
        var reduced = temp.reduce(function(allDates, date) {
            if (allDates.some(function(e) {
                return e.date === date.date
              })) {
              allDates.filter(function(e) {
                return e.date === date.date
              })
              [0].deaths += + date.deaths
            } else {
              allDates.push({
                date: date.date,
                deaths: +date.deaths
              })
            }
            return allDates
        }, []);
        for (var j = 0; j < reduced.length; j++) {
            var jsonObj = {x: moment(reduced[j].date), y: reduced[j].deaths};
            json.push(jsonObj);
        }
        console.log(json);
        return(json)
        this.setState( {
            chart: {
                datasets: [
                    {
                        label: 'stats',
                        data: json,
                        pointBackgroundColor: "rgba(0,0,0)",
                    }
                ]
            },
        })
     
    }
    convPointStock(val, dtype) {
	var json = [];
	for (var i = 0; i<val.length; i++) {
	    json.push({x: moment(val[i].date), y: val[i][dtype]});
	}
	return(json)
    }

    getCountry(countryName, symbolName) {
        this.setState({isLoading: true});

        const url = `${API_URL}/api/get-country/`;
        const data = {country:countryName, symbol:symbolName};
        axios.post(url, data).then(response => this.setState({data: response.data.covid_data, stockRawData: response.data.stock_data, isLoaded: true}, () => {
	    //console.log(response.data.stock_data);
            //console.log(this.state.stockRawData);
	    var openData = this.convPointStock(this.state.stockRawData, "open");
	    console.log(openData);
	    var closeData = this.convPointStock(this.state.stockRawData, "close");
	    //var closeData = this.state.stockRawData.close;
	    console.log(this.state.stockRawData);
            var deathData = this.convToPointDeath(this.state.data);
            var caseData = this.convToPointCase(this.state.data);
            this.setState( {
                chart: {
                    datasets: [
                        {
                            label: 'cases',
                            data: caseData,
                            pointBackgroundColor: "rgba(0,0,0)",
                        },
                        {
                            label: 'deaths',
                            data: deathData,
                            pointBackgroundColor: "rgba(0,0,0)",
                        },
			{
			    label: 'open',
			    data: openData,
			    pointBackgroundColor: "rgba(0,0,0)",
			},
			{
			    label: 'close',
			    data: closeData,
	                    pointBackgroundColor: "rgba(0,0,0)",
			}
                    ]
                },
            })
        }));
    }
    componentDidMount() {
        this.getCountry('Germany', "SPY");
        


    }

    componentDidUpdate() {
    }
    render() {
        if (!this.state.isLoaded) {
            return <p>Loading the state</p>;
        }


        
        return (
            
            <div>
                <Select 
                    options = {this.state.options} 
                    value = {this.state.selectedName}
                    onChange={this.handleChange}
                    autoFocus={true}
                />
		<Select
		    options = {this.state.symbolOptions}
		    value = {this.state.selectedSymbol}
		    onChange={this.handleStockChange}
		    autoFocus={true}
		/>
                <ChartComponent chartData={this.state.chart} />
                <ChartComponent dispName={this.state.selectedName}/>
            </div>
            
        );
                //return (<ChartComponent chartData = {this.state.data}/>);
    }
}
