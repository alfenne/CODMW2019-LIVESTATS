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
    'longestStreak': 14
}


function pollAPI(timeoutTime, prevData) {

    $.ajax({
        url: 'http://127.0.0.1:5000/getStats',
        type: 'GET',
        success: function (currData) {

            if (prevData === "init") {
                updateUI(currData);
            }
            
            if (checkDataEquality(prevData, currData)) {
                timeoutTime = 120000;
                //timeoutTime = 5000;
                console.log("Found equal data...setting timeout time to 5 minutes");
            } else {
                timeoutTime = 90000;
                //timeoutTime = 3000;
                updateUI(currData);
                console.log("Found unequal data...setting timeout time to 90 seconds");
            }
            setTimeout(function() {
                pollAPI(timeoutTime, currData);
            }, timeoutTime);
        },
        error: function (error) { 
            console.error(error);
        }
    });

}

function incrementCard() {

    if (currCard < 7) {
        currCard++;
    } else {
        currCard = 0;
    }

    for (var i = 0; i < cardDivs.length; i++) {
        if (i === currCard) {
            cardDivs[i].style.display = "block";
        } else {
            cardDivs[i].style.display = "none";
        }
    }
}


function checkDataEquality(prevData, currData) {

    if (prevData === "init") {
        return false;
    }

    var dataEquality = true;

    Object.keys(currData).forEach(function(key, index) {

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
            
            document.getElementById(idString).style.display = "none";
            document.getElementById(idString2).style.display = "none";
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

}
