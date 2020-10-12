function frequency(text){
    let freq_dict = {};
    for (ch of text)
        if (ch in freq_dict){
            freq_dict[ch] = freq_dict[ch]+1
        }else{freq_dict[ch]=1
        }
    return freq_dict;
}

var text = 'aaabccdeeeeeffg';
var freq = frequency(text);

function sortFreq(freq_dict){
    let letters_list = Object.keys(freq_dict);
    let nested_list = []; 
    for (i=0; i<letters_list.length; i++){
        nested_list.push([freq_dict[letters_list[i]],letters_list[i]]);
    }
    nested_list.sort()
    return nested_list; 
}

var nested_list = sortFreq(freq);

function buildTree(nestedList){
    while(nestedList.length > 1){
    let least_two = nestedList.slice(0,2);
    let rest_list = nestedList.slice(2,); 
    let combine_freq = least_two[0][0] + least_two[1][0];
    nestedList = rest_list.concat([[combine_freq].concat([least_two])]); 
    nestedList.sort();
    }
    return nestedList[0]; 
}

var tree_code = buildTree(nested_list);
console.log(tree_code)

function trimTree(tree){
    let p = tree[1];
    if (typeof(p) ==typeof("")){
        return p;
    }else{
        return [trimTree(p[0]), trimTree(p[1])];
    }
}

var trim = trimTree(tree_code);
console.log(trim)

var codes = {}; 
function assignCodes(node, pat=''){
    if (typeof(node) == typeof("")){
        codes[node] = pat;
    }else{
        assignCodes(node[0], pat+'0');
        assignCodes(node[1], pat+'1');
    }
}

assignCodes(trim)
console.log(codes);

function encode(text){
    let output ='';
    for (ch of text){
        output += codes[ch];
    }return output
}

var encode_text = encode(text);

function decode(tree,bytecode){
    let output = '';
    let p = tree;
    for (bit of bytecode){
        if (bit == '0'){
            p = p[0];
        }else{p = p[1];}
        if (typeof(p) == typeof('')){
            output += p;
            p = tree;
        }
    }return output
}

var string = decode(trim, encode_text);
console.log(string);

function decode_with_bitecode (bitcode, code_dict){
    let output ='';
    let decode_dict = {};
    for (key in code_dict){
        decode_dict[code_dict[key]] = key;
    }
    let byte = ''; 
    for (bit of bitcode){
        byte += bit;
        if (byte in decode_dict){
            output += decode_dict[byte];
            byte = ''
        }
    }return output
}

var string_2 = decode_with_bitecode(encode_text, codes);
console.log(string_2);
