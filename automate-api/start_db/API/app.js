import sequelize from './database.js';
import { DataTypes } from 'sequelize';

// Define o modelo
const Fretes = sequelize.define('Fretes', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
        unique: true,
    },
    produto: {
        type: DataTypes.STRING,
        allowNull: false
    },
    origem_1: {
        type: DataTypes.STRING,
        allowNull: false
    },
    origem_2: {
        type: DataTypes.STRING,
        allowNull: false
    },
    destino_1: {
        type: DataTypes.STRING,
        allowNull: false
    },
    destino_2: {
        type: DataTypes.STRING,
        allowNull: false
    },
    valor_acima_de: {
        type: DataTypes.INTEGER,
        allowNull: false
    }
}, {
    tableName: 'fretes',
    timestamps: false,
});

// Sincroniza com o banco de dados
(async () => {
    try {
        await sequelize.authenticate();  // Verifica a conexão
        console.log('Conexão bem-sucedida.');

        await Fretes.sync({ alter: true });  // Cria ou altera a tabela
        console.log('Tabela sincronizada com sucesso.');
    } catch (error) {
        console.error('Erro ao sincronizar a tabela:', error);
    } finally {
        await sequelize.close();  // Fecha a conexão (opcional, dependendo do uso)
    }
})();