<template src="./test_list.html"></template>

<script>
export default {
  mixins: [],
  data() {
    return {
      message: 'aaaaa'
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
          //console.log(err)
          this.message = err;
        })
        .finally()
    }
  },
  created() {
    // console.log(process.env.VUE_APP_API_URL)
    this.initData();
  }
}
</script>