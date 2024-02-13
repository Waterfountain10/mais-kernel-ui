import React from 'react';

const DataTable = ({ data }) => {
  return (
    <div className="data-table w-1/2 h-screen overflow-y-scroll">
      <table className="table-auto w-full">
        <thead>
          <tr>
            <th className="px-4 py-2">Field Name</th>
            <th className="px-4 py-2">Extracted Data</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([key, value], index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{key}</td>
              <td className="border px-4 py-2">{value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
