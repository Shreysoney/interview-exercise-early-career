package com.comcast.stringinator;

import com.comcast.stringinator.model.StringinatorInput;
import com.comcast.stringinator.model.StringinatorResult;
import com.comcast.stringinator.service.StringinatorService;

import java.io.Console;

public class StringinatorApplication {

	public static void main(String[] args) {
		StringinatorService service = new StringinatorService();

		Console console = System.console();
		while (true) {
			String inputString = console.readLine("Enter an input string ('stats' to see statistics, 'quit' to exit): ");

			if ("stats".equalsIgnoreCase(inputString)) {
				console.printf("\nStats:\n");
				console.printf(service.stats().getInputs().toString());
			} else if ("quit".equalsIgnoreCase(inputString)) {
				console.printf("Exiting...\n");
				break;
			} else {
				StringinatorInput input = new StringinatorInput(inputString);
				StringinatorResult result = service.stringinate(input);

				console.printf("\nInput = " + result.getInput());
				console.printf("\nLength = " + result.getLength());
			}

			console.printf("\n\n");
		}
	}

}
