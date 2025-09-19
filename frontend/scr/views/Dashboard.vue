<template>
    <v-container>
        <PieChart :data="categoryChartData" />
        <v-alert v-for="rec in recommendations" :key="rec.message" type="warning">
            {{ rec.message }} <br /> <i>{{ rec.suggestion }}</i>
        </v-alert>
        <TransactionList :transactions="transactions" />
    </v-container>
</template>

<script setup>
import { onMounted, computed } from "vue";
import { useFinanceStore } from "../stores/finance";
import PieChart from "../components/PieChart.vue";
import TransactionList from "../components/TransactionList.vue";

const store = useFinanceStore();
onMounted(()=>{store.fetchTransactions(); store.fetchAnalytics();})
const transactions = computed(()=>store.transactions);
const recommendations = computed(()=>store.recommendations);
const categoryChartData = computed(()=> {
    const categoryGroups = {};
    transactions.value.forEach(t => {
        if (t.type==='expense')
            categoryGroups[t.category] = (categoryGroups[t.category]||0) + t.amount
    });
    return {
        labels: Object.keys(categoryGroups),
        datasets: [{data: Object.values(categoryGroups), backgroundColor: ["#FF6384","#36A2EB","#FFCE56"]}]
    }
});
</script>