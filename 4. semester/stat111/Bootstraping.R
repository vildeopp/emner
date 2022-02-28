set.seed(5000)

x = rnorm(n=100, mean = 2, sd = 32) 

#Tankegangen til bootsraping
s_tab = 0

for(i in 1:1000){
  x_sim = x = rnorm(n=100, mean = 2, sd = 32)

  s_tab[i] = sd(x_sim)
}

hist(s_tab)

sample(1:10, size = 4, replace = T) #eksempel på trekkning med tilbakelegging

#Bootstraping 
B = 1000 #antall samples som skal ta
n = 100 #antall elementer i hvert sample
boot_tab = 0 
for(i in 1:B){
  x_star = sample(x, size = n, replace = T)
  boot_tab[i] = sd(x_star) #standard deviation 
}
hist(boot_tab)
sd(boot_tab) #estimatoren

quantile(boot_tab, c(0.025, 0.0975)) #95% konfidensintervall basert på bootstrap av SD
