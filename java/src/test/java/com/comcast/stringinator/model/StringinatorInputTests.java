package com.comcast.stringinator.model;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * A DTO is a DTO. Not a very useful test, but perhaps a guide to work from.
 */
class StringinatorInputTests {

    @Test
    @DisplayName("should return the input that is set")
    void inputField() {
        // given
        String s = "input string";

        // when
        StringinatorInput input = new StringinatorInput(s);

        // then
        assertEquals(s, input.getInput());
    }

}
