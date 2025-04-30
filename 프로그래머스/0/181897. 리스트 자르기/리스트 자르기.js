function solution(n, slicer, num_list) {
    var answer = [];
    const a = slicer[0]
    const b = slicer[1]
    const c = slicer[2]
    
    switch(n){
        case 1:
            return num_list.slice(0,b+1)
        case 2:
            return num_list.slice(a,num_list.length+1)
        case 3:
            return num_list.slice(a,b+1)
        case 4:
            return num_list.slice(a,b+1).filter((_, i) => i%c === 0)
    }
    return answer;
}