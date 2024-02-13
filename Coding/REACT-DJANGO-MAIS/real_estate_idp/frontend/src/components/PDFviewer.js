import React from 'react';
import { Document, Page } from 'react-pdf';
import 'react-pdf/dist/esm/Page/AnnotationLayer.css';

const PDFViewer = ({ file }) => {
  return (
    <div className="pdf-viewer w-1/2 h-screen">
      <Document file={file} className="h-full">
        <Page pageNumber={1} scale={1.0} />
      </Document>
    </div>
  );
};

export default PDFViewer;
