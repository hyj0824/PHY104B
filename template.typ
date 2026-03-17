// 不打断段内文本的多行数学公式
#import "@preview/mitex:0.2.6": *
#let mathblk(content) = box(width: 100%)[#content]
#let texblk(content) = mathblk(mitex(content))

#import "@preview/fancy-units:0.1.1": unit
#let u(content) = unit(per-mode: "slash", content)

// 自定义填空下划线函数
// 使用 box + line 实现更可控的下划线效果
#let field(key, value) = {
  key + "："
  box(
    stroke: (bottom: 0.5pt),
    outset: (bottom: 2pt), // 下划线向下偏移一点，避免切到文字
    inset: (x: 2pt), // 左右留白
  )[#value]
}

#let report(
  doc,
  report-title: [],
  uid: [12510430],
  name: [喻邻溥],
  date: [],
  room: [],
  time: [星期二下午],
) = {
  set document(title: report-title)
  set page(
    paper: "a4",
    numbering: "1",
    margin: (x: 2cm, y: 2cm),
  )
  set par(
    first-line-indent: (amount: 2em, all: true),
    leading: 1em,
    justify: true,
  )
  set text(font: "Noto Serif CJK SC", lang: "zh", region: "cn", size: 12pt)

  show heading: set block(below: 1em)
  // show heading.where(level: 1): set text(size: 14pt)
  // set heading(numbering: "一、")
  set enum(indent: 2em)

  place(
    top + left,
    dy: -0.5cm,
  )[#text(size: 35pt, weight: "medium")[物理实验报告]]

  place(
    top + right,
    dy: -0.7cm,
  )[#image("LOGO.png", height: 35pt)]

  v(2em)

  block[
    #set par(first-line-indent: 0pt, spacing: 7pt)
    #set text(font: "Noto Sans CJK SC", size: 10pt)
    #line(length: 100%)
    #field("学号", uid) #h(1em)
    #field("姓名", name) #h(1em)
    #field("日期", date) #h(1em)
    #field("实验室", room) #h(1em)
    #field("时间", time)
    #line(length: 100%)
  ]

  // 下面可以开始写正文...
  align(center)[#title(text(size: 20pt)[#report-title])]

  doc
}
