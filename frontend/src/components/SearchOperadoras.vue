<script>
import api from "../services/api";

export default {
  data() {
    return {
      query: "", // Termo de busca digitado pelo usuário
      operadoras: [], // Lista de operadoras retornadas pela API
      loading: false, // Estado de carregamento
      error: null, // Mensagem de erro
    };
  },
  methods: {
    async buscarOperadoras() {
      if (!this.query) return;

      this.loading = true;
      this.error = null;

      try {
        const response = await api.get("/busca-operadora/", {
          params: { q: this.query },
        });
        this.operadoras = response.data;
      } catch (err) {
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
    
    <input 
      v-model="query" 
      @keyup.enter="buscarOperadoras" 
      placeholder="Digite o nome da operadora..." 
    />
    
    <button @click="buscarOperadoras">Buscar</button>
    
    <p v-if="loading">🔄 Buscando...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <ul v-if="operadoras.length">
      <li v-for="operadora in operadoras" :key="operadora.Registro_ANS">
        {{ operadora.Razao_Social }} (Registro ANS: {{ operadora.Registro_ANS }})
      </li>
    </ul>

    <p v-else-if="!loading && query">Nenhum resultado encontrado.</p>
  </div>
</template>

<style scoped>
.container {
  max-width: 400px;
  margin: 20px auto;
  text-align: center;
}
input {
  width: 80%;
  padding: 8px;
  margin-bottom: 10px;
}
button {
  padding: 8px 12px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #369970;
}
.error {
  color: red;
}
</style>