<script>
import api from "../services/api";

export default {
  data() {
    return {
      query: "", // Inicializa como uma string vazia
      operadoras: [], // Lista de operadoras retornadas pela API
      loading: false, // Estado de carregamento
      error: null, // Mensagem de erro
    };
  },
  methods: {
    async buscarOperadoras() {
      console.log("Valor de this.query antes da verificação:", this.query); // Log para depuração
      if (!this.query) return; // Verifica se o campo de busca está vazio

      this.loading = true;
      this.error = null;

      try {
        console.log("Enviando consulta:", this.query); // Log para depuração
        const response = await api.get("/busca-operadora/", {
          params: { q: this.query },
        });
        console.log("Resposta da API:", response.data); // Log para depuração
        this.operadoras = response.data;
      } catch (err) {
        console.error("Erro ao buscar operadoras:", err); // Log do erro
        this.error = "Erro ao buscar operadoras.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<template>
  <div class="container">
    <h2>Buscar Operadoras</h2>
    
    <!-- Campo de entrada vinculado à propriedade `query` -->
    <input 
      v-model="query" 
      @keyup.enter="buscarOperadoras" 
      placeholder="Digite o nome da operadora..." 
    />
    
    <button @click="buscarOperadoras">Buscar</button>
    
    <p v-if="loading">🔄 Buscando...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <!-- Exibição dos resultados em cartões -->
    <div v-if="operadoras.length" class="cards-container">
      <div v-for="operadora in operadoras" :key="operadora.Registro_ANS" class="card">
        <h3>{{ operadora.Razao_Social }}</h3>
        <p><strong>Registro ANS:</strong> {{ operadora.Registro_ANS }}</p>
        <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>
        <p><strong>Cidade:</strong> {{ operadora.Cidade }}</p>
        <p><strong>UF:</strong> {{ operadora.UF }}</p>
      </div>
    </div>

    <p v-else-if="!loading && query">Nenhum resultado encontrado.</p>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 20px auto;
  text-align: center;
}

input {
  width: 80%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #369970;
}

.error {
  color: red;
}

/* Estilo para os cartões */
.cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
  margin-top: 20px;
}

.card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  width: 250px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.card h3 {
  margin: 0 0 10px;
  font-size: 18px;
  color: #333;
}

.card p {
  margin: 5px 0;
  font-size: 14px;
  color: #555;
}

.card p strong {
  color: #333;
}
</style>