package com.des;

import java.security.SecureRandom;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

public class Main {

	public static void main(String[] args) {
		DES des = new DES();
		
		String text = "YOU SUCK N";
		
		String cipher = des.encrypt(text);
	}
	
}
