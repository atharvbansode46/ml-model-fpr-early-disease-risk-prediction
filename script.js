let chart;

function predictRisk() {

    let age = parseInt(document.getElementById("age").value) || 0;
    let bp = parseInt(document.getElementById("bp").value) || 0;
    let sugar = parseInt(document.getElementById("sugar").value) || 0;
    let cholesterol = parseInt(document.getElementById("cholesterol").value) || 0;
    let heart = parseInt(document.getElementById("heart").value) || 0;
    let bmi = parseInt(document.getElementById("bmi").value) || 0;

    let score = 0;

    // Risk Calculation

    if (age > 50) score += 20;

    if (bp > 140) score += 20;

    if (sugar > 120) score += 20;

    if (cholesterol > 200) score += 20;

    if (heart > 100) score += 10;

    if (bmi > 30) score += 10;

    let riskLevel = "";
    let resultText = "";

    // Risk Conditions

    if (score < 30) {

        riskLevel = "Low Risk";

        resultText =
            "✅ Patient has LOW disease risk.";

    }

    else if (score < 60) {

        riskLevel = "Medium Risk";

        resultText =
            "⚠️ Patient has MEDIUM disease risk.";

    }

    else {

        riskLevel = "High Risk";

        resultText =
            "🚨 Patient has HIGH disease risk.";
    }

    // Result Box

    document.getElementById("result").innerHTML = `
        ${resultText}
        <br><br>
        Risk Percentage:
        <span style="color:#38bdf8">
            ${score}%
        </span>
    `;

    // Progress Bar

    document.getElementById("progressFill").style.width =
        score + "%";

    document.getElementById("progressText").innerText =
        score + "%";

    // Chart

    const ctx =
        document.getElementById("riskChart");

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(ctx, {

        type: 'doughnut',

        data: {

            labels: [
                'Risk %',
                'Safe %'
            ],

            datasets: [{

                data: [
                    score,
                    100 - score
                ],

                backgroundColor: [
                    '#ef4444',
                    '#22c55e'
                ],

                borderWidth: 2
            }]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: 'black',

                        font: {
                            size: 15
                        }
                    }
                },

                title: {

                    display: true,

                    text:
                        riskLevel +
                        " (" +
                        score +
                        "%)",

                    color: 'black',

                    font: {
                        size: 22
                    }
                }
            }
        }
    });

}