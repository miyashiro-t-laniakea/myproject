import React, { useState, useEffect } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';

import 'moment/locale/ja';
moment.locale('ja');

const localizer = momentLocalizer(moment);

const Dashboard = () => {
  const [repairJobs, setRepairJobs] = useState([]);
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching repair jobs...');
        const jobsResponse = await fetch('http://localhost:8000/api/repair-jobs/');
        console.log('Repair jobs response:', jobsResponse);

        console.log('Fetching vehicles...');
        const vehiclesResponse = await fetch('http://localhost:8000/api/vehicles/');
        console.log('Vehicles response:', vehiclesResponse);

        if (!jobsResponse.ok || !vehiclesResponse.ok) {
          throw new Error('API request failed');
        }

        const jobsData = await jobsResponse.json();
        const vehiclesData = await vehiclesResponse.json();

        console.log('Repair Jobs data:', jobsData);
        console.log('Vehicles data:', vehiclesData);

        setRepairJobs(jobsData.map(job => ({
          ...job,
          start: new Date(job.start_date),
          end: new Date(job.end_date),
          title: job.description
        })));
        setVehicles(vehiclesData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const getStatusText = (status) => {
    switch(status) {
      case 'pending': return '待機中';
      case 'in_progress': return '進行中';
      case 'completed': return '完了';
      default: return status;
    }
  };

  const eventStyleGetter = (event) => {
    let backgroundColor = '#3174ad';
    if (event.status === 'completed') {
      backgroundColor = '#5cb85c';
    } else if (event.status === 'pending') {
      backgroundColor = '#f0ad4e';
    }
    return { style: { backgroundColor } };
  };

  return (
    <div className="dashboard p-4">
      <h1 className="text-2xl font-bold mb-4">自動車整備工場ダッシュボード</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">修理作業</h2>
          <ul>
            {repairJobs.map(job => (
              <li key={job.id} className="mb-2">
                <span className="font-medium">{job.description}</span> - {getStatusText(job.status)}
                <br />
                <span className="text-sm text-gray-600">
                  {moment(job.start_date).format('YYYY年MM月DD日')} ～ {moment(job.end_date).format('YYYY年MM月DD日')}
                </span>
              </li>
            ))}
          </ul>
        </div>
        
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">車両一覧</h2>
          <ul>
            {vehicles.map(vehicle => (
              <li key={vehicle.id} className="mb-2">
                {vehicle.make} {vehicle.model} ({vehicle.year}年)
              </li>
            ))}
          </ul>
        </div>
      </div>
      
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-semibold mb-4">作業スケジュール</h2>
        <Calendar
          localizer={localizer}
          events={repairJobs}
          startAccessor="start"
          endAccessor="end"
          titleAccessor="title"
          style={{ height: 500 }}
          eventPropGetter={eventStyleGetter}
          messages={{
            next: "次へ",
            previous: "前へ",
            today: "今日",
            month: "月",
            week: "週",
            day: "日"
          }}
        />
      </div>

    </div>
  );
};

export default Dashboard;