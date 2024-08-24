# [level 1] Failure rate - 42889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42889) 

### 성능 요약

메모리: 10.3 MB, 시간: Passed 0.01 ms

### 구분

Coding test practice > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 23일 23:03:27

### 문제 설명

<h2><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Failure rate</font></font></h2>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/bde471d8ac/48ddf1cc-c4ea-499d-b431-9727ee799191.png" title="" alt="failture_rate1.png"></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Super game developer Oreli was in deep trouble. Her game, Friends Ocheonseong, was a huge success, but the number of new users was rapidly decreasing. The reason was that the stage gap between new users and existing users was too big.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">She was wondering how to solve this problem, so she decided to adjust the difficulty by dynamically increasing the game time. As expected of a super developer, she easily implemented most of the logic, but she ran into a crisis when it came to calculating the failure rate. Complete the code to calculate the failure rate for Aurelie.</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The failure rate is defined as follows:

</font></font><ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Number of players who have reached the stage but not yet cleared it / Number of players who have reached the stage</font></font></li>
</ul></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Complete the solution function so that it returns an array of stage numbers in descending order, starting with the stage with the highest failure rate, when given as parameters the number of stages N and an array stages containing the number of the stage on which the user playing the game is currently stopped.</font></font></p>

<h5><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Restrictions</font></font></h5>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The number of stages, N, is a natural number </font></font><code>1</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">less than </font></font><code>500</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">or equal to .</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The length of stages is </font></font><code>1</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">greater than or </font></font><code>200,000</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">equal to .</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">stages </font><font style="vertical-align: inherit;">contains natural numbers greater than

 </font></font><code>1</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">or equal to .</font></font><code>N + 1</code><font style="vertical-align: inherit;"></font><ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Each natural number represents the number of the stage the user is currently challenging.</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">However, </font></font><code>N + 1</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">indicates a user who has cleared the last stage (Nth stage).</font></font></li>
</ul></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">If there are stages with the same failure rate, the stage with the lower number should come first.</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">If no user has reached a stage, the failure rate of that stage </font></font><code>0</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">is defined as .</font></font></li>
</ul>

<h5><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input/output example</font></font></h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>stages</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>[2, 1, 2, 6, 2, 4, 3, 3]</td>
<td>[3,4,2,1,5]</td>
</tr>
<tr>
<td>4</td>
<td>[4,4,4,4,4]</td>
<td>[4,1,2,3]</td>
</tr>
</tbody>
      </table>
<h5><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input/output example explanation</font></font></h5>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input/Output Example #1 </font></font><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
A total of 8 users have attempted Stage 1, and 1 user has not cleared it yet. Therefore, the failure rate for Stage 1 is as follows.</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stage 1 failure rate: 1/8</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A total of 7 users have attempted Stage 2, and 3 of them have not cleared it yet. Therefore, the failure rate for Stage 2 is as follows.</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stage 2 failure rate: 3/7</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Similarly, the failure rates for the remaining stages are as follows:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stage 3 failure rate: 2/4</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stage 4 failure rate: 1/2</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Stage 5 failure rate: 0/1</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The numbers for each stage are sorted in descending order of failure rate as follows:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[3,4,2,1,5]</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input/Output Example #2</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Since all users are at the last stage, the failure rate for stage 4 is 1 and the failure rates for the remaining stages are 0.</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[4,1,2,3]</font></font></li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges