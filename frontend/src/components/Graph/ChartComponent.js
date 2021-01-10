import React, { Component } from 'react';
import { Scatter } from 'react-chartjs-2';
import moment from 'moment';

export default class ChartComponent extends React.Component {

  constructor(props){
    super(props);
    this.chartRef = React.createRef();
    this.state = {
        //chart : null,
        //isLoaded : false
     };
  }


  componentDidMount(){

  }

//  static getDerivedStateFromProps(props, state) {
//      if (state.chartData !== props.chartData) {
//         var json = [];
//         var temp = props.chartData.data;
//         var reduced = temp.reduce(function(allDates, date) {
//             if (allDates.some(function(e) {
//                 return e.date === date.date
//               })) {
//               allDates.filter(function(e) {
//                 return e.date === date.date
//               })[0].cases += +date.cases
//             } else {
//               allDates.push({
//                 date: date.date,
//                 cases: +date.cases
//               })
//             }
//             return allDates
//         }, []);
//         //console.log(reduced);
//         //console.log(temp);
//         for (var j = 0; j < reduced.length; j++) {
//             var jsonObj = {x: moment(reduced[j].date), y: reduced[j].cases};
//             json.push(jsonObj);
//         }
//         console.log(json);
//         return {
//             chart: {
//                 datasets: [
//                     {
//                         label: 'Cases',
//                         data: json,
//                         pointBackgroundColor: "rgba(0,0,0)",
//                     }
//                 ]
//             },
//             //isLoaded : true
//         }
//      }
//      return null;
     
//  } 

//  componentDidUpdate(prevProps, prevState) {
//     if (this.props.chartData !== prevProps.chartData) {
//       this.selectNew();
//     }
//   }

  render(){
    // if (!this.state.isLoaded) {
    //     return <p>Loading.</p>;
    // }
    return (
        <div>
          
            <Scatter
                data={this.props.chartData}
                options={{
                    title:{
                      display:true,
                      text:'Cases',
                      fontSize:20
                    },
                    scales: {
                        xAxes: [{
                            position: 'bottom',
                            display: true,
                            type: 'time',
                            time: {
                                parser: 'YYYY-MM-DD',
                                displayFormats: {
                                    'day': 'YYYY-MM-DD'
                                }
                            }
                        }]
                    }
                }}
            />
            
        </div>
    )
        
    
  }

  
}