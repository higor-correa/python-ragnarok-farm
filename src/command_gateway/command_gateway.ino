#include <Keyboard.h>
#include <Mouse.h>
int m_x = 0;
int m_y = 0;
int to_move_x = 0;
int to_move_y = 0;

void setup() {
  delay(1000);
  pinMode(3, INPUT_PULLUP);
  Keyboard.begin();
  Mouse.begin();
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  delay(10000);

  while (digitalRead(3) == HIGH) {
    while (Serial.available() == 0) {}

    String incoming = Serial.readString();

    if (incoming == "start") {
      setAlootid();
    }

    if (incoming == "ALT1") {
      useAltShortcut('1');
    }

    if (incoming == "ALT3") {
      useAltShortcut('3');
    }

    if (incoming == "ALT7") {
      useAltShortcut('7');
    }

    if (incoming == "F1") {
      skillTargetAndCast(KEY_F1);
    }

    if (incoming == "F3") {
      skillTargetAndCast(KEY_F3);
    }

    if (incoming == "moveToStorage") {
      moveToStorage();
    }

    if (incoming == "typeText") {
      while (Serial.available() == 0) {}
      String text = Serial.readString();
      typeInRagnarok(text);
    }

    if (incoming == "simpleClick") {
      Mouse.click();
    }

    if (incoming == "closeTextBox") {
      Keyboard.press(KEY_RETURN);
      Keyboard.releaseAll();
      delay(50);
    }

    if (incoming == "move") {
      while (Serial.available() == 0) {}
      m_x = Serial.parseInt(SKIP_ALL, '\n');
      while (Serial.available() == 0) {}
      m_y = Serial.parseInt(SKIP_ALL, '\n');
      Mouse.move(m_x, m_y, 0);
    }
  }
}

void setAlootid() {
  typeInRagnarok("@alootid +12040");
  typeInRagnarok("@alootid +644");
  typeInRagnarok("@alootid +603");
  typeInRagnarok("@alootid +617");
}

void typeInRagnarok(String value) {
  Keyboard.print(value);
  delay(60);
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
  delay(60);
}

void moveToStorage() {
  Keyboard.press(KEY_LEFT_ALT);

  Keyboard.press('e');
  delay(50);
  Keyboard.release('e');
  delay(50);

  for (int i = 0; i < 1000; i++) {
    Mouse.click(MOUSE_RIGHT);
  }

  Keyboard.press('e');
  delay(50);
  Keyboard.release('e');

  Keyboard.releaseAll();
}

void skillTargetAndCast(uint8_t skillKey) {
  Keyboard.press(skillKey);
  delay(30);
  Keyboard.release(skillKey);
  delay(30);
  Mouse.press();
  delay(30);
  Mouse.release();
}

void useAltShortcut(char shortcutKey) {
  Keyboard.press(KEY_LEFT_ALT);

  Keyboard.press(shortcutKey);
  delay(50);
  Keyboard.release(shortcutKey);
  delay(50);
  
  Keyboard.releaseAll();
}