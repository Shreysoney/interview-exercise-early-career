package com.comcast.stringinator.service;

import com.comcast.stringinator.model.StatsResult;
import com.comcast.stringinator.model.StringinatorInput;
import com.comcast.stringinator.model.StringinatorResult;

import java.util.HashMap;
import java.util.Map;

public class StringinatorService {

    private Map<String, Integer> seenStrings = new HashMap<>();

    public StringinatorResult stringinate(StringinatorInput input) {
        seenStrings.compute(input.getInput(), (k, v) -> (v == null) ? Integer.valueOf(1) : v + 1);

        StringinatorResult result = new StringinatorResult(input.getInput(), Integer.valueOf(input.getInput().length()));
        return result;
    }

    public StatsResult stats() {
        return new StatsResult(seenStrings);
    }


}
