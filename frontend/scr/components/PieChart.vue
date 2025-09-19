<template>
    <canvas ref="pieCanvas"></canvas>
</template>
<script setup>
import { ref, onMounted, watch } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables)


const props = defineProps({data: Object});
const pieCanvas = ref();
let chart;
const renderChart = () => {
    if (chart) chart.destroy();
    chart = new Chart(pieCanvas.value.getContext("2d"), {type: "pie", data: props.data});
};

onMounted(renderChart);
watch(()=>props.data, renderChart, {deep:true});
</script>