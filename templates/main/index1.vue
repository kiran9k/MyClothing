
<template>
    <div>
        <div class="ss-app">
            <div id="smart-sizes-grid" class="survey-wrap ">
                <a class="current-unit " href="#">US</a>
                <div class="ss-unit-toggle global-toggle">
                    <a class="unit-us" data-unit="us" href="#">
                        <span>US</span>
                    </a>
                    <a class="unit-metric" data-unit="metric" href="#">
                        <span>Metric</span>
                    </a>
                </div>
                
                <div class="row"><br/><br/></div>
                <div class="size-survey " data-format="us">
                    
                    <section id="smart_size_step_1" v-if="navPage == 1" class="question first is-current mt-3 " data-type="radio">
                        <h2>
                            <span>01</span>What size t-shirts do you typically&nbsp;wear?</h2>
                        <div class="answers flex-col lg-2-col md-2-col sm-2-col">
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="Extra Small" v-model="size" value="xs" tabindex="1" autofocus>
                                <span>Extra Small</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="Small" v-model="size" value="s">
                                <span>Small</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="Medium" v-model="size" value="m">
                                <span>Medium</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="Large" v-model="size" value="l">
                                <span>Large</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="Extra Large" v-model="size" value="xl">
                                <span>Extra Large</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="2XL" v-model="size" value="xxl">
                                <span>2XL</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="3XL" v-model="size" value="3xl">
                                <span>3XL</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="4XL" v-model="size" value="4xl">
                                <span>4XL</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="5XL" v-model="size" value="5xl">
                                <span>5XL</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-tshirt" data-fname="6XL" v-model="size" value="6xl">
                                <span>6XL</span>
                            </label>
                        </div>
                        <nav class="q-nav">
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    
                    <section id="smart_size_step_2"   v-if="navPage == 2" class="question  first is-current " data-type="input">
                        <header>
                            <h2>
                                <span>02</span>How tall are you?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="US" data-measure-metric="EU">
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_4" in-value="5&prime;4&Prime;" cm-value="166">
                                <span>5&prime;4&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_5" in-value="5&prime;5&Prime;" cm-value="168">
                                <span>5&prime;5&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_6" in-value="5&prime;6&Prime;" cm-value="170">
                                <span>5&prime;6&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_7" in-value="5&prime;7&Prime;" cm-value="172">
                                <span>5&prime;7&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_8" in-value="5&prime;8&Prime;" cm-value="174">
                                <span>5&prime;8&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_9" in-value="5&prime;9&Prime;" cm-value="176">
                                <span>5&prime;9&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_10" in-value="5&prime;10&Prime;" cm-value="178">
                                <span>5&prime;10&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_11" in-value="5&prime;11&Prime;" cm-value="180">
                                <span>5&prime;11&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_0" in-value="6&prime;0&Prime;" cm-value="182">
                                <span>6&prime;0&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_1" in-value="6&prime;1&Prime;" cm-value="184">
                                <span>6&prime;1&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_2" in-value="6&prime;2&Prime;" cm-value="186">
                                <span>6&prime;2&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_3" in-value="6&prime;3&Prime;" cm-value="188">
                                <span>6&prime;3&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_4" in-value="6&prime;4&Prime;" cm-value="190">
                                <span>6&prime;4&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_5" in-value="6&prime;5&Prime;" cm-value="192">
                                <span>6&prime;5&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_6" in-value="6&prime;6&Prime;" cm-value="194">
                                <span>6&prime;6&Prime;</span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_7" in-value="6&prime;7&Prime;" cm-value="196">
                                <span>6&prime;7&Prime;</span>
                            </label>
                            <label class="answer block other"><input class="else" type="radio" name="q-height" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="tall" class="height-ft" type="number" width="1" maxlength="1" inputmode="numeric">
                                        <i class="other-label">ft</i>
                                    </i>
                                    <i class="other-wrap">
                                        <input data-what="tall" class="height-in" type="number" width="4" maxlength="5" inputmode="numeric" step="0.1">
                                        <i class="other-label">in</i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>
                            <label class="answer block"><input class="skip" type="radio" name="q-height" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_3"  v-if="navPage == 3" class="question  first is-current" data-type="input">
                        <header>
                            <h2>
                                <span>03</span>How much do you weigh?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="lbs" data-measure-metric="kg">
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="150" in-value="150" cm-value="70">
                                <span>150</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="155" in-value="155" cm-value="72">
                                <span>155</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="160" in-value="160" cm-value="74">
                                <span>160</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="165" in-value="165" cm-value="76">
                                <span>165</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="170" in-value="170" cm-value="78">
                                <span>170</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="175" in-value="175" cm-value="80">
                                <span>175</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="180" in-value="180" cm-value="82">
                                <span>180</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="185" in-value="185" cm-value="84">
                                <span>185</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="190" in-value="190" cm-value="86">
                                <span>190</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="195" in-value="195" cm-value="88">
                                <span>195</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="200" in-value="200" cm-value="90">
                                <span>200</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="205" in-value="205" cm-value="92">
                                <span>205</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="210" in-value="210" cm-value="94">
                                <span>210</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="215" in-value="215" cm-value="96">
                                <span>215</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="220" in-value="220" cm-value="98">
                                <span>220</span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="225" in-value="225" cm-value="100">
                                <span>225</span>
                            </label>
                            <label class="answer block other"><input class="else" type="radio" name="q-weight" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="weight" value="" type="number" width="3" maxlength="6" inputmode="numeric" step="5" style="min-width: 80px;">
                                        <i class="other-label"></i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>
                            <label class="answer block"><input class="skip" type="radio" name="q-weight" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>
                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_4"  v-if="navPage == 4" class="question  first is-current" data-type="radio">
                        <header>
                            <h2>
                                <span>04</span>Which best describes your ethnicity?</h2>
                        </header>

                        <div class="answers flex-col lg-1-col sm-1-col">
                            <label class="answer"><input class="first" type="radio" name="q-ethnicity" value="1">
                                <span>Asian</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-ethnicity" value="2">
                                <span>Black</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-ethnicity" value="3">
                                <span>Caucasian</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-ethnicity" value="4">
                                <span>Hispanic</span>
                            </label>
                            <label class="answer block"><input class="skip" type="radio" name="q-ethnicity" value="" checked="checked">
                                <span>Other - I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>

                    </section>

                    <section id="smart_size_step_5"  v-if="navPage == 5" class="question  first is-current suit-size " data-type="input">
                        <header>
                            <h2>
                                <span>05</span>What is your suit jacket size (
                                <i data-text-eu="EU Sizing" data-text-us="if you know it">if you know it</i>)?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col">
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="36" in-value="36" cm-value="46">
                                <span>36</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="37" in-value="37" cm-value="47">
                                <span>37</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="38" in-value="38" cm-value="48">
                                <span>38</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="39" in-value="39" cm-value="49">
                                <span>39</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="40" in-value="40" cm-value="50">
                                <span>40</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="41" in-value="41" cm-value="51">
                                <span>41</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="42" in-value="42" cm-value="52">
                                <span>42</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="43" in-value="43" cm-value="53">
                                <span>43</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="44" in-value="44" cm-value="54">
                                <span>44</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="45" in-value="45" cm-value="55">
                                <span>45</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="46" in-value="46" cm-value="56">
                                <span>46</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="47" in-value="47" cm-value="57">
                                <span>47</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="48" in-value="48" cm-value="58">
                                <span>48</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="49" in-value="49" cm-value="59">
                                <span>49</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="50" in-value="50" cm-value="60">
                                <span>50</span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="51" in-value="51" cm-value="61">
                                <span>51</span>
                            </label>
                            <label class="answer block other"><input class="else" type="radio" name="q-jacket" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="jacket_size" type="number" width="2" maxlength="2" inputmode="numeric" style="min-width: 70px;">
                                        <i class="other-label"></i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>
                            <label class="answer block"><input class="skip" type="radio" name="q-jacket" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>
                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_6"   v-if="navPage == 6" class="question first is-current  " data-type="input">
                        <header>
                            <h2>
                                <span>06</span>What is the waist size of your&nbsp;pants?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="27" in-value="27" cm-value="74">
                                <span>27</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="28" in-value="28" cm-value="76">
                                <span>28</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="29" in-value="29" cm-value="78">
                                <span>29</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="30" in-value="30" cm-value="80">
                                <span>30</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="31" in-value="31" cm-value="82">
                                <span>31</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="32" in-value="32" cm-value="84">
                                <span>32</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="33" in-value="33" cm-value="86">
                                <span>33</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="34" in-value="34" cm-value="88">
                                <span>34</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="35" in-value="35" cm-value="90">
                                <span>35</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="36" in-value="36" cm-value="92">
                                <span>36</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="37" in-value="37" cm-value="94">
                                <span>37</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="38" in-value="38" cm-value="96">
                                <span>38</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="39" in-value="39" cm-value="98">
                                <span>39</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="40" in-value="40" cm-value="100">
                                <span>40</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="41" in-value="41" cm-value="102">
                                <span>41</span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="42" in-value="42" cm-value="104">
                                <span>42</span>
                            </label>
                            <label class="answer block other"><input class="else" type="radio" name="q-pants" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="pants_waist" type="number" width="5" maxlength="5" inputmode="numeric" style="min-width: 70px;">
                                        <i class="other-label"></i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>
                            <label class="answer block"><input class="skip" type="radio" name="q-pants" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>
                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_7"  v-if="navPage == 7"  class="question first is-current " data-type="radio">
                        <h2>
                            <span>07</span>Which best describes your midsection?</h2>
                        <div class="answers flex-col sm-2-col lg-4-col">

                            <label class="answer center"><input type="radio" name="q-midsection" value="0">
                                <span>
                                    <figure><img src="https://propercloth.com/images/size-survey/a.png" alt=""></figure>No belly at all</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-midsection" value="1">
                                <span>
                                    <figure><img src="https://propercloth.com/images/size-survey/b.png" alt=""></figure>Pretty fit</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-midsection" value="2">
                                <span>
                                    <figure><img src="https://propercloth.com/images/size-survey/c.png" alt=""></figure>Medium belly</span>
                            </label>
                            <label class="answer center"><input type="radio" name="q-midsection" value="3">
                                <span>
                                    <figure><img src="https://propercloth.com/images/size-survey/d.png" alt=""></figure>Significant</span>
                            </label>
                            <label class="answer center block"><input class="skip" type="radio" name="q-midsection" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_8"  v-if="navPage == 8" class="question  first is-current " data-type="input">
                        <header>
                            <h2>
                                <span>08</span>What is your collar size (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13" in-value="13" cm-value="35">
                                <span>13</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13.5" in-value="13.5" cm-value="36">
                                <span>13.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14" in-value="14" cm-value="37">
                                <span>14</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14.5" in-value="14.5" cm-value="38">
                                <span>14.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15" in-value="15" cm-value="39">
                                <span>15</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15.5" in-value="15.5" cm-value="40">
                                <span>15.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16" in-value="16" cm-value="41">
                                <span>16</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16.5" in-value="16.5" cm-value="42">
                                <span>16.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17" in-value="17" cm-value="43">
                                <span>17</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17.5" in-value="17.5" cm-value="44">
                                <span>17.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18" in-value="18" cm-value="45">
                                <span>18</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18.5" in-value="18.5" cm-value="46">
                                <span>18.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19" in-value="19" cm-value="47">
                                <span>19</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19.5" in-value="19.5" cm-value="48">
                                <span>19.5</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20" in-value="20" cm-value="49">
                                <span>20</span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20.5" in-value="20.5" cm-value="50">
                                <span>20.5</span>
                            </label>

                            <label class="answer block other"><input class="else" type="radio" name="q-collar" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="collar" type="number" width="5" maxlength="5" inputmode="numeric" style="min-width: 70px;">
                                        <i class="other-label"></i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>

                            <label class="answer block"><input class="skip" type="radio" name="q-collar" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_9"  v-if="navPage == 9" class="question first is-current  " data-type="input">
                        <header>
                            <h2>
                                <span>09</span>What is your sleeve length (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30" in-value="30" cm-value="79">
                                <span>30</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30.5" in-value="30.5" cm-value="80">
                                <span>30.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31" in-value="31" cm-value="81">
                                <span>31</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31.5" in-value="31.5" cm-value="82">
                                <span>31.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32" in-value="32" cm-value="83">
                                <span>32</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32.5" in-value="32.5" cm-value="84">
                                <span>32.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33" in-value="33" cm-value="85">
                                <span>33</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33.5" in-value="33.5" cm-value="86">
                                <span>33.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34" in-value="34" cm-value="87">
                                <span>34</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34.5" in-value="34.5" cm-value="88">
                                <span>34.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35" in-value="35" cm-value="89">
                                <span>35</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35.5" in-value="35.5" cm-value="90">
                                <span>35.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36" in-value="36" cm-value="91">
                                <span>36</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36.5" in-value="36.5" cm-value="92">
                                <span>36.5</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37" in-value="37" cm-value="93">
                                <span>37</span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37.5" in-value="37.5" cm-value="94">
                                <span>37.5</span>
                            </label>

                            <label class="answer block other"><input class="else" type="radio" name="q-sleeve" value="other">
                                <span class="other-input">
                                    <i>Something else:</i>
                                    <i class="other-wrap">
                                        <input data-what="sleeve" type="number" width="2" maxlength="5" inputmode="numeric" style="min-width: 70px;">
                                        <i class="other-label">in</i>
                                    </i>
                                </span>
                                <div class="invalid-msg"></div>
                            </label>

                            <label class="answer block"><input class="skip" type="radio" name="q-sleeve" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_10"  v-if="navPage == 10" class="question  first is-current " data-type="radio">
                        <h2>
                            <span>10</span>Do you tuck your dress shirts in?</h2>

                        <div class="answers flex-col lg-1-col md-1-col sm-1-col">
                            <label class="answer"><input type="radio" name="q-tucked" value="1">
                                <span>Always tucked</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-tucked" value="0">
                                <span>Always untucked</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-tucked" value="2">
                                <span>Both</span>
                            </label>
                            <label class="answer skip-wrap block"><input class="skip" type="radio" name="q-tucked" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next" @click="incrementPage()">Next</a>
                        </nav>
                    </section>

                    <section id="smart_size_step_11"  v-if="navPage == 11" class="question first is-current " data-type="radio">
                        <h2>
                            <span>11</span>How slim do you like your dress shirts to fit?</h2>

                        <div class="answers flex-col lg-1-col md-1-col sm-1-col">
                            <label class="answer"><input type="radio" name="q-style" value="0">
                                <span>Classic, casual fit, a bit loose and boxy</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-style" value="1">
                                <span>Office appropriate tailored fit, not too tight</span>
                            </label>
                            <label class="answer"><input type="radio" name="q-style" value="2">
                                <span>Uber stylish, very close to the body</span>
                            </label>
                            <label class="answer skip-wrap"><input class="skip" type="radio" name="q-style" value="" checked="checked">
                                <span>I&rsquo;m not sure, skip this question</span>
                            </label>
                        </div>

                        <nav class="q-nav">
                            <a href="#" class="btn prev" @click="decrementPage()">Prev</a>
                            <a href="#" class="btn next form-submit reveal-jump-1">Next</a>
                        </nav>
                    </section>

                </div>

                <aside class="sidebar">
                    <span class="back" href="#">
                        <span>&larr;</span> View Calculated Sizes</span>
                    <span class="back-review" href="#">
                        <span>&larr;</span> Review Answers</span>
                    <span class="back-change" href="#">
                        <span>&larr;</span> Change Answers</span>
                    <div class="title">
                        <h2 class="first">Find your
                            <span>Smart Size</span> with just a few easy questions.
                            <i>Almost done&hellip;</i>
                        </h2>
                        <h2 class="second">
                            <span>Create an account</span> to reveal your custom size.</h2>
                        <h2 class="third">Nice work.
                            <span>Your Smart Sizes are ready.</span>
                            <i>We’ve generated 3 sizes for you based on your answers.</i>
                        </h2>
                    </div>
                    <div class="survey-progress">
                        <svg width="88" height="88" viewBox="0 0 88 88" class="progress">
                            <circle class="progress-meter" cx="44" cy="44" r="36" stroke-width="12" />
                            <circle class="progress-value" cx="44" cy="44" r="36" stroke-width="12" stroke-dasharray="226.195" stroke-dashoffset="205.632" />
                        </svg>
                        <p>
                            <span class="current-q">1</span>/
                            <span></span>11</span>
                        </p>
                    </div>
                    <div class="calculating">
                        <span></span>
                        <p>Calculating...</p>
                    </div>
                </aside>

                <div class="ss-results" id="ss-results">
                    <div class="inner">
                        <div class="visible-sm visible-xs mob-back-links">
                            <span class="back-review" href="#">
                                <span>&larr;</span> Review Answers</span>
                            <span class="back-change" href="#">
                                <span>&larr;</span> Change Answers</span>
                        </div>
                        <section class="ss-dimensions" id="ss-dimensions">
                            <h5>Your Smart Size Dimensions</h5>
                            <div class="panel">
                                <div class="size-tabs">
                                    <a href="#results" class="is-active" ss-type="1">
                                        <span>Long Sleeve Tucked</span>
                                    </a>
                                    <a href="#results" ss-type="2">
                                        <span>Long Sleeve Untucked</span>
                                    </a>
                                    <a href="#results" ss-type="3">
                                        <span>Short Sleeve Untucked</span>
                                    </a>
                                </div>
                                <div class="list" id="size">
                                    <ul>
                                        <li>
                                            <span>Collar Around</span>
                                            <span data-what="collar"></span>
                                        </li>
                                        <li>
                                            <span>Sleeve Length</span>
                                            <span data-what="sleeve"></span>
                                        </li>
                                        <li class="hide">
                                            <span>Short Sleeve Length</span>
                                            <span data-what="short_sleeve_length"></span>
                                        </li>
                                        <li>
                                            <span>Yoke Width</span>
                                            <span data-what="yoke"></span>
                                        </li>
                                        <li>
                                            <span>Chest Width</span>
                                            <span data-what="chest"></span>
                                        </li>
                                        <li>
                                            <span>Midsection Width</span>
                                            <span data-what="midsection"></span>
                                        </li>
                                        <li>
                                            <span>Shirt Length</span>
                                            <span data-what="length"></span>
                                        </li>
                                        <li>
                                            <span>Sleeve Width</span>
                                            <span data-what="sleeve_width"></span>
                                        </li>
                                        <li>
                                            <span>Cuff Around</span>
                                            <span data-what="cuff"></span>
                                        </li>
                                        <li class="hide">
                                            <span>Short Sleeve Width</span>
                                            <span data-what="short_sleeve_width"></span>
                                        </li>
                                        <li class="hide">
                                            <span>Short Sleeve Opening</span>
                                            <span data-what="short_sleeve_opening_width"></span>
                                        </li>
                                        <p class="unit-note">
                                            <small>*All dimensions shown in
                                                <span>inches</span>
                                            </small>
                                        </p>
                                        <span class="show-all">More Size Details</span>
                                        <div>
                                            <li>
                                                <span>Bottom Width</span>
                                                <span data-what="bottom_width_value"></span>
                                            </li>
                                            <li>
                                                <span>Watch Allowance</span>
                                                <span data-what="cuff_watch_allowance"></span>
                                            </li>
                                            <li>
                                                <span>Shoulder Slope</span>
                                                <span data-what="shulders_slope"></span>
                                            </li>
                                            <li>
                                                <span>Forearm</span>
                                                <span data-what="forearm"></span>
                                            </li>
                                            <li>
                                                <span>Shoulder / Armpit Fit</span>
                                                <span data-what="shoulder_fit"></span>
                                            </li>
                                            <li>
                                                <span>Rear Pleats</span>
                                                <span data-what="rear_pleats"></span>
                                            </li>
                                            <li>
                                                <span>Back Darts</span>
                                                <span data-what="back_darts"></span>
                                            </li>
                                            <li>
                                                <span>Posture</span>
                                                <span data-what="posture"></span>
                                            </li>
                                            <li>
                                                <span>Top Button Placement</span>
                                                <span data-what="top_button_placement">Standard</span>
                                            </li>
                                            <li class="note">
                                                <p>You can fine-tune any of these dimensions later.</p>
                                            </li>
                                        </div>
                                    </ul>
                                </div>
                            </div>
                            <div class="action-btns">
                                <a href="#" class="btn btn-default-grey back-review">Review Answers</a>
                                <a href="https://propercloth.com/suggested/shirts/1" class="btn btn-default continue smartsizes_browse_shirts" id="smartsizes_answers">CONTINUE &rarr;</a>
                            </div>
                            <div class="why">
                                <section class="ranked">
                                    <h2>Top Ranked by Thousands of&nbsp;Customers</h2>
                                    <div class="verified">
                                        <div class="col">
                                            <img src="https://cdn.propercloth.com/images/create_a_size/6a_p3.png" class="stars">
                                            <img src="https://cdn.propercloth.com/images/get-started/perfect-fit/reviews-google-color.png" class="logos google">
                                            <p>
                                                <span>Based on Over </span>600
                                                <span class="show-sm-below">+</span> Google Reviews</p>
                                        </div>
                                        <div class="col">
                                            <img src="https://cdn.propercloth.com/images/create_a_size/6a_p3.png" class="stars">
                                            <img src="https://cdn.propercloth.com/images/get-started/perfect-fit/reviews-yelp-color.png" class="logos">
                                            <p>
                                                <span>Based on Over </span>450
                                                <span class="show-sm-below">+</span> Yelp Reviews</p>
                                        </div>
                                    </div>
                                </section>
                                <section class="pfg">
                                    <h5>Order Risk Free</h5>
                                    <h2>Perfect Fit Guaranteed</h2>
                                    <p>If you don’t absolutely love how your shirt fits, we’ll remake your shirt in an adjusted size or issue you a complete refund with no&nbsp;hassle.
                                    </p>
                                </section>
                                <section class="delivery">
                                    <h2>Order today for delivery by</h2>
                                    <h4>May 25 - May 30</h4>
                                    <p>(US, Canada &amp; Europe)</p>
                                </section>
                                <section class="quotes">
                                    <blockquote>
                                        &ldquo;Proper Cloth has become a go-to source for made-to-measure shirts for even the most discerning menswear&nbsp;customer.&rdquo;
                                        <img src="https://cdn.propercloth.com/images/home2/press/gq.png" height="36">
                                    </blockquote>
                                    <blockquote>
                                        &ldquo;The made-to-order shirting specialists at Proper Cloth may be more than happy to let you design your own custom creation, but they also offer up a few collections of pre-designed options each season. And we should all be happy that they do.&rdquo;
                                        <img src="https://cdn.propercloth.com/images/home2/press/esquire.png" height="26">
                                    </blockquote>
                                </section>
                            </div>
                        </section>
                        <section class="ss-answers" id="ss-answers">
                            <h5>Review Your Answers</h5>
                            <div class="panel">
                                <div class="list" id="size">
                                    <ul>
                                        <li class="answer-edit" data-what="smart_size_step_1">
                                            <span>
                                                <i>1</i> What size t-shirt fits you best?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_2">
                                            <span>
                                                <i>2</i> How tall are you?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_3">
                                            <span>
                                                <i>3</i> How much do you weigh?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_4">
                                            <span>
                                                <i>4</i> Which best describes your ethnicity?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_5">
                                            <span>
                                                <i>5</i> What is your suit jacket size?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_6">
                                            <span>
                                                <i>6</i> What is the waist size of your pants?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_7">
                                            <span>
                                                <i>7</i> Which best describes your midsection?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_8">
                                            <span>
                                                <i>8</i> What is your collar size?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_9">
                                            <span>
                                                <i>9</i> What is your sleeve length?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_10">
                                            <span>
                                                <i>10</i> Do you tuck your dress shirts in?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="answer-edit" data-what="smart_size_step_11">
                                            <span>
                                                <i>11</i> How slim do you like your dress shirts to fit?</span>
                                            <span>

                                                <span>Change</span>
                                            </span>
                                        </li>
                                        <li class="note">
                                            <p>Choose any question above to change your answer.</p>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="action-btns">
                                <a href="#" class="btn btn-default-grey back">View Calculated Sizes</a>
                                <a href="https://propercloth.com/suggested/shirts/1" class="btn btn-default continue smartsizes_browse_shirts" id="smartsizes_answers">CONTINUE &rarr;</a>
                                <a href="#" class="btn btn-default confirm-and-calc">Continue &rarr;</a>
                            </div>
                            <div class="why">
                                <section class="ranked">
                                    <h2>Top Ranked by Thousands of&nbsp;Customers</h2>
                                    <div class="verified">
                                        <div class="col">
                                            <img src="https://cdn.propercloth.com/images/create_a_size/6a_p3.png" class="stars">
                                            <img src="https://cdn.propercloth.com/images/get-started/perfect-fit/reviews-google-color.png" class="logos google">
                                            <p>
                                                <span>Based on Over </span>600
                                                <span class="show-sm-below">+</span> Google Reviews</p>
                                        </div>
                                        <div class="col">
                                            <img src="https://cdn.propercloth.com/images/create_a_size/6a_p3.png" class="stars">
                                            <img src="https://cdn.propercloth.com/images/get-started/perfect-fit/reviews-yelp-color.png" class="logos">
                                            <p>
                                                <span>Based on Over </span>450
                                                <span class="show-sm-below">+</span> Yelp Reviews</p>
                                        </div>
                                    </div>
                                </section>
                                <section class="pfg">
                                    <h5>Order Risk Free</h5>
                                    <h2>Perfect Fit Guaranteed</h2>
                                    <p>If you don’t absolutely love how your shirt fits, we’ll remake your shirt in an adjusted size or issue you a complete refund with no&nbsp;hassle.
                                    </p>
                                </section>
                                <section class="delivery">
                                    <h2>Order today for delivery by</h2>
                                    <h4>May 25 - May 30</h4>
                                    <p>(US, Canada &amp; Europe)</p>
                                </section>
                                <section class="quotes">
                                    <blockquote>
                                        &ldquo;Proper Cloth has become a go-to source for made-to-measure shirts for even the most discerning menswear&nbsp;customer.&rdquo;
                                        <img src="https://cdn.propercloth.com/images/home2/press/gq.png" height="36">
                                    </blockquote>
                                    <blockquote>
                                        &ldquo;The made-to-order shirting specialists at Proper Cloth may be more than happy to let you design your own custom creation, but they also offer up a few collections of pre-designed options each season. And we should all be happy that they do.&rdquo;
                                        <img src="https://cdn.propercloth.com/images/home2/press/esquire.png" height="26">
                                    </blockquote>
                                </section>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
            <div class="display-none">
                <input type="text" id="collar_field" value="0.00" />
                <input type="text" id="sleeve_field" value="0.00" />
                <input type="text" id="yoke_field" value="0.00" />
                <input type="text" id="chest_field" value="0.00" />
                <input type="text" id="midsection_field" value="0.00" />
                <input type="text" id="length_field" value="0.00" />
                <input type="text" id="sleeve_w_field" value="0.00" />
                <input type="text" id="short_sleeve_length_field" value="0.00" />
                <input type="text" id="short_sleeve_width_field" value="0.00" />
                <input type="text" id="short_sleeve_opening_width_field" value="0.00" />
                <input type="text" id="cuff_field" value="0.00" />
                <input type="text" id="adddim_bottom_width_field" value="0.00" />
                <input name="adddim_method_field" id="adddim_method_field_default" type="radio" value="default" />
                <input name="adddim_method_field" id="adddim_method_field_override" type="radio" value="override" />
                <select id="adddim_cuff_watch_allowance_field">
                    <option value="none">None</option>
                    <option value="+25leftcuff">+0.25" Left Cuff</option>
                    <option value="+5leftcuff">+0.5" Left Cuff</option>
                    <option value="+75leftcuff">+0.75" Left Cuff</option>
                    <option value="+25rightcuff">+0.25" Right Cuff</option>
                    <option value="+5rightcuff">+0.5" Right Cuff</option>
                    <option value="+75rightcuff">+0.75" Right Cuff</option>
                </select>
                <select id="adddim_shulders_slope_field">
                    <option value="normal">Normal</option>
                    <option value="square">Square Shoulders</option>
                    <option value="sloping">Sloping Shoulders</option>
                    <option value="verysloping">Very Sloping Shoulders</option>
                    <option value="veryverysloping">Very Very Sloping Shoulders</option>
                    <option value="verysquare">Very Square Shoulders</option>
                    <option value="veryverysquare">Very Very Square Shoulders</option>
                </select>
                <select id="adddim_forearm_field">
                    <option value="slim">One Pleat</option>
                    <option value="traditional">Two Pleats</option>
                    <option value="three">Three Pleats</option>
                </select>
                <select id="adddim_shoulder_fit_field">
                    <option value="full">Full (default)</option>
                    <option value="tailored">Tailored</option>
                </select>
                <select id="adddim_rear_pleats_field">
                    <option value="none">None (default)</option>
                    <option value="side_pleats">Side Pleats</option>
                    <option value="center_box_pleat">Center Box Pleat</option>
                </select>
                <select id="adddim_posture_field">
                    <option value="standard">Normal (default)</option>
                    <option value="back_1_2">Neck Back 1/2"</option>
                    <option value="back_1">Neck Back 1"</option>
                    <option value="forward_1_2">Neck Forward 1/2"</option>
                    <option value="forward_1">Neck Forward 1"</option>
                </select>
                <select id="adddim_back_darts_field">
                    <option value="none">None (default)</option>
                    <option value="yes">Yes</option>
                </select>
                <input type="text" id="adddim_buttons_on_shirt_front_field" value="8">
            </div>
        </div>

        <div id="loader">
            <img src="https://propercloth.com/images/washed_italian_denim/SS_Charcoal_100.gif" width="50" height="50">
        </div>
        <div id="modal_window" class="modal in">
            <div class="content modal-dialog modal-lg">
                <div class="content-inside modal-content">
                    <div id="mw_signin_register_form">
                        <div class="modal-header">
                            <button type="button" class="close" aria-label="Close">
                                <span aria-hidden="true">×</span>
                            </button>
                            <h4 class="modal-title">Sign In / Register</h4>
                        </div>
                        <div class="modal-body">
                            <form class="form-horizontal" role="form">
                                <div class="form-group form-custom">
                                    <label for="mw_email" class="col-xs-3 col-sm-2 col-lg-2 control-label">EMAIL</label>
                                    <div class="col-xs-9 col-sm-10 col-lg-10 control-area">
                                        <input type="email" class="form-control" id="mw_email">
                                    </div>
                                </div>
                                <div class="form-group form-custom">
                                    <label for="mw_password" class="col-xs-3 col-sm-2 col-lg-2 control-label">PASSWORD</label>
                                    <div class="col-xs-9 col-sm-10 col-lg-10 control-area">
                                        <input type="password" class="form-control" id="mw_password">
                                    </div>
                                </div>
                                <div class="form-group form-custom no-border">
                                    <div id="captcha_container"></div>
                                </div>
                            </form>
                            <div class="row">
                                <div class="col-xs-6 padding-0 padding-right-5">
                                    <button type="button" class="btn btn-default btn-width-all CreateAccount" id="mw_buttonCreateAccountConfirm">REGISTER</button>
                                </div>
                                <div class="col-xs-6 padding-0 padding-left-5 align-center">
                                    <button type="button" class="btn btn-default btn-width-all" id="mw_buttonSignInConfirm">SIGN IN</button>
                                    <input type="hidden" class="form-control" id="mw_with_refresh" value="yes">
                                    <p id="mw_forgot_password" class="mw_text display-none">
                                        <a href="#">Forgot your password?</a>
                                    </p>
                                </div>
                            </div>
                            <input type="hidden" id="mw_inp_sp" name="mw_inp_sp" value="sp_say_not" />
                            <p>
                                <div class="message-danger mw_text margin-top-0-imp"></div>
                            </p>
                        </div>
                    </div>
                    <div id="mw_forgot_password_form" class="display-none">
                        <div class="modal-header">
                            <button type="button" class="close" aria-label="Close">
                                <span aria-hidden="true">×</span>
                            </button>
                            <h4 class="modal-title">RESET PASSWORD</h4>
                        </div>
                        <div class="modal-body">
                            <form class="form-horizontal" role="form">
                                <div class="form-group form-custom">
                                    <label for="email_field" class="col-xs-3 col-sm-2 col-lg-1 control-label">EMAIL</label>
                                    <div class="col-xs-9 col-sm-10 col-lg-11 control-area">
                                        <input type="email_field" class="form-control" id="mw_email_forgot" value="">
                                    </div>
                                </div>
                            </form>
                            <div class="indent-20"></div>
                            <div class="row">
                                <div class="col-xs-6 padding-0 padding-right-5">
                                    <button type="button" class="btn btn-default-grey btn-width-all mw_close">CANCEL</button>
                                </div>
                                <div class="col-xs-6 padding-0 padding-left-5 align-center">
                                    <button type="button" class="btn btn-default btn-width-all" id="mw_buttonResetPassword">
                                        <div class="hidden-xxs">RESET PASSWORD</div>
                                        <div class="visible-xxs">RESET</div>
                                    </button>
                                </div>
                            </div>
                            <input type="hidden" id="inp_sp" name="inp_sp" value="sp_say_not" />
                            <div class="indent-30">
                                <div class="indent-5"></div>
                                <div class="message-danger margin-top-0-imp"></div>
                            </div>
                            <div class="align-center">
                                We'll email you a new password.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <span class="nav-shade"></span>
        <div class="indent-20"></div>

        </div>
        </div>
    </div>
</template>
<script>
export default {
    data: function() {
        return {
            size: '',
            navPage: 1
        }
    },
    methods: {
        incrementPage: function() {
            
            this.navPage = this.navPage + 1;
            console.log(this.navPage);
            console.log(this.size);
        },
        decrementPage: function() {
            this.navPage = this.navPage - 1;
        }
    }
}
</script>