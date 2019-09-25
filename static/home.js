//globals

// const selector = d3.select("#selDataset");
// const selectorDos = d3.select("#selDatasetDos");


// function optionChanged() {
//     // Fetch new data each time a new sample is selected
//     let selectValue = d3.select("#selDataset").property('value');
//     //send new value to new options route
//     d3.json(`${selectValue}`).then((newOptions) => {
//         //clear old options
//         console.log(newOptions);
//     })
    
// };

// function init() {
//     d3.json("/webpages").then((pageNames) => {
//         // create dropdown
//         const names = Object.keys(pageNames);
//         console.log(names);
//         const routes = Object.keys(pageNames);
//         console.log(pageNames);
//         for (let i = 0; i < names.length; i++) {
//             selector
//             .append("option")
//             .text(names[i])
//             .property("value",routes[i])
            
//         }
//     })
// };

// init();