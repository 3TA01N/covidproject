import React, { Component } from 'react';
import { Scatter } from 'react-chartjs-2';
import moment from 'moment';

export default class ChartComponent extends React.Component {

  constructor(props){
    super(props);
    this.chartRef = React.createRef();
    this.state = {
        chart: {
                datasets: [
                    {
                        
                    }
                ]
        }

        //isLoaded : false
     };
   
  }


  componentDidMount(){
   
}
    componentDidUpdate(prevProps) {
        if (prevProps.chartData !== this.props.chartData) {
            this.setState({chart: this.props.chartData}, () => {
        console.log("line 31 in chartcomponenet");
        console.log(this.state.chart.datasets[0].data);
    
    });  
}
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
     
//  } chart

//  componentDidUpdate(prevProps, prevState) {
//     if (this.props.chartData !== prevProps.chartData) {
//       this.selectNew();
//     }
//   }
  


  render(){
    if (!this.props.chartData) {
         return <p>Loading.</p>;
    }
    //console.log("chart data from chart");
    //this.waitNull();

    return (
        <div>
          
            <Scatter
                data={this.props.chartData.datasets[0].data}
                options={{
                    title:{
                      display:true,
                      text:"cases",
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
            <Scatter
                data={this.props.chartData}
                options={{
                    title:{
                      display:true,
                      text:"e",
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
