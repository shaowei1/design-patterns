代码中的很多低级质量问题不需要人工去审查，java开发有很多现成的工具可以使用，比如：checkstyle，findbugs, pmd, jacaco, sonar等。

Checkstyle,findbugs,pmd是静态代码分析工具，通过分析源代码或者字节码，找出代码的缺陷，比如参数不匹配，有歧义的嵌套语句，错误的递归，非法计算，可能出现的空指针引用等等。三者都可以集成到gradle等构建工具中。

Jacoco是一种单元测试覆盖率统计工具，也可以集成到gradle等构建工具中，可以生成漂亮的测试覆盖率统计报表，同时Eclipse提供了插件可以EclEmma可以直观的在IDE中查看单元测试的覆盖情况。

Sonar Sonar 是一个用于代码质量管理的平台。可以在一个统一的平台上显示管理静态分析，单元测试覆盖率等质量报告。