% Arash's coursework template (Thanks Jamie Gabbay)
%

% Ziyad, H00296507  <--- so we know who you are
% F28PL Coursework, Prolog    <--- sanity check


% Due: Friday 6th of Dec, 2019, at 3:30pm sharp.
% Submit (this file) via GitLab as usual.
% This coursework constitutes 6% of your final F28PL mark.

% You may assume variables, procedures, and functions defined in earlier questions
% in your answers to later questions, though you should add comments in code explaining
% this if any clarification might help read your code.


/* For All Questions, include testing in comments, so your marker can load this file as a
database then cut-and-paste any testing into the command line.

Testing on GitLab will NOT be provided for prolog. Your own test will in this case be
 marked - note this is unlike the python coursework.

*/

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 1   <--- Yes, so we know what question you think you're answering
%
% The complex numbers are explained here (and elsewhere):
%  http://www.mathsisfun.com/algebra/complex-number-multiply.html
% Represent a complex integer as a two-element list of integers, so [4,5] represents 4+5i.
% Write Prolog predicates
%  cadd/3
%  cmult/3
% representing complex integer addition and multiplication. Thus for instance,
%  cadd([X1,X2],[Y1,Y2],[Z1,Z2])
% succeeds if and only if Z1=X1+Y1 and Z2=X2+Y2.
% Note that complex number multiplication is not just like complex number addition.
% Check the link and read the definition.
%
%   <--- always have the question under your nose



cadd([X1,X2],[Y1,Y2],[Z1,Z2]) :- Z1 is X1 + Y1, Z2 is X2 + Y2.  % simple addition of two lists of same size, returning the sum of the same index of both lists
cmult([X1,X2],[Y1,Y2],[Z1,Z2]) :- Z1 is X1*Y1 - X2*Y2, Z2 is X1*Y2 + X2*Y1. % same as addition, except the calculation method is different for multiplying



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 2
%
% An integer sequence is a list of integers. Write a Prolog predicate
%  seqadd/3
% such that seqadd(X,Y,Z) succeeds when X and Y are lists of integers of the same length and
% Z is their sequence sum.


seqadd([],[],[]). % first of all setting 3 empty lists before
seqadd([X1|Y1],[X2|Y2],[Z1|Z2]) :- Z1 is X1 + X2, seqadd(Y1,Y2,Z2). % the | symbol seperates the head from the tail of the list
% first of all add the head elements of both lists, then recursively add the tail elements and put both into the result


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 3
%
% 3a. Explain what backtracking has to do with Prolog. You might find this webpage helpful:
% https://www.doc.gold.ac.uk/~mas02gw/prolog_tutorial/prologpages/search.html
%
% 3b. What is Cut in prolog and what does it have to do with backtracking? Explain your answer by giving examples of Cut
% used in at least one prolog rule, and explain how it affects the execution/resolution process.
%

%                               Backtracking

%   Backtracking in Prolog is essentially another form of searching. In Prolog,
%   when a rule (for example) has to satisfy a goal X1 and a goal X2, Prolog
%   first of all has to 'look back' and try to look for variables/other rules
%   that would allow X1 to be satisfied. After X1 is satisfied, it then continues
%   to backtrack to try and satisfy the goal X2. 
%   Here is an example:

oldenough(james).
oldenough(jane).
oldenough(john).

hasmoney(john).

can_enter_club(X) :- oldenough(X), hasmoney(X).

%   In this example, we are trying to see who can enter a club. You can only 
%   enter if you are old enough and have enough money. 3 people are old enough
%   but only one has enough money. So when can_enter_club(X) is ran, it will first
%   attempt to see who is old enough. it will first go to James, who passes the
%   old enough test. But then it tries to see if he has enough money, and he
%   doesn't, so it would fail. It will now backtrack. It will go to Jane, and
%   the same will happen to her as it did with James as she also does not have
%   enough. Then it will backtrack again and will go to John, and both will pass
%   as he also has enough money, so when the rule is ran it will output:
%                           X = john.


%                                    Cut
%   In prolog Cut is another feature which can be used during backtracking. The
%   symbol for cut is an exclamation mark (!) and what it does is that it stops
%   the backtracking of a rule whenever the cut is reached. This is something
%   that is easier explained with examples. I will make 2 rules which check for
%   the biggest number between two numbers:

biggestnum(X,Y,Y) :- X<Y.
biggestnum(X,Y,X) :- Y<X.

%   So these two rules will either return X or Y depending on which number is
%   bigger using backtracking. However, there is a different way you can do it
%   using cut:

biggestnumtwo(X,Y,Y) :- X<Y, !.
biggestnumtwo(X,Y,X).

%   So what this does, is that it first of all checks if Y is bigger than X. If
%   it is, then the rule has been satisfied. However, if Y is not bigger than X,
%   then cut will be used to prevent backtracking and will automatically move on
%   to the second rule, stating that X is bigger than Y. Doing this allows the
%   rules to be satisfied faster, as it does not need to continually backtrack
%   to satsify the rule.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 4
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Question 4
%
% Write a database for a predicate cycleoflife/1 such that the query
%  cycleoflife(X)
% returns the instantiations
%  X = eat
%  X = sleep
%  X = code
%  X = eat
%  X = sleep
%  X = code
%  ...
% in an endless cycle.
% (This question has a beautiful and simple answer. If you find yourself writing lines and lines of
% complex code, there’s probably something amiss.)

cycle1(eat).
cycle2(sleep). % making the 3 different cycles
cycle3(code).
cycleoflife(X) :- cycle1(X). % calling first cycle 'eat'
cycleoflife(X) :- cycle2(X). % calling second cycle 'sleep'
cycleoflife(X) :- cycle3(X). % calling third cycle 'code'
cycleoflife(X) :- cycleoflife(X). % calling cycleoflife again which allows it to loop over all the cycles again

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% END ANSWER TO Question 5
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
