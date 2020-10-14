function data(){
    var nama = document.getElementById('nama_in').value;
    var m1 = document.getElementById('n1').value;
    var m1 = document.getElementById('n2').value;
    var m1 = document.getElementById('n3').value;
    var m1 = document.getElementById('n4').value;
    var m1 = document.getElementById('n5').value;
    var m2 = document.getElementById('n6').value;
    var m3 = document.getElementById('n7').value;
    
    tugas = 0.5*m1;
    uts = 0.25*m2;
    uas = 0.25*m3;
 
    jumlah = tugas+uts+uas;
 
   var grade;
 
      if(jumlah >=80)
     {
     grade= "A" ;
     }
     else if (jumlah >=70)
     {
     grade= "B" ;
     }
 
     else if (jumlah >=59)
     {
     grade= "C" ;
     }
     else if (jumlah >=50)
     {
     grade= "D" ;
     }
     else
     {
     grade="E" ;
 
     }
 
 
 /*output*/
    document.getElementById("nama_out").innerHTML="Nama : "+nama;
    document.getElementById("uts_out").innerHTML="UTS : "+m2;
    document.getElementById("uas_out").innerHTML="UAS : "+m3;
 
    document.getElementById("note").innerHTML="Note : ";
    document.getElementById("ket_tugas").innerHTML="Tugas 50% : "+tugas;
    document.getElementById("ket_uts").innerHTML="Tugas 25% : "+uts;
    document.getElementById("ket_uas").innerHTML="Tugas 25% : "+uas;
 
 
    document.getElementById("jumlah_out").innerHTML="Jumlah : "+jumlah;
    document.getElementById("grade_out").innerHTML="Grade : "+grade;
  }