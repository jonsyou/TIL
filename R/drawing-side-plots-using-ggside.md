# ggside를 이용한 side plots 그리기

```ggside``` 라이브러리를 활용하여 ```side-plots```를 그릴 수 있다.

우선 필요한 라이브러리를 불러온다. ```ggside```, ```tidyverse```, ```tidyquant```가 필요하다.
```r
library(ggside)
library(tidyverse)
library(tidyquant)
```

예시 데이터로 ```mpg``` 데이터를 활용하였다.
```r
mpg %>% 
  ggplot(aes(hwy, cty, color = class)) +
  geom_point(size = 2, alpha = 0.3) +
  geom_smooth(aes(color = NULL), se=TRUE) +
  geom_xsidedensity(
    aes(y = after_stat(density),
         fill = class
         ),
    alpha = 0.5,
    size = 1,
    position = 'stack'
    ) + 
  geom_ysidedensity(
    aes(
      x = after_stat(density),
      fill = class
    ),
    alpha = 0.5,
    size = 1,
    position = 'stack'
  ) +
  scale_color_tq() +
  scale_fill_tq() +
  theme_tq() +
  labs(title = 'title',
       subtitle = 'subtitle',
       x = 'x axis', y = 'y axis') +
  theme(
    ggside.panel.scale.x = 0.4,
    ggside.panel.scale.y = 0.4
  )
```
위의 코드를 통해 산점도 및 각 변수마다의 히스토그램까지 확인 가능하다.
