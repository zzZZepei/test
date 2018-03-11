###############内存管理##########################
"""
Python是如何进行内存管理的？

答:从三个方面来说,一对象的引用计数机制,二垃圾回收机制,三内存池机制
一、对象的引用计数机制（Python的垃圾收集机制主要使用的引用计数方式）
python内部使用引用计数Python的垃圾收集机制主要使用的引用计数方式
，来保持追踪内存中的对象，所有对象都有引用计数。
引用计数增加的情况：
1，一个对象分配一个新名称
2，将其放入一个容器中（如列表、元组或字典）
引用计数减少的情况：
1，使用del语句对对象别名显示的销毁
2，引用超出作用域或被重新赋值
sys.getrefcount( )函数可以获得对象的当前引用计数
多数情况下，引用计数比你猜测得要大得多。对于不可变数据（如数字和字符串），解释器会在程序的不同部分共享内存，以便节约内存。
二、垃圾回收
1，当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。
2，当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象的名称。然而由于每个对象都包含一个对其他对象的应用，
因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。
三、内存池机制
Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。
1，Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。
2，Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的malloc。
3，对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。
gc.disable()  # 暂停自动垃圾回收.
gc.collect()  # 执行一次完整的垃圾回收, 返回垃圾回收所找到无法到达的对象的数量.
gc.set_threshold()  # 设置Python垃圾回收的阈值.
gc.set_debug()  # 设置垃圾回收的调试标记. 调试信息会被写入std.err.

同时我们还使用了objgraphPython库, 本文中具体使用到的接口包括:
objgraph.count(typename)  # 对于给定类型typename,
返回Python垃圾回收器正在跟踪的对象个数.


Python有两种共存的内存管理机制: 引用计数和垃圾回收. 引用计数是一种非常高效的内存管理手段,
当一个Python对象被引用时其引用计数增加1, 当其不再被一个变量引用时则计数减1.
当引用计数等于0时对象被删除.
"""


import gc

import objgraph

gc.disable()


class A(object):
	pass

class B(object):
	pass

def test1():
	a = A()
	b = B()

test1()
print("Object count of A:",objgraph.count('A'))
print("Object count of B:",objgraph.count('B'))