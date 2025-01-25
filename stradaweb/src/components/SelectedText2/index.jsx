import React, { useState } from 'react';
import { fetchSettings } from '../../api/services/config-service';
import { Input, Button, List, Typography, Space, message, Row, Col } from 'antd';
import { DeleteOutlined } from '@ant-design/icons';
import styles from './index.module.css';

const { Text } = Typography;

const TextListApp = () => {
  const [text1, setText1] = useState('');
  const [text2, setText2] = useState('');
  const [items, setItems] = useState([]);

  const handleAddItem = async () => {
    console.log(items);

    if (text1.trim() === '' || text2.trim() === '') {
      message.warning('Preencha ambos os campos antes de adicionar.');
      return;
    }

    const payload = [...items, { text1, text2 }];

    setItems(payload);
    setText1('');
    setText2('');
    await fetchSettings({ payload });

    message.success('Textos adicionados à lista!');
  };

  const handleRemoveItem = async (index) => {
    const newItems = items.filter((_, i) => i !== index);
    setItems(newItems);
    await fetchSettings({ payload: [] });

    message.info('Texto removido da lista.');
  };

  return (
    <div className={styles.master} >
      <Space direction="vertical" style={{ width: '100%' }}>
        <Row gutter={8}>
          <Col span={12}>
            <Input
              placeholder="Digite a primeira origem..."
              value={text1}
              onChange={(e) => setText1(e.target.value)}
            />
          </Col>
          <Col span={12}>
            <Input
              placeholder="Digite a segunda origem..."
              value={text2}
              onChange={(e) => setText2(e.target.value)}
            />
          </Col>
        </Row>
        <Button type="primary" onClick={handleAddItem}>
          Adicionar à lista
        </Button>
      </Space>

      <List
        style={{ marginTop: 10, overflow: 'auto', maxHeight: '500px' }}
        bordered
        dataSource={items}
        renderItem={(item, index) => (
          <List.Item
            actions={[
              <Button
                type="text"
                danger
                icon={<DeleteOutlined />}
                onClick={() => handleRemoveItem(index)}
              />
            ]}
          >
            <Text strong>{item.text1}</Text> - <Text type="secondary">{item.text2}</Text>
          </List.Item>
        )}
      />
    </div>
  );
};

export default TextListApp;