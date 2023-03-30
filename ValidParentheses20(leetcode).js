
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let stack = []
  for(let i of s){
    if( i === '(' || i=== '{' || i==='['){
      stack.push(i);
      continue;
    }
    if(i===')'){
      if(stack.pop()!='('){
        return false
      }
      continue;
    }
    if(i==='}'){
      if(stack.pop()!='{'){
        return false
      }
      continue;
    }
    if(i===']'){
      if(stack.pop()!='['){
        return false
      }
    }
  }
  return stack.length===0;
  
};

s = '()'

result = isValid(s);

console.log(result)
