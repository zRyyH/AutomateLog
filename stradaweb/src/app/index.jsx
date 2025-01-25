import styles from './index.module.css';
import React, { useState } from 'react';
import { Switch } from 'antd';
import TextListApp from '../components/SelectedText2';
import { fetchStop, fetchStart } from '../api/services/config-service';



function App() {
  const [running, setRunning] = useState(false);

  async function handleChange(checked) {
    setRunning(checked);
    console.log('Switch está:', checked ? 'Ligado' : 'Desligado');

    if (checked) {
      await fetchStart()
    } else {
      await fetchStop()
    }
  };

  return (
    <div className={styles.master}>
      <div className={styles.contextCointainer} >
        <div className={styles.header} >
          <p>STRADA LOG</p>
        </div>
        <div className={styles.body} >
          <TextListApp />
        </div>
        <div className={styles.footer} >
          <p>Ativar ou Desativar BOT</p>
          <Switch checked={running} onChange={handleChange} />
        </div>
      </div>
    </div>
  );
}


export default App;