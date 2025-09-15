import { defineStore }  from "pinia";
import axios from "axios";
export const useFinanceStore = defineStore("finance", {
    state: () => ({
        transactions: [],
        categoryDist: {},
        recommendations: [],
        loading: false,
    }),
    actions: {
        async fetchTransactions(){
            this.loading = true;
            const res = await axios.get("/api/transactions", {headers: authHeader()});
            this.transactions = res.data;
            this.loading = false;
        },
        async fetchAnalytics() {
            const res = await axios.get("/api/analytics/recommendations", {headers: authHeader()});
            this.recommendations = res.data;
        }
    }
})
function authHeader() {
    return {"Authorization": "Bearer" + localStorage.getItem('token')};
}