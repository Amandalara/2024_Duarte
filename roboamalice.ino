#define int1 3 // F_VERDE
#define int2 5 // F_BRANCO1
#define int3 9 // F_CINZA
#define int4 10 // F_BRANCO2



void setup() {
  // put your setup code here, to run once:
pinMode(int1, OUTPUT);
pinMode(int2, OUTPUT);
pinMode(int3, OUTPUT);
pinMode(int4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite (int1,HIGH);
digitalWrite (int2,LOW);
digitalWrite (int3,HIGH);
digitalWrite (int4,LOW);

}
