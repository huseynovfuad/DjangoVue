<template>
  <div class='row'>
      <div class='col-lg-6'>
      <input type='hidden' v-model='url' class='form-control mt-2' placeholder='Enter todo text'>
      <input type='text' class='form-control mt-2' placeholder='Enter todo text' v-model='text'><br>
      <button @click='postTodo' class='btn bg-success text-light'>Add</button>
      </div>
      <div class='col-lg-6'>
          <table class='table'>
              <thead>
                  <th>Text</th>
                  <th>Completed</th>
                  <th>Edit</th>
                  <th>Delete</th>
              </thead>
              <tbody>
                  <tr v-for='list in lists' v-bind:key='list.url'>
                      <td>{{list.text}}</td>
                      <td>
                        <button style='background:none;border:none;' @click='checkTodo(list)'>
                          <i style='font-size:35px;' v-if='list.completed' class="fa fa-times text-danger"></i>
                          <i style='font-size:35px;' v-else class="fa fa-check text-success"></i>
                        </button>
                      </td>
                      <td><button @click='getOne(list)' class='btn bg-info text-light'><i class="fa fa-pencil"></i></button></td>
                      <td><button @click='deleteOne(list.url)' class='btn bg-warning text-light'><i class="fa fa-trash"></i></button></td>
                  </tr>
              </tbody>
          </table>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      lists:null,
      text:'',
      url:'',
      completed:false,
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/api/todos').then((res)=>{
        this.lists = res.data;
        this.text='';
        this.url='';
      })
    },
    getOne(list){
      this.url = list.url;
      this.text = list.text;
    },
    deleteOne(url){
      axios.delete(url).then(()=>{
        this.getAll();
      });
    },
    checkTodo(list){
      var checked;
      checked = !list.completed;
      console.log(checked);
      axios.put(list.url,{text:list.text,completed:checked,}).then(()=>{
        this.getAll();
      });
    },
    postTodo(){
      if(this.url == ''){
        axios.post('http://localhost:8000/api/todos/',{text:this.text,completed:this.completed})
      .then(()=>{
        this.getAll();
      });
      this.text='';
      }
      else{
        axios.put(this.url,{text:this.text,completed:this.completed})
      .then(()=>{
        this.getAll();
      });
      this.text='';
      }
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
