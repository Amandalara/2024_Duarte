#define int1 2 // F_AMARELO
#define int2 4 // F_BRANCO1
#define int3 7 // F_CINZA
#define int4 8 // F_BRANCO2



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
