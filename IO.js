var write = new Function(string){
  print(string);
}

//Then just have the parser define print();

var input= new Function(type){
  var x=raw_input();
  if (type===int){
    x=int(x)
  }
  elseif(type===float){
    x=float(x);
  }
  elseif(type===str){
    x=str(x);
  }
  else{
    return False;
  break;
  }
return x;
}

var open = new Function(path, opt){
  //Code for file open here
}
