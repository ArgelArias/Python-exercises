function solution(N){
  let res_arr = [];
  total = 0
  let half = Math.ceil(N/2);

  for (let i = 0; i < half; i++) {
    let new_val = Math.floor((Math.random() * N)) - half

    if(!res_arr.includes(new_val)){
      res_arr[i] = new_val;
      total += new_val;
    }
    else{
      while (res_arr.includes(new_val)){
        new_val = Math.floor((Math.random() * N)) - half;
      }
      res_arr[i] = new_val
      total += new_val;
    }
  }

  for (let i = half; i < N; i++) {
    let new_val = Math.floor((Math.random() * (N - total))/Math.floor(N/2))
    //let new_val = Math.ceil((N - total)/Math.floor(N/2));

    if(i == N -1){
      new_val = N - total;
    }

    if(!res_arr.includes(new_val)){
      res_arr[i] = new_val;
      total += new_val;
    }
    else{
      while (res_arr.includes(new_val)){
        new_val = Math.floor((Math.random() * N)) - half;
      }
      res_arr[i] = new_val
      total += new_val;
    }

  }

  return res_arr;
}

console.log(solution(4));
console.log(solution(5));
