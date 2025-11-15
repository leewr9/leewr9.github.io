---
title: Bootstrap Stylesheet
category: Frontend
tag: [Bootstrap, SCSS, Sass, Frontend]
---

> 스타일시트는 웹 페이지의 시각적 표현을 정의하는 중요한 요소입니다. `Bootstrap`과 `SCSS`는 효율적이고 일관된 스타일링을 가능하게 하여, 개발 생산성을 높이고 유지보수를 용이하게 합니다. 변수, 믹스인, 함수 등 SCSS의 강력한 기능을 활용하면, 일관성 있는 디자인과 생산성 높은 프론트엔드 개발이 가능합니다.

---

## SCSS

**SCSS(Sassy CSS)**는 `Sass`의 문법 중 하나로, `CSS`를 더 효율적으로 작성할 수 있게 해주는 CSS 전처리기입니다. 변수, 중첩, 연산, 재사용, 반복문 등 다양한 기능을 제공합니다.

- 색상, 폰트, 그리드 등 다양한 디자인 요소를 변수로 관리 가능
- 필요한 컴포넌트만 선택적으로 import하여 빌드 용량 최소화
- 믹스인, 함수 등으로 반복되는 스타일을 효율적으로 관리

### Variables

`Variables`는 `$` 기호로 선언하며, 색상, 폰트 크기, 여백 등 자주 사용하는 값을 재사용할 수 있습니다.
변수를 활용하면 전체 스타일의 일관성을 유지하고, 테마 변경도 쉽습니다.

```scss
$primary-color: #0d6efd;
$font-size-base: 1rem;
$spacing-unit: 0.5rem;

body {
  color: $primary-color;
  font-size: $font-size-base;
  margin: $spacing-unit * 2;
}
```

### Nesting

`Nesting`은 선택자 구조를 계층화하여, 관련 스타일을 그룹화할 수 있게 해줍니다. `CSS` 구조가 복잡할 때 코드 가독성과 유지보수성이 크게 향상됩니다.

```scss
.navbar {
  background-color: $primary-color;

  .nav-item {
    margin-right: $spacing-unit;

    .nav-link {
      color: white;

      &:hover {
        color: darken(white, 10%);
      }
    }
  }
}
```

### Directives

`Directives`는 `SCSS`에서 스타일 작성 시 제어 흐름과 재사용을 돕는 특별한 명령어입니다.

#### @mixin

`@mixin`은 재사용 가능한 스타일 블록을 만들고, `@include`로 적용합니다. 파라미터를 받아 동적으로 스타일을 생성할 수도 있습니다.

```scss
@mixin rounded($radius) {
  border-radius: $radius;
}
.btn {
  @include rounded(8px);
}
```

#### @function

`@function`은 계산이나 가공 로직을 재사용할 때 사용합니다. 복잡한 연산이나 단위 변환, 색상 가공 등에 활용됩니다.

```scss
@function px-to-rem($px) {
  @return $px / 16 * 1rem;
}
h1 {
  font-size: px-to-rem(32);
}
```

#### @for

`@for`는 반복되는 스타일을 자동으로 생성할 때 사용합니다. 규칙적인 클래스나 유틸리티 스타일을 대량으로 만들 때 유용합니다.

```scss
@for $i from 1 through 3 {
  .m-#{$i} {
    margin: #{$i}rem;
  }
}
// .m-1 { margin: 1rem; } ... .m-3 { margin: 3rem; }
```

#### @import

`@import`는 여러 SCSS 파일을 분할 관리할 때 사용합니다. 대규모 프로젝트에서 코드의 모듈화와 유지보수성을 높여줍니다.

```scss
@import "variables";
@import "mixins";
@import "components/button";
```

#### @extend

`@extend`는 기존 클래스의 스타일을 상속받아 재사용할 때 사용합니다. 공통 스타일을 여러 클래스에 쉽게 적용할 수 있습니다.

```scss
.btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
}
.btn-primary {
  @extend .btn;
  background-color: $primary-color;
  color: white;
}
```

---

## Reference

- [Bootstrap 공식문서](https://getbootstrap.com/docs/)
- [Sass 공식문서](https://sass-lang.com/documentation/)

<nav class="post-toc" markdown="1">
   <h2>Table of Contents</h2>
* TOC
{:toc}
</nav>
