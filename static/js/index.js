var currCard = 0;
const cardDivs = document.getElementsByClassName("statCard");

const cardOrder = {
    'kdSpread':0,
    'scorePerMinute': 2,
    'scorePerGame': 4,
    'wlRatio': 6,
    'killsPerGame': 8,
    'killsPerMinute': 10,
    'accuracy': 12,
    'longestStreak': 14,
    'atKdSpread': 16
}


function pollAPI(prevData) {

    $.ajax({
        url: 'http://127.0.0.1:5000/getStats',
        type: 'GET',
        success: function (currData) {

            if (prevData === "init") {
                updateUI(currData);
            }
            else if (currData !== "error") {
                //if (!checkDataEquality(prevData, currData)) {
                    updateMap(currData);
                    updateCorona(currData);
                    updateUI(currData);
                    
                //}
            } else {
                currData = prevData
            }

            setTimeout(function() {
                pollAPI(currData);
            }, 120000);
        
        },
        error: function (error) { 
            console.error(error);
        }
    });
}

function updateMap(currData) {

    document.getElementById("map").innerHTML = "";

    $(function(){
        $('#map').vectorMap({
        map: 'us_aea',
        backgroundColor: "#323130",
        series: {
            regions: [{
                values: currData['stateData'],
            scale: ['#fff5f5', '#7a0000'],
            normalizeFunction: 'polynomial'
            }]
        },
        onRegionTipShow: function(e, el, code){
            el.html(el.html()+ " " + String((currData['stateData'][code] / 100).toFixed(4)) + "%");
        }
        });
    });
}

function updateCorona(data) {

    if (data['coronaDeaths'] === undefined || data['coronaCases'] === undefined || data['currRate'] === undefined) {
        console.log("data error");
    } else {

        document.getElementById("coronaDeaths").innerHTML = "Deaths: " + String(data['coronaDeaths']);
        document.getElementById("coronaCases").innerHTML = "Cases: " + String(data['coronaCases']);
        document.getElementById("deathRate").innerHTML = "Rate: " + String(data['currRate']) + "%";
    
    //     var days = [];
    //     var deaths = [];
    //     var cases = [];
    
    //     for (var i = 0; i < data['timeSeriesData'].length; i++) {
    //         days.push(data['timeSeriesData'][i]['date']);
    //         deaths.push(data['timeSeriesData'][i]['deaths']);
    //         cases.push(data['timeSeriesData'][i]['cases']);
    //     } 
    
    //     new Chart(document.getElementById("rateChart"), {
    //         type: 'line',
    //         data: {
    //           labels: days,
    //           datasets: [{
    //               data: cases,
    //               label: "Cases",
    //               borderColor: "#3e95cd",
    //               fill: false
    //               },
    //               {
    //                   data:deaths,
    //                   label:"Deaths",
    //                   borderColor:"#ff4f38",
    //                   fill:false
    //               }
    //            ]
    //         },
    //         options: {
    //             legend: {
    //                 fontColor: "white"
    //             },
    //             scales: {
    //                 yAxes: [{
    //                     ticks: {
    //                         fontColor: 'white'
    //                     },
    //                     type: 'logarithmic',
    //                 }],
    //               xAxes: [{
    //                     ticks: {
    //                         fontColor: 'white'
    //                     },
    //                 }]
    //             } 
    //         }
    //       });
    }

}

function incrementCard() {

    if (currCard < 8) {
        currCard++;
    } else {
        currCard = 0;
    }
    for (var i = 0; i < cardDivs.length; i++) {
        if (i === currCard) {
            cardDivs[i].style.display = "block";
        } else {
            cardDivs[i].style.display = "none";
            // document.getElementById("statusArrow" + String(i * 2)).style.visibility = "hidden";
            // document.getElementById("statusArrow" + String((i * 2) + 1)).style.visibility = "hidden";
        }
    }
}

function checkDataEquality(prevData, currData) {

    if (prevData === "init") {
        return false;
    }
    var dataEquality = true;
    Object.keys(currData).forEach(function(key, index) {

        if (key === "coronaDeaths" || key === "coronaCases") {
            console.log("Hitting");
        } else {

            var idString = "statusArrow" + String(cardOrder[key]);
            var idString2 = "statusArrow" + String(cardOrder[key] + 1);
    
            if (currData[key] !== prevData[key]) {
                dataEquality = false;
    
                if (currData[key] > prevData[key]) {
                    document.getElementById(idString).src = "../static/img/uparrow.svg";
                    document.getElementById(idString2).src = "../static/img/uparrow.svg";
    
                } else {
                    
                    document.getElementById(idString).src = "../static/img/downarrow.svg";
                    document.getElementById(idString2).src = "../static/img/downarrow.svg";
    
                }
            } else {
                document.getElementById(idString).style.visibility = "hidden";
                document.getElementById(idString2).style.visibility = "hidden";
            }

        }
    });
    return dataEquality;
}

function updateUI(currData) {

    var kdSpread = currData['kdSpread'];
    document.getElementById("kdSpreadData").innerHTML = kdSpread.toFixed(5);

    var scorePerMinute = currData['scorePerMinute'];
    document.getElementById("scorePerMinuteData").innerHTML = scorePerMinute.toFixed(3);

    var scorePerGame = currData['scorePerGame'];
    document.getElementById("scorePerGameData").innerHTML = scorePerGame.toFixed(2);

    var wlRatio = currData['wlRatio'];
    document.getElementById("wlRatioData").innerHTML = wlRatio.toFixed(5);

    document.getElementById("longestStreakData").innerHTML = currData['longestStreak'];

    var killsPerGame = currData['killsPerGame'];
    document.getElementById("killsPerGameData").innerHTML = killsPerGame.toFixed(4);

    var killsPerMinute = currData['killsPerMinute'];
    document.getElementById("killsPerMinuteData").innerHTML = killsPerMinute.toFixed(5);

    var accuracy = currData['accuracy'];
    document.getElementById("accuracyData").innerHTML = accuracy.toFixed(4) + "%";

    var atKdSpread = currData['atKdSpread'];
    document.getElementById('atKdSpreadData').innerHTML = atKdSpread.toFixed(5);

    // var id1 = "statusArrow" + String(currCard * 2);
    // var id2 = "statusArrow" + String((currCard * 2) + 1);

    // document.getElementById(id1).style.visibility = "visible";
    // document.getElementById(id2).style.visibility = "visible";

    // setTimeout(function(){
    //     var allArrows = document.getElementsByClassName("statusArrow");
    //     for (var i = 0; i < allArrows.length; i++) {
    //         allArrows[i].style.visibility = "hidden";
    //     }
    // },15000);

}
