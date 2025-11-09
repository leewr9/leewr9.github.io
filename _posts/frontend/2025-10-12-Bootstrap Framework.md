---
title: Bootstrap Framework
category: Frontend
tag: [Bootstrap, Frontend]
---

> Bootstrap은 빠른 UI 개발, 반응형 웹 지원, 다양한 컴포넌트와 유틸리티 클래스를 제공하여 별도의 디자인 없이도 일관된 프론트엔드 화면을 쉽게 만들 수 있는 프레임워크입니다. 생산성과 일관성을 높여주며, 방대한 커뮤니티와 다양한 테마·플러그인으로 확장성도 뛰어납니다.

---

## Bootstrap

`Bootstrap`은 반응형 웹 디자인과 빠른 UI 개발을 위한 오픈소스 CSS 프레임워크입니다. `HTML`, `CSS`, `JS` 컴포넌트와 다양한 유틸리티 클래스를 제공하여, 별도의 디자인 없이도 일관된 UI를 빠르게 구현할 수 있습니다.

- 반응형 웹을 손쉽게 구현
- 다양한 브라우저와 기기에서 일관된 UI 제공
- 버튼, 폼, 네비게이션 등 다양한 컴포넌트 내장
- 유틸리티 클래스 활용으로 빠른 스타일링

{% raw %}

```html
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
  rel="stylesheet"
/>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

{% endraw %}

### Layout

`container`, `row`, `col` 클래스를 활용한 12단계 그리드 구조로 이루어집니다. 다양한 반응형 구간을 지원하여, 모바일부터 데스크탑까지 유연하게 레이아웃을 구성할 수 있습니다.

- `.container`, `.container-fluid`로 반응형 레이아웃 생성
- `.row`, `.col-*`로 12단계 그리드 배치
- `sm`, `md`, `lg`, `xl`, `xxl` 등 breakpoint 지원

### Utility

`margin`, `padding`, `text alignment`, `display`, `colors` 등 자주 쓰이는 스타일을 위한 유틸리티 클래스를 제공합니다. 여백, 정렬, 색상, 반응형 숨김 등 다양한 스타일을 손쉽게 적용할 수 있습니다.

- **여백/정렬**: `.m-3`, `.p-2`, `.text-center`, `.d-flex`, `.justify-content-between`
- **색상**: `.bg-primary`, `.text-success`, `.border-danger`
- **반응형 숨김**: `.d-none d-md-block` 등

```html
<div class="container">
  <div class="row">
    <div class="col-md-6 py-3 bg-light">왼쪽</div>
    <div class="col-md-6 py-3 bg-dark text-white">오른쪽</div>
  </div>
</div>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\bootstrap.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\bootstrap.png)

---

## Components

### Button

`Button`은 다양한 색상과 크기의 버튼을 손쉽게 만들 수 있는 컴포넌트입니다. `btn` 클래스를 기본으로, 색상/스타일별로 다양한 변형을 제공합니다.

- `.btn`, `.btn-primary`, `.btn-success` 등 다양한 스타일
- 크기, 색상, outline 등 옵션 지원

**예시**

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-outline-secondary">Outline</button>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\button.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\button.png)

### Form

`Form`은 입력 필드, 셀렉트 박스 등 폼 요소를 일관된 스타일로 구성할 수 있는 컴포넌트입니다. `form-control`, `form-select` 등 클래스를 활용해 손쉽게 적용할 수 있습니다.

- 입력창, 셀렉트 등 폼 요소 일관된 스타일
- 다양한 폼 레이아웃 및 유효성 검사 지원

**예시**

```html
<input class="form-control" type="text" placeholder="입력하세요" />
<select class="form-select">
  <option>선택</option>
  <option>옵션1</option>
</select>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\form.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\form.png)

### Navigation

`Navigation`은 상단 네비게이션 바, 탭, 메뉴 등 다양한 네비게이션 UI를 쉽게 구현할 수 있는 컴포넌트입니다. `navbar`, `nav`, `nav-tabs` 등 클래스를 활용합니다.

- 반응형 네비게이션 바, 탭, 드롭다운 등 지원
- 다양한 스타일과 조합 가능

**예시**

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Brand</a>
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
    </ul>
  </div>
</nav>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\navbar.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\navbar.png)

### Card

`Card`는 정보 박스, 프로필, 상품 등 다양한 정보를 카드 형태로 보여줄 수 있는 컴포넌트입니다. 이미지, 텍스트, 버튼 등 다양한 요소를 조합할 수 있습니다.

- 이미지, 텍스트, 버튼 등 자유로운 조합
- 리스트, 갤러리, 상품 등 다양한 용도

```html
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/150" class="card-img-top" alt="..." />
  <div class="card-body">
    <h5 class="card-title">카드 제목</h5>
    <p class="card-text">카드 내용 예시입니다.</p>
    <a href="#" class="btn btn-primary">바로가기</a>
  </div>
</div>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\card.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\card.png)

### Modal

`Modal`은 팝업 다이얼로그, 알림창 등 모달 UI를 쉽게 구현할 수 있는 컴포넌트입니다. 버튼 클릭 시 레이어 팝업 형태로 표시됩니다.

- 팝업, 알림, 확인창 등 다양한 용도
- 트리거 버튼과 함께 사용

```html
<button
  type="button"
  class="btn btn-primary"
  data-bs-toggle="modal"
  data-bs-target="#exampleModal"
>
  모달 열기
</button>

<div
  class="modal fade"
  id="exampleModal"
  tabindex="-1"
  aria-labelledby="exampleModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">모달 제목</h5>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="modal"
          aria-label="닫기"
        ></button>
      </div>
      <div class="modal-body">모달 내용입니다.</div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">
          닫기
        </button>
      </div>
    </div>
  </div>
</div>
```

[![](\assets\posts\2025-10-12-Bootstrap Framework.md\modal.png)](\assets\posts\2025-10-12-Bootstrap Framework.md\modal.png)

---

## Reference

- [Bootstrap 공식 문서](https://getbootstrap.com/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
