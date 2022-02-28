
set.seed(5000)

#Oppgave 1a)
n = 1000 #angir antall verdier som skal genereres 
df = 6 #frihetsgrader
b = 50
x = rchisq(n, df)

hist(x, breaks = b, prob = T)

xs = seq(0, 25, l=100)
lines(xs, y = dchisq(xs, df=df), col = "red", lwd = 4) #teoretisk tetthet

#Oppgave 1bi) 
x1 = rnorm(6)
y1 = sum(x1^2)
print(x1)

print(y1)

#Oppgave 1bii)
yb = replicate(n, sum(rnorm(6)**2))

hist(yb, freq = FALSE,  xlim = c(0,20), breaks = b, prob = T, col = "lightblue")

ys = seq(0,20, l = 100)
lines(ys, y = dchisq(ys, df = df), col = "black", lwd = 4) #teoretisk tetthet

#oppgave 1c 
par(mfrow = c(1,2))

hist(x, breaks = b, prob = T)

xs = seq(0, 25, l=100)
lines(xs, y = dchisq(xs, df=df), col = "red", lwd = 4) #teoretisk tetthet

hist(yb, freq = FALSE,  xlim = c(0,20), breaks = b, prob = T, col = "lightblue")

ys = seq(0,20, l = 100)
lines(ys, y = dchisq(ys, df = df), col = "black", lwd = 4) #teoretisk tetthet


#Oppgave 2a
b2 = 100
z = rlnorm(1000)
hist(z, breaks = b2, xlim = c(0,15), freq = FALSE, col = "lightblue", prob = T)

zs = seq(0,15, l = 100)
lines(zs, y = dlnorm(zs), col = "black", lwd = 2)

#Oppgave 2b 
#dersom z er lognormal fordelt, vil logaritmen av Z være normalfordelt
#må komme os fra lognormalfordelte variabler til normalfordelte variable 

y = log(z)

hist(y, breaks = b, prob = T)

ys = seq(-3,3 , l = 100)
lines(ys, y = dnorm(ys), lwd = 4)

var = sd(y)^2
mean = mean(y)

m = matrix(c(mean, var), ncol=2)
colnames(m) = c("forventning", "varians")

print(m)

#oppgave 2c
#sammenligne histogrammen, kan bekrefte av at ved å ta logaritmen til alle observasjonene i a 
#vil verdiene i b bli normalfordelte, ved å se på histogrammene. 
par(mfrow = c(1,2))

#historgrammet i a 
hist(z, breaks = b2, xlim = c(0,15), freq = FALSE, col = "lightblue", prob = T)
lines(zs, y = dlnorm(zs), col = "black", lwd = 4)
#historgammet i b
hist(y, breaks = b, prob = T)
lines(ys, y = dnorm(ys), lwd = 4)

#Oppgave 3
#ai
m = 5 #antall observasjoner 
theta = 9 

x = runif(n = 5, min = 0, max = theta)
y = max(x)
print(y)

#aii
yb = replicate(n = 1000, max(runif(n = 5, min = 0, max = theta)))

hist(yb, breaks = 50,  prob = T)
#må regne ut tettheten til det ordnende utvalget her
y_seq = seq(0, theta, l =100)
lines(y_seq, 5*y_seq^4*theta^(-5), col = "red", lwd = 2)

#b 
par(mfrow = c(1,2))

func = function(theta, n = 1000, m = 5 ){
  y8 = replicate(n=n, max(runif(n = m, min = 0, max = theta)))
  
  hist(y8, 
       breaks = 50, 
       prob = T, 
       main = paste("theta =", as.character(theta)))
  
  seq = seq(0, theta, l = 100)
  lines(seq, 5*seq^4*theta^(-5), col = "red", lwd = 2) 
}

func(2)
func(30) 



#oppgave 4 
#a
p = 20 #antall observasjoner
varians = 3 #valgt verdi

y4 = rnorm(n = p, mean = 0, sd = sqrt(varians))

print(y4)
std = sd(y4)
var = std^2

alpha = 0.05 #alpha for 95% konf.intervall 

lowerQalpha = 1-(alpha/2)
upperQalpha = alpha/2

lowerQ = qchisq(p = lowerQalpha, df = p-1)
upperQ = qchisq(p = upperQalpha, df = p-1)

lowerBound = (var*(p-1))/lowerQ
upperBound = (var*(p-1))/upperQ

m = matrix(c(lowerBound, upperBound), ncol = 2)
table = as.table(m)

print(table)
colnames(table) = c("lower", "upper")
rownames(table) = c(" ")

print(table)

#b 

B = 999
#genererer 999 varianser av samme sample som den i oppgave 4a
#pluss varaiansen til den orginale sample
b.varians = c(var, replicate(n = B, var(sample(x = y4, size = p, replace = TRUE))))
b.varians = sort(b.varians)

hist(b.varians, breaks = 50, prob = T)

#siden vi har 1000 verdier kan vi velge de 25 første som de laveste grensen og de 25 siste som den 
#høyeste grensen. 
bootQ1 = b.varians[25] 
bootQ3 = b.varians[975]

m_b = matrix(c(bootQ1, bootQ3), ncol = 2)
colnames(m_b) = c("lower", "upper")
print(m_b)

#kan se at det valgte sd er med innenfor intervallet, men det skulle heller vært mer 
#symmetrisk







