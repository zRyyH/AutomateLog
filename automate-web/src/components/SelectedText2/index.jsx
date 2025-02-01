import React, { useState } from 'react';
import { fetchSettings } from '../../api/services/config-service';
import { Input, Button, List, Typography, Space, message, Row, Col } from 'antd';
import { DeleteOutlined } from '@ant-design/icons';
import styles from './index.module.css';

const { Text } = Typography;

const TextListApp = () => {
  const [origem1, setOrigem1] = useState('');
  const [origem2, setOrigem2] = useState('');
  const [produto, setProduto] = useState('');
  const [items, setItems] = useState([]);

  const handleAddItem = async () => {
    if (origem1.trim() === '' || origem2.trim() === '' || produto.trim() === '') {
      message.warning('Preencha todos os campos antes de adicionar.');
      return;
    }

    const payload = [...items, { origem1, origem2, produto }];

    setItems(payload);
    setOrigem1('');
    setOrigem2('');
    setProduto('');
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
    <div className={styles.master}>
      <Space direction="vertical" style={{ width: '100%' }}>
        <Row gutter={8}>
          <Col span={8}>
            <Input
              placeholder="Origem 1..."
              value={origem1}
              onChange={(e) => setOrigem1(e.target.value)}
            />
          </Col>
          <Col span={8}>
            <Input
              placeholder="Origem 2..."
              value={origem2}
              onChange={(e) => setOrigem2(e.target.value)}
            />
          </Col>
          <Col span={8}>
            <Input
              placeholder="Tipo de produto..."
              value={produto}
              onChange={(e) => setProduto(e.target.value)}
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
            <Text strong>{item.origem1}</Text> - <Text type="secondary">{item.origem2}</Text> - <Text>{item.produto}</Text>
          </List.Item>
        )}
      />
    </div>
  );
};

export default TextListApp;