<template src="./subjects_list.html"></template>

<script>
export default {
  mixins: [],
  data() {
    return {
      message: ''
    }
  },
  computed: {},
  watch: {},
  methods: {
    initData() {
      this.fetchTests();
    },
    async fetchTests() {
      const uri = '/settings/subjects';
      return this.$axios.get(uri)
        .then(res => {
          this.message = res.data.results;
        })
        .catch(err => {
          this.message = err;
        })
        .finally()
    }
  },
  created() {
    this.initData();
  }
}
</script>