<template>
  <div>
    <select v-model="selectedPlot" @change="fetchPlot">
      <option v-for="plot in plotTypes" :key="plot" :value="plot">
        {{ plot }}
      </option>
    </select>
    <div ref="plotContainer"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist'

export default {
  data() {
    return {
      selectedPlot: 'Contour',
      plotTypes: ['Contour', 'Bar', 'Scatter'],
    }
  },
  mounted() {
    this.fetchPlot()
  },
  methods: {
    async fetchPlot() {
      try {
        const response = await fetch(`http://localhost:5000/plot/${this.selectedPlot}`)
        const data = await response.json()
        Plotly.newPlot(this.$refs.plotContainer, JSON.parse(data))
      } catch (error) {
        console.error('Error fetching plot:', error)
      }
    }
  }
}
</script>