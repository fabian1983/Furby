 myMP3.play(myRandom);
 
    while (myMP3.isPlaying()){
     Serial.println("Track is playing");
     speak();     
    }
