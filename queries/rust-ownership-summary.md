---
title: Rust Ownership System Summary / Rust 所有权系统总结
tags:
  - rust
  - ownership
  - memory-safety
  - programming
date: 2026-04-14
---

# Rust Ownership System / Rust 所有权系统

## Overview / 概述

Rust's ownership system is the core feature that enables memory safety without garbage collection. It consists of a set of rules that the compiler checks at compile time.

Rust 的所有权系统是实现无垃圾回收内存安全的核心特性。它由编译器在编译时检查的一组规则组成。

---

## Three Ownership Rules / 三条所有权规则

### Rule 1: Each value has a single owner / 规则 1：每个值都有唯一的所有者

```rust
// Example 1: Single ownership / 单一所有权示例
fn main() {
    let s1 = String::from("hello");  // s1 owns the String
    let s2 = s1;                      // Ownership moves to s2
    
    // println!("{}", s1);            // ERROR: s1 is no longer valid
    println!("{}", s2);               // OK: s2 now owns the data
}
```

**Explanation / 说明:**
- When `s1` is assigned to `s2`, ownership is **moved** (not copied)
- `s1` becomes invalid after the move
- This prevents double-free errors at compile time

当 `s1` 赋值给 `s2` 时，所有权被**转移**（而非复制）。`s1` 在转移后失效，这在编译时防止了重复释放错误。

### Rule 2: When the owner goes out of scope, the value is dropped / 规则 2：当所有者离开作用域时，值会被丢弃

```rust
// Example 2: Scope and drop / 作用域与丢弃示例
fn main() {
    {
        let s = String::from("hello");  // s is valid here
        println!("{}", s);
    }                                     // s goes out of scope,
                                          // drop() is called automatically
    
    // println!("{}", s);                // ERROR: s no longer exists
}
```

**Explanation / 说明:**
- Rust automatically calls `drop()` when a variable leaves its scope
- This ensures no memory leaks without needing manual deallocation
- Similar to destructors in C++ but guaranteed by the type system

Rust 在变量离开作用域时自动调用 `drop()`，确保无需手动释放内存且不会泄漏。

### Rule 3: Values can have only one owner at a time / 规则 3：同一时间值只能有一个所有者

```rust
// Example 3: Ownership transfer in functions / 函数中的所有权转移
fn main() {
    let s = String::from("hello");
    takes_ownership(s);                  // s moves into function
    
    // println!("{}", s);                // ERROR: s was moved
    
    let x = 5;
    makes_copy(x);                       // x is copied (i32 implements Copy)
    println!("{}", x);                   // OK: x is still valid
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
}                                        // some_string goes out of scope, dropped

fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}                                        // some_integer is a primitive, no special drop
```

---

## Borrowing Rules / 借用规则

Borrowing allows you to reference a value without taking ownership.

借用允许你引用一个值而不获取其所有权。

### Immutable Borrowing / 不可变借用

```rust
// Example 4: Immutable borrows / 不可变借用示例
fn main() {
    let s1 = String::from("hello");
    
    let r1 = &s1;                        // First immutable borrow
    let r2 = &s1;                        // Second immutable borrow - OK!
    
    println!("{} and {}", r1, r2);
    // s1 is still usable here
}
```

**Rule / 规则:** You can have multiple immutable borrows simultaneously.
你可以同时拥有多个不可变借用。

### Mutable Borrowing / 可变借用

```rust
// Example 5: Mutable borrow rules / 可变借用规则示例
fn main() {
    let mut s = String::from("hello");
    
    let r1 = &s;                         // Immutable borrow
    // let r2 = &mut s;                  // ERROR: cannot borrow as mutable while immutably borrowed
    
    println!("{}", r1);                  // r1 used here, borrow ends
    
    let r2 = &mut s;                     // OK: r1's borrow ended
    r2.push_str(", world");
    println!("{}", r2);
}
```

**Rules / 规则:**
1. You can have **either** one mutable reference **or** any number of immutable references (not both)
2. References must always be valid (no dangling references)

你只能拥有**一个**可变引用**或**任意数量的不可变引用（不能同时存在）。引用必须始终有效（无悬垂引用）。

### Borrowing Summary Table / 借用规则总结表

| Borrow Type / 借用类型 | Count Allowed / 允许数量 | Can Modify / 可修改 |
|------------------------|-------------------------|---------------------|
| Immutable (&T) / 不可变 | Multiple / 多个 | No / 否 |
| Mutable (&mut T) / 可变 | One / 一个 | Yes / 是 |

---

## Lifetimes Introduction / 生命周期简介

Lifetimes are Rust's way of ensuring that references are valid for as long as they need to be.

生命周期是 Rust 确保引用在需要时始终有效的机制。

### Why Lifetimes? / 为什么需要生命周期？

```rust
// Example 6: Lifetime annotation / 生命周期标注示例
fn main() {
    let s1 = String::from("long");
    let s2 = String::from("short");
    let result;
    
    {
        let s3 = String::from("x");
        // result = longest(&s1, &s3);  // ERROR: s3 doesn't live long enough
    }
    
    result = longest(&s1, &s2);          // OK: both s1 and s2 outlive result
    println!("The longest string is {}", result);
}

// Lifetime annotation 'a means: returned reference lives as long as
// the shorter of the two input references
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

**Key Points / 关键点:**

1. **Lifetime annotations** (like `'a`) don't change how long references live - they describe relationships
   生命周期标注（如 `'a`）不改变引用的存活时间，而是描述关系

2. The compiler uses them to verify references don't outlive the data they point to
   编译器用它来验证引用不会比其指向的数据存活更久

3. Most of the time, the compiler can infer lifetimes automatically (lifetime elision rules)
   大多数情况下，编译器可以自动推断生命周期（生命周期省略规则）

### Common Lifetime Patterns / 常见生命周期模式

```rust
// Elided lifetimes (compiler infers) / 省略的生命周期
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}

// Explicit lifetimes needed / 需要显式生命周期
fn longest_with_annotation<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

---

## Summary / 总结

| Concept / 概念 | Rule / 规则 |
|---------------|------------|
| Ownership / 所有权 | Each value has one owner; moved on assignment |
| Borrowing / 借用 | Immutable: multiple OK; Mutable: one only, exclusive |
| Lifetimes / 生命周期 | Ensure references don't outlive their data |

The ownership system guarantees:
- No dangling pointers / 无悬垂指针
- No double frees / 无重复释放
- No data races / 无数据竞争

All at compile time, with zero runtime overhead!
所有这些都在编译时保证，零运行时开销！
