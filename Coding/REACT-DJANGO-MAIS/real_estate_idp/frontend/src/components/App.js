import React, { Component } from 'react';
import { render } from "react-dom";
import PDFViewer from "./PDFviewer";
import DataTable from "./DataTable";

export default class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null, // Holds the uploaded PDF file (as a URL or file object)
            extractedData: {} // This will hold the extracted data for the DataTable
        };
    }

    // Handler for file selection
    onFileChange = (event) => {
        const file = event.target.files[0];
        if (file && file.type === "application/pdf") {
            this.setState({
                file: URL.createObjectURL(file) // Create a URL for the file
            });
        } else {
            console.log("Please select a PDF file.");
        }
    };

    // Render function
    render() {
        const { file, extractedData } = this.state;
        return(
            <div className="app-container">
                <div className="file-upload">
                    <input type="file" onChange={this.onFileChange} accept="application/pdf" />
                    {/* Button can be used to trigger further actions like extracting data */}
                </div>
                <div className="flex">
                    {file && <PDFViewer file={file} />}
                    <DataTable data={extractedData} />
                </div>
            </div>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
