---
title: Image Formats
category: File
tag: [Image, File]
---

> 이미지는 디지털 콘텐츠에서 가장 핵심적인 시각 자료입니다. 하지만 모든 이미지는 같은 방식으로 저장되거나 처리되지 않습니다. 크게 래스터 이미지와 벡터 이미지로 나뉘며, 각각의 포맷은 목적에 따라 선택해야 합니다.

---

## Raster Imgae
`Raster Image`는 픽셀을 기반으로 이미지를 표현하는 방식으로, 가장 일반적이고 대중적인 이미지 유형입니다. 수많은 픽셀로 구성되어 있어 복잡한 색상과 디테일을 표현하는 데 유리하지만, 해상도에 따라 품질이 영향을 받습니다.

[![](\assets\posts\2025-08-10-Image Formats.md\raster.png)](\assets\posts\2025-08-10-Image Formats.md\raster.png)

### JPEG
**JPEG(Joint Photographic Experts Group)**는 사진처럼 복잡한 색상 표현이 필요한 경우에 적합한 대표적인 포맷입니다. 손실 압축 방식으로 파일 크기를 줄이며, 대부분의 디지털 환경에서 기본적으로 사용됩니다.

[![](\assets\posts\2025-08-10-Image Formats.md\jpeg.jpg)](\assets\posts\2025-08-10-Image Formats.md\jpeg.jpg)

- 손실 압축
- 용량 대비 품질 우수
- 배경 투명도 미지원
- 반복 저장 시 화질 저하


### PNG
**PNG(Portable Network Graphics)**는 무손실 압축과 투명 배경을 지원하는 포맷으로, 로고나 UI 아이콘처럼 선명함과 투명도가 중요한 작업에 자주 사용됩니다.

[![](\assets\posts\2025-08-10-Image Formats.md\png.png)](\assets\posts\2025-08-10-Image Formats.md\png.png)

- 무손실 압축
- 투명 배경 지원
- 텍스트, 로고, 아이콘에 적합
- JPEG보다 파일 크기 큼


### GIF
**GIF(Graphics Interchange Format)**는 단순한 애니메이션을 지원하며, 제한된 색상 덕분에 용량이 작습니다. 움짤, 짧은 루프 애니메이션 등에 널리 사용됩니다.

[![](\assets\posts\2025-08-10-Image Formats.md\gif.gif)](\assets\posts\2025-08-10-Image Formats.md\gif.gif)

- 최대 256색
- 간단한 애니메이션 지원
- 단일 투명색 지원
- 낮은 색 품질


### BMP
**BMP(Bitmap)**은 마이크로소프트가 개발한 기본 래스터 이미지 포맷으로, 압축을 거의 사용하지 않아 품질 손실 없이 원본 그대로 저장됩니다.

- 무압축에 가까움
- 품질 손실 없음
- 용량이 매우 큼
- 윈도우 환경에서 널리 지원

### WebP
`WebP`는 Google이 개발한 포맷으로, `JPEG`보다 뛰어난 압축 효율을 제공하면서 `PNG`와 `GIF`의 장점도 일부 흡수한 현대적 이미지 포맷입니다.

- 손실/무손실 압축 모두 지원
- 투명도 및 애니메이션 가능
- 작은 파일 크기
- 대부분의 최신 브라우저에서 지원

### HDR
**HDR(High Dynamic Range)**은 기존 이미지보다 훨씬 넓은 밝기와 색상 범위를 저장하여 자연광과 그림자의 미묘한 차이를 표현할 수 있습니다. 주로 사진 후처리, 3D 렌더링, 게임 그래픽 분야에서 사용되며, 대표 포맷으로 `.exr`, `.hdr`이 있습니다.

- 사실적인 빛과 색 표현 가능
- 사진, 렌더링, 시각 효과에 적합

---

## Vector Image
`Vector Image`는 선, 곡선, 도형 등 수학적 정의를 통해 이미지를 표현하는 방식입니다. 확대나 축소에도 품질 저하가 없으며, 로고, 아이콘, 일러스트 등에 적합합니다.

[![](\assets\posts\2025-08-10-Image Formats.md\vector.png)](\assets\posts\2025-08-10-Image Formats.md\vector.png)

### SVG
**SVG(Scalable Vector Graphics)**는 `XML` 기반으로 작성된 벡터 이미지 포맷으로, 웹 브라우저에서 직접 렌더링되며 `CSS` 및 `JavaScript`로 조작할 수 있습니다. 인터랙티브 UI, 아이콘, 차트 등에 적합하며, 용량이 작고 버전 관리도 용이합니다.

[![](\assets\posts\2025-08-10-Image Formats.md\svg.png)](\assets\posts\2025-08-10-Image Formats.md\svg.png)

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="25" y="25" width="150" height="150" fill="blue" />
  <circle cx="100" cy="100" r="75" fill="red" />
</svg>
```

- XML 기반 텍스트 포맷
- 해상도 독립적
- CSS/JS로 동적 조작 가능
- 아이콘/웹 그래픽에 최적화
- 경량이며 Git으로 버전 관리 용이



### EPS
**EPS(Encapsulated PostScript)**는 `PostScript` 기반의 인쇄용 벡터 포맷으로, 레이아웃 유지에 강하고 고해상도 출력이 가능합니다. 웹에서는 거의 사용되지 않으며, 전문 디자인 툴이 필요합니다.

- 인쇄용 벡터 포맷
- 고해상도 출력에 적합
- 레이아웃 보존에 강함
- 웹 호환성 낮음

### AI
`AI`는 Adobe Illustrator 전용 포맷으로, 복잡한 벡터 오브젝트와 레이어, 효과 등을 포함할 수 있습니다. 웹 직접 사용은 어렵지만, 최종 출력용 포맷(SVG, EPS 등)으로 변환해 활용됩니다.

- Illustrator 전용
- 고급 벡터 구성 지원
- SVG/EPS로 내보내기 가능
- 디자인의 원본 작업용으로 사용됨

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
