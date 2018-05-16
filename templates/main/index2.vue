<template>
        <div class="ss-app">
              <div class="size-survey" data-format="us">
                    <section  v-if="navPage == 1" class="question first is-current " data-type="radio">
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

                    <section v-if="navPage == 2" class="question  first is-current " data-type="input">
                        <header>
                            <h2>
                                <span>02</span>How tall are you?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="US" data-measure-metric="EU">
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_4" in-value="5&prime;4&Prime;" cm-value="166">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_5" in-value="5&prime;5&Prime;" cm-value="168">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_6" in-value="5&prime;6&Prime;" cm-value="170">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_7" in-value="5&prime;7&Prime;" cm-value="172">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_8" in-value="5&prime;8&Prime;" cm-value="174">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_9" in-value="5&prime;9&Prime;" cm-value="176">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_10" in-value="5&prime;10&Prime;" cm-value="178">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_11" in-value="5&prime;11&Prime;" cm-value="180">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_0" in-value="6&prime;0&Prime;" cm-value="182">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_1" in-value="6&prime;1&Prime;" cm-value="184">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_2" in-value="6&prime;2&Prime;" cm-value="186">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_3" in-value="6&prime;3&Prime;" cm-value="188">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_4" in-value="6&prime;4&Prime;" cm-value="190">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_5" in-value="6&prime;5&Prime;" cm-value="192">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_6" in-value="6&prime;6&Prime;" cm-value="194">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_7" in-value="6&prime;7&Prime;" cm-value="196">
                                <span></span>
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
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="155" in-value="155" cm-value="72">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="160" in-value="160" cm-value="74">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="165" in-value="165" cm-value="76">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="170" in-value="170" cm-value="78">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="175" in-value="175" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="180" in-value="180" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="185" in-value="185" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="190" in-value="190" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="195" in-value="195" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="200" in-value="200" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="205" in-value="205" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="210" in-value="210" cm-value="94">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="215" in-value="215" cm-value="96">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="220" in-value="220" cm-value="98">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="225" in-value="225" cm-value="100">
                                <span></span>
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

                    <section id="smart_size_step_4"  v-if="navPage == 4" class="question  " data-type="radio">
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

                        <p class="help">
                            <a href="#">Why do we ask?</a>
                        </p>
                    </section>

                    <section id="smart_size_step_5"  v-if="navPage == 5" class="question  suit-size " data-type="input">
                        <header>
                            <h2>
                                <span>05</span>What is your suit jacket size (
                                <i data-text-eu="EU Sizing" data-text-us="if you know it">if you know it</i>)?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col">
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="36" in-value="36" cm-value="46">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="37" in-value="37" cm-value="47">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="38" in-value="38" cm-value="48">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="39" in-value="39" cm-value="49">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="40" in-value="40" cm-value="50">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="41" in-value="41" cm-value="51">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="42" in-value="42" cm-value="52">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="43" in-value="43" cm-value="53">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="44" in-value="44" cm-value="54">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="45" in-value="45" cm-value="55">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="46" in-value="46" cm-value="56">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="47" in-value="47" cm-value="57">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="48" in-value="48" cm-value="58">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="49" in-value="49" cm-value="59">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="50" in-value="50" cm-value="60">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="51" in-value="51" cm-value="61">
                                <span></span>
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

                    <section id="smart_size_step_6"   v-if="navPage == 6" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>06</span>What is the waist size of your&nbsp;pants?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="27" in-value="27" cm-value="74">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="28" in-value="28" cm-value="76">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="29" in-value="29" cm-value="78">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="30" in-value="30" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="31" in-value="31" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="32" in-value="32" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="33" in-value="33" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="34" in-value="34" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="35" in-value="35" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="36" in-value="36" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="37" in-value="37" cm-value="94">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="38" in-value="38" cm-value="96">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="39" in-value="39" cm-value="98">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="40" in-value="40" cm-value="100">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="41" in-value="41" cm-value="102">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="42" in-value="42" cm-value="104">
                                <span></span>
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

                    <section id="smart_size_step_7"  v-if="navPage == 7"  class="question  " data-type="radio">
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

                    <section id="smart_size_step_8"  v-if="navPage == 8" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>08</span>What is your collar size (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13" in-value="13" cm-value="35">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13.5" in-value="13.5" cm-value="36">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14" in-value="14" cm-value="37">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14.5" in-value="14.5" cm-value="38">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15" in-value="15" cm-value="39">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15.5" in-value="15.5" cm-value="40">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16" in-value="16" cm-value="41">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16.5" in-value="16.5" cm-value="42">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17" in-value="17" cm-value="43">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17.5" in-value="17.5" cm-value="44">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18" in-value="18" cm-value="45">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18.5" in-value="18.5" cm-value="46">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19" in-value="19" cm-value="47">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19.5" in-value="19.5" cm-value="48">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20" in-value="20" cm-value="49">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20.5" in-value="20.5" cm-value="50">
                                <span></span>
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

                    <section id="smart_size_step_9"  v-if="navPage == 9" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>09</span>What is your sleeve length (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30" in-value="30" cm-value="79">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30.5" in-value="30.5" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31" in-value="31" cm-value="81">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31.5" in-value="31.5" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32" in-value="32" cm-value="83">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32.5" in-value="32.5" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33" in-value="33" cm-value="85">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33.5" in-value="33.5" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34" in-value="34" cm-value="87">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34.5" in-value="34.5" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35" in-value="35" cm-value="89">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35.5" in-value="35.5" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36" in-value="36" cm-value="91">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36.5" in-value="36.5" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37" in-value="37" cm-value="93">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37.5" in-value="37.5" cm-value="94">
                                <span></span>
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

                    <section id="smart_size_step_10"  v-if="navPage == 10" class="question  " data-type="radio">
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

                    <section id="smart_size_step_11"  v-if="navPage == 11" class="question  " data-type="radio">
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
                <!--
            <div  class="survey-wrap ">
                <a class="current-unit sm-only" href="#">US</a>
                <div class="ss-unit-toggle global-toggle">
                    <a class="unit-us"   href="#">
                        <span>US</span>
                    </a>
                    <a class="unit-metric"   href="#">
                        <span>Metric</span>
                    </a>
                </div>
                <!--
                <div class="survey-progress at-top">
                    <p>
                        <span class="current-q">{{navPage}}</span>
                        <span></span>11</span>
                    </p>
                </div>
                <span class="progress-bar at-top">
                    <span class="progress-bar-progress">&nbsp;</span>
                </span>
                
                <div class="size-survey" data-format="us">
                    <section id="smart_size_step_1" v-if="navPage == 2" class="question first is-current " data-type="radio">
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

                    <section id="smart_size_step_1"   v-if="navPage == 1" class="question  height " data-type="input">
                        <header>
                            <h2>
                                <span>02</span>How tall are you?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="US" data-measure-metric="EU">
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_4" in-value="5&prime;4&Prime;" cm-value="166">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_5" in-value="5&prime;5&Prime;" cm-value="168">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_6" in-value="5&prime;6&Prime;" cm-value="170">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_7" in-value="5&prime;7&Prime;" cm-value="172">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_8" in-value="5&prime;8&Prime;" cm-value="174">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_9" in-value="5&prime;9&Prime;" cm-value="176">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_10" in-value="5&prime;10&Prime;" cm-value="178">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="5_11" in-value="5&prime;11&Prime;" cm-value="180">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_0" in-value="6&prime;0&Prime;" cm-value="182">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_1" in-value="6&prime;1&Prime;" cm-value="184">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_2" in-value="6&prime;2&Prime;" cm-value="186">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_3" in-value="6&prime;3&Prime;" cm-value="188">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_4" in-value="6&prime;4&Prime;" cm-value="190">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_5" in-value="6&prime;5&Prime;" cm-value="192">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_6" in-value="6&prime;6&Prime;" cm-value="194">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="height" type="radio" name="q-height" value="6_7" in-value="6&prime;7&Prime;" cm-value="196">
                                <span></span>
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

                    <section id="smart_size_step_3"  v-if="navPage == 3" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>03</span>How much do you weigh?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="lbs" data-measure-metric="kg">
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="150" in-value="150" cm-value="70">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="155" in-value="155" cm-value="72">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="160" in-value="160" cm-value="74">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="165" in-value="165" cm-value="76">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="170" in-value="170" cm-value="78">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="175" in-value="175" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="180" in-value="180" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="185" in-value="185" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="190" in-value="190" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="195" in-value="195" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="200" in-value="200" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="205" in-value="205" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="210" in-value="210" cm-value="94">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="215" in-value="215" cm-value="96">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="220" in-value="220" cm-value="98">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="weight" type="radio" name="q-weight" value="225" in-value="225" cm-value="100">
                                <span></span>
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

                    <section id="smart_size_step_4"  v-if="navPage == 4" class="question  " data-type="radio">
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

                        <p class="help">
                            <a href="#">Why do we ask?</a>
                        </p>
                    </section>

                    <section id="smart_size_step_5"  v-if="navPage == 5" class="question  suit-size " data-type="input">
                        <header>
                            <h2>
                                <span>05</span>What is your suit jacket size (
                                <i data-text-eu="EU Sizing" data-text-us="if you know it">if you know it</i>)?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col">
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="36" in-value="36" cm-value="46">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="37" in-value="37" cm-value="47">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="38" in-value="38" cm-value="48">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="39" in-value="39" cm-value="49">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="40" in-value="40" cm-value="50">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="41" in-value="41" cm-value="51">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="42" in-value="42" cm-value="52">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="43" in-value="43" cm-value="53">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="44" in-value="44" cm-value="54">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="45" in-value="45" cm-value="55">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="46" in-value="46" cm-value="56">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="47" in-value="47" cm-value="57">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="48" in-value="48" cm-value="58">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="49" in-value="49" cm-value="59">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="50" in-value="50" cm-value="60">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="jacket_size" type="radio" name="q-jacket" value="51" in-value="51" cm-value="61">
                                <span></span>
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

                    <section id="smart_size_step_6"   v-if="navPage == 6" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>06</span>What is the waist size of your&nbsp;pants?</h2>
                        </header>
                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="27" in-value="27" cm-value="74">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="28" in-value="28" cm-value="76">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="29" in-value="29" cm-value="78">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="30" in-value="30" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="31" in-value="31" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="32" in-value="32" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="33" in-value="33" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="34" in-value="34" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="35" in-value="35" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="36" in-value="36" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="37" in-value="37" cm-value="94">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="38" in-value="38" cm-value="96">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="39" in-value="39" cm-value="98">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="40" in-value="40" cm-value="100">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="41" in-value="41" cm-value="102">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="pants_waist" type="radio" name="q-pants" value="42" in-value="42" cm-value="104">
                                <span></span>
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

                    <section id="smart_size_step_7"  v-if="navPage == 7"  class="question  " data-type="radio">
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

                    <section id="smart_size_step_8"  v-if="navPage == 8" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>08</span>What is your collar size (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13" in-value="13" cm-value="35">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="13.5" in-value="13.5" cm-value="36">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14" in-value="14" cm-value="37">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="14.5" in-value="14.5" cm-value="38">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15" in-value="15" cm-value="39">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="15.5" in-value="15.5" cm-value="40">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16" in-value="16" cm-value="41">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="16.5" in-value="16.5" cm-value="42">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17" in-value="17" cm-value="43">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="17.5" in-value="17.5" cm-value="44">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18" in-value="18" cm-value="45">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="18.5" in-value="18.5" cm-value="46">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19" in-value="19" cm-value="47">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="19.5" in-value="19.5" cm-value="48">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20" in-value="20" cm-value="49">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="collar" type="radio" name="q-collar" value="20.5" in-value="20.5" cm-value="50">
                                <span></span>
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

                    <section id="smart_size_step_9"  v-if="navPage == 9" class="question  " data-type="input">
                        <header>
                            <h2>
                                <span>09</span>What is your sleeve length (if you know it)?</h2>
                        </header>

                        <div class="answers flex-col lg-4-col sm-4-col" data-measure-us="in" data-measure-metric="cm">
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30" in-value="30" cm-value="79">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="30.5" in-value="30.5" cm-value="80">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31" in-value="31" cm-value="81">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="31.5" in-value="31.5" cm-value="82">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32" in-value="32" cm-value="83">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="32.5" in-value="32.5" cm-value="84">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33" in-value="33" cm-value="85">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="33.5" in-value="33.5" cm-value="86">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34" in-value="34" cm-value="87">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="34.5" in-value="34.5" cm-value="88">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35" in-value="35" cm-value="89">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="35.5" in-value="35.5" cm-value="90">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36" in-value="36" cm-value="91">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="36.5" in-value="36.5" cm-value="92">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37" in-value="37" cm-value="93">
                                <span></span>
                            </label>
                            <label class="answer center"><input data-what="sleeve" type="radio" name="q-sleeve" value="37.5" in-value="37.5" cm-value="94">
                                <span></span>
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

                    <section id="smart_size_step_10"  v-if="navPage == 10" class="question  " data-type="radio">
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

                    <section id="smart_size_step_11"  v-if="navPage == 11" class="question  " data-type="radio">
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

                </div>-->

            </div>
        </div>
     
</template>
<script>
export default {
    data: function() {
        return {
            size: '',
            navPage: 1,
        }
    },
    methods: {
        incrementPage: function() {
            this.navPage = this.navPage + 1;
            console.log(this.navPage);
        },
        decrementPage: function() {
            this.navPage = this.navPage - 1;
        }
    }
}
</script>