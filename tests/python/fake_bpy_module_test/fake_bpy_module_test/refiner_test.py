from fake_bpy_module.common import (    # pylint: disable=E0401
    ModuleStructure,
    EntryPoint,
    DataTypeRefiner,
    UnknownDataType,
    IntermidiateDataType,
)
from . import common


class ModuleStructureTest(common.FakeBpyModuleTestBase):

    name = "ModuleStructureTest"
    module_name = __module__

    def test_root_only(self):
        root = ModuleStructure()

        with self.assertRaises(RuntimeError):
            _ = root.name

        expect_dict = {
            "name": None,
            "children": [],
        }

        self.assertDictEqual(root.to_dict(), expect_dict)

    def test_one_child(self):
        root = ModuleStructure()

        child = ModuleStructure()
        child.name = "child_module"
        root.add_child(child)

        expect_dict = {
            "name": None,
            "children": [
                {
                    "name": "child_module",
                    "children": [],
                }
            ]
        }

        self.assertEqual(child.name, "child_module")
        self.assertEqual(root.children(), [child])
        self.assertDictEqual(root.to_dict(), expect_dict)

    def test_multiple_children(self):
        root = ModuleStructure()

        child1 = ModuleStructure()
        child1.name = "child_module_1"
        root.add_child(child1)

        child2 = ModuleStructure()
        child2.name = "child_module_2"
        root.add_child(child2)

        grandchild = ModuleStructure()
        grandchild.name = "grandchild_module"
        child2.add_child(grandchild)

        expect_dict = {
            "name": None,
            "children": [
                {
                    "name": "child_module_1",
                    "children": [],
                },
                {
                    "name": "child_module_2",
                    "children": [
                        {
                            "name": "grandchild_module",
                            "children": [],
                        }
                    ],
                }
            ]
        }

        self.assertEqual(child1.name, "child_module_1")
        self.assertEqual(child2.name, "child_module_2")
        self.assertEqual(grandchild.name, "grandchild_module")
        self.assertEqual(root.children(), [child1, child2])
        self.assertEqual(child1.children(), [])
        self.assertEqual(child2.children(), [grandchild])
        self.assertDictEqual(root.to_dict(), expect_dict)


class EntryPointTest(common.FakeBpyModuleTestBase):

    name = "EntryPointTest"
    module_name = __module__

    def test_all(self):
        entry_point = EntryPoint()
        entry_point.type = "constant"
        entry_point.module = "module.a"
        entry_point.name = "DATA"

        self.assertEqual(entry_point.type, "constant")
        self.assertEqual(entry_point.module, "module.a")
        self.assertEqual(entry_point.name, "DATA")


class DataTypeRefinerTest(common.FakeBpyModuleTestBase):

    name = "DataTypeRefinerTest"
    module_name = __module__

    def test_basic(self):
        package = ModuleStructure()
        module = ModuleStructure()
        module.name = "module"
        submodule = ModuleStructure()
        submodule.name = "submodule"
        module.add_child(submodule)
        package.add_child(module)

        entry_point_1 = EntryPoint()
        entry_point_1.type = "class"
        entry_point_1.module = "module.submodule"
        entry_point_1.name = "ClassA"
        entry_point_2 = EntryPoint()
        entry_point_2.type = "class"
        entry_point_2.module = "module"
        entry_point_2.name = "ClassB"

        refiner = DataTypeRefiner(package, [entry_point_1, entry_point_2])

        self.assertEqual(
            refiner.get_base_name("module.submodule.ClassA"), "ClassA")

        self.assertIsNone(refiner.get_module_name(None))
        self.assertEqual(
            refiner.get_module_name("module.submodule.ClassA"),
            "module.submodule")
        self.assertIsNone(refiner.get_module_name("module.submodule2.ClassA"))
        self.assertEqual(refiner.get_module_name("module.ClassB"), "module")

    def test_get_generation_data_type(self):
        package = ModuleStructure()
        module_1 = ModuleStructure()
        module_1.name = "module_1"
        submodule_1 = ModuleStructure()
        submodule_1.name = "submodule_1"
        module_1.add_child(submodule_1)
        submodule_2 = ModuleStructure()
        submodule_2.name = "submodule_2"
        module_1.add_child(submodule_2)
        package.add_child(module_1)
        module_2 = ModuleStructure()
        module_2.name = "module_2"
        package.add_child(module_2)

        entry_point_1 = EntryPoint()
        entry_point_1.type = "class"
        entry_point_1.module = "module_1.submodule_1"
        entry_point_1.name = "ClassA"
        entry_point_2 = EntryPoint()
        entry_point_2.type = "class"
        entry_point_2.module = "module_1.submodule_2"
        entry_point_2.name = "ClassB"
        entry_point_3 = EntryPoint()
        entry_point_3.type = "class"
        entry_point_3.module = "module_1"
        entry_point_3.name = "ClassC"
        entry_point_4 = EntryPoint()
        entry_point_4.type = "class"
        entry_point_4.module = "module_1"
        entry_point_4.name = "ClassD"
        entry_point_5 = EntryPoint()
        entry_point_5.type = "class"
        entry_point_5.module = "module_2"
        entry_point_5.name = "ClassE"

        refiner = DataTypeRefiner(
            package,
            [
                entry_point_1, entry_point_2, entry_point_3,
                entry_point_4, entry_point_5
            ]
        )

        self.assertIsNone(refiner.get_generation_data_type(None, "module_2"))
        self.assertEqual(
            refiner.get_generation_data_type("module_1.ClassC", None),
            "module_1.ClassC")
        self.assertEqual(
            refiner.get_generation_data_type(
                "module_1.submodule_1.ClassA", "module_2"),
            "module_1.submodule_1.ClassA")
        self.assertEqual(
            refiner.get_generation_data_type("module_1.ClassC", "module_1"),
            "ClassC")
        self.assertEqual(
            refiner.get_generation_data_type(
                "module_1.submodule_1.ClassA", "module_1.submodule_2"),
            "module_1.submodule_1.ClassA")
        self.assertEqual(
            refiner.get_generation_data_type(
                "module_1.ClassC", "module_1.submodule_1"),
            "module_1.ClassC")
        self.assertEqual(
            refiner.get_generation_data_type(
                "module_1.submodule_1.ClassA", "module_1"),
            "module_1.submodule_1.ClassA")

    def test_get_refined_data_type(self):
        package = ModuleStructure()
        module_1 = ModuleStructure()
        module_1.name = "module_1"
        submodule_1 = ModuleStructure()
        submodule_1.name = "submodule_1"
        module_1.add_child(submodule_1)
        submodule_2 = ModuleStructure()
        submodule_2.name = "submodule_2"
        module_1.add_child(submodule_2)
        package.add_child(module_1)
        module_2 = ModuleStructure()
        module_2.name = "module_2"
        package.add_child(module_2)

        entry_point_1 = EntryPoint()
        entry_point_1.type = "class"
        entry_point_1.module = "module_1.submodule_1"
        entry_point_1.name = "ClassA"
        entry_point_2 = EntryPoint()
        entry_point_2.type = "class"
        entry_point_2.module = "module_1.submodule_2"
        entry_point_2.name = "ClassB"
        entry_point_3 = EntryPoint()
        entry_point_3.type = "class"
        entry_point_3.module = "module_1"
        entry_point_3.name = "ClassC"
        entry_point_4 = EntryPoint()
        entry_point_4.type = "class"
        entry_point_4.module = "module_1"
        entry_point_4.name = "ClassD"
        entry_point_5 = EntryPoint()
        entry_point_5.type = "class"
        entry_point_5.module = "module_2"
        entry_point_5.name = "ClassE"

        refiner = DataTypeRefiner(
            package,
            [
                entry_point_1, entry_point_2, entry_point_3,
                entry_point_4, entry_point_5
            ]
        )

        unknown_data_type = UnknownDataType()
        refined_data_type = refiner.get_refined_data_type(
            unknown_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'UNKNOWN')

        intermidiate_data_type = IntermidiateDataType("list of int")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'BUILTIN')
        self.assertEqual(
            refined_data_type.modifier().modifier_data_type(), "list")
        self.assertEqual(refined_data_type.data_type(), "int")

        intermidiate_data_type = IntermidiateDataType("dict")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MODIFIER')
        self.assertEqual(refined_data_type.modifier_data_type(), "dict")

        intermidiate_data_type = IntermidiateDataType("sequence ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MODIFIER')
        self.assertEqual(refined_data_type.modifier_data_type(), "list")

        intermidiate_data_type = IntermidiateDataType("float")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'BUILTIN')
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(refined_data_type.data_type(), "float")

        intermidiate_data_type = IntermidiateDataType("string ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'BUILTIN')
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(refined_data_type.data_type(), "str")

        intermidiate_data_type = IntermidiateDataType("`module_1.ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(refined_data_type.data_type(), "module_1.ClassC")

        intermidiate_data_type = IntermidiateDataType(
            "list of `module_1.ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(
            refined_data_type.modifier().modifier_data_type(), "list")
        self.assertEqual(refined_data_type.data_type(), "module_1.ClassC")

        intermidiate_data_type = IntermidiateDataType("`module_1.ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module_1.ClassC")

        intermidiate_data_type = IntermidiateDataType("`ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module_1.ClassC")

        intermidiate_data_type = IntermidiateDataType("`ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module_1.ClassC")

        def assert_equal_commutative(expect, actual):
            def compare_func(expect, actual):
                if expect["type"] != actual.type():
                    return False
                if expect["modifier"] is None:
                    if actual.has_modifier():
                        return False
                else:
                    if expect["modifier"] \
                            != actual.modifier().modifier_data_type():
                        return False
                if expect["data_type"] is None:
                    if actual.has_modifier():
                        return False
                else:
                    if expect["data_type"] != actual.data_type():
                        return False
                if expect["modifier_add_info"] is None:
                    if actual.modifier_add_info():
                        return False
                else:
                    if expect["modifier_add_info"] \
                            != actual.modifier_add_info():
                        return False
                return True

            self.assertEqual(len(expect), len(actual))
            actual_copied = actual.copy()
            for e in expect:
                for a in actual_copied[:]:
                    if compare_func(e, a):
                        actual_copied.remove(a)
            if len(actual_copied) > 0:
                self.log("--- Expect ---")
                for e in expect:
                    self.log(f"{e}")
                self.log("--- Actual ---")
                for a in actual:
                    self.log(f"{a.to_string()}")
            self.assertEqual(len(actual_copied), 0)

        intermidiate_data_type = IntermidiateDataType(
            "(`bpy_prop_collection` of float)")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'BUILTIN',
                "modifier": "list",
                "data_type": "float",
                "modifier_add_info": None,
            },
            {
                "type": 'BUILTIN',
                "modifier": "dict",
                "data_type": "float",
                "modifier_add_info": {"dict_key": "str"},
            },
            {
                "type": 'CUSTOM',
                "modifier": None,
                "data_type": "bpy_prop_collection",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType(
            " `bpy_prop_collection` of float")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'BUILTIN',
                "modifier": "list",
                "data_type": "float",
                "modifier_add_info": None,
            },
            {
                "type": 'BUILTIN',
                "modifier": "dict",
                "data_type": "float",
                "modifier_add_info": {"dict_key": "str"},
            },
            {
                "type": 'CUSTOM',
                "modifier": None,
                "data_type": "bpy_prop_collection",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType("enum")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'BUILTIN',
                "modifier": None,
                "data_type": "str",
                "modifier_add_info": None,
            },
            {
                "type": 'BUILTIN',
                "modifier": None,
                "data_type": "int",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType("int, float")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'BUILTIN',
                "modifier": None,
                "data_type": "float",
                "modifier_add_info": None,
            },
            {
                "type": 'BUILTIN',
                "modifier": None,
                "data_type": "int",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType("int, `module_1.ClassC`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'BUILTIN',
                "modifier": None,
                "data_type": "int",
                "modifier_add_info": None,
            },
            {
                "type": 'CUSTOM',
                "modifier": None,
                "data_type": "module_1.ClassC",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType(
            "`module_2.ClassE`, `module_1.submodule_1.ClassA`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        expect = [
            {
                "type": 'CUSTOM',
                "modifier": None,
                "data_type": "module_2.ClassE",
                "modifier_add_info": None,
            },
            {
                "type": 'CUSTOM',
                "modifier": None,
                "data_type": "module_1.submodule_1.ClassA",
                "modifier_add_info": None,
            }
        ]
        assert_equal_commutative(expect, refined_data_type.data_types())

        intermidiate_data_type = IntermidiateDataType("`ClassZ`")
        refined_data_type = refiner.get_refined_data_type(
            unknown_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'UNKNOWN')

        intermidiate_data_type = IntermidiateDataType("`module_1.ClassZ`")
        refined_data_type = refiner.get_refined_data_type(
            unknown_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'UNKNOWN')

    def test_get_refined_data_type_for_custom_modifier(self):
        package = ModuleStructure()
        module = ModuleStructure()
        module.name = "module_1"
        package.add_child(module)

        entry_point = EntryPoint()
        entry_point.type = "class"
        entry_point.module = "module"
        entry_point.name = "ClassA"

        refiner = DataTypeRefiner(package, [entry_point])

        intermidiate_data_type = IntermidiateDataType(
            "`bpy_prop_collection` of `ClassA`, ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module.ClassA")
        self.assertTrue(refined_data_type.has_modifier())
        modifier = refined_data_type.modifier()
        self.assertEqual(modifier.type(), 'CUSTOM_MODIFIER')
        self.assertEqual(
            modifier.modifier_data_type(), "bpy.types.bpy_prop_collection")
        self.assertEqual(
            refined_data_type.to_string(),
            "bpy.types.bpy_prop_collection['module.ClassA']")

    def test_get_refined_data_type_for_various_patterns(self):
        package = ModuleStructure()
        module = ModuleStructure()
        module.name = "module_1"
        package.add_child(module)

        entry_point_1 = EntryPoint()
        entry_point_1.type = "class"
        entry_point_1.module = "module"
        entry_point_1.name = "ClassA"

        entry_point_2 = EntryPoint()
        entry_point_2.type = "class"
        entry_point_2.module = "module"
        entry_point_2.name = "ClassB"

        entry_point_3 = EntryPoint()
        entry_point_3.type = "class"
        entry_point_3.module = "bpy.ops.module"
        entry_point_3.name = "ClassC"

        refiner = DataTypeRefiner(
            package, [entry_point_1, entry_point_2, entry_point_3])

        intermidiate_data_type = IntermidiateDataType(
            "int in [-inf, inf], default 0, ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'BUILTIN')
        self.assertEqual(refined_data_type.data_type(), "int")
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(
            refined_data_type.to_string(), "int")

        intermidiate_data_type = IntermidiateDataType(
            "`ClassB` `bpy_prop_collection` of `ClassA`, ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module.ClassB")
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(
            refined_data_type.to_string(), "'module.ClassB'")

        intermidiate_data_type = IntermidiateDataType("`ClassB`, (readonly)")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module.ClassB")
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(
            refined_data_type.to_string(), "'module.ClassB'")

        intermidiate_data_type = IntermidiateDataType(
            "`MODULE_OT_ClassC`, ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(),
                         "bpy.ops.module.ClassC")
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(refined_data_type.to_string(),
                         "'bpy.ops.module.ClassC'")

        intermidiate_data_type = IntermidiateDataType(
            "`module.ClassB`, ")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'CUSTOM')
        self.assertEqual(refined_data_type.data_type(), "module.ClassB")
        self.assertFalse(refined_data_type.has_modifier())
        self.assertEqual(
            refined_data_type.to_string(), "'module.ClassB'")

        # Pattern: sequence of string tuples or a function
        # Ref: https://github.com/nutti/fake-bpy-module/issues/140
        intermidiate_data_type = IntermidiateDataType(
            "sequence of string tuples or a function")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MIXIN')
        dt = refined_data_type.data_types()[0]
        self.assertEqual(dt.type(), 'BUILTIN')
        self.assertEqual(dt.data_type(), "str")
        self.assertTrue(dt.has_modifier())
        self.assertEqual(dt.modifier().modifier_data_type(), "iteriter")
        self.assertEqual(dt.to_string(),
                         "typing.Iterable[typing.Iterable[str]]")
        dt = refined_data_type.data_types()[1]
        self.assertEqual(dt.type(), 'MODIFIER')
        self.assertEqual(dt.modifier_data_type(), "typing.Callable")
        self.assertEqual(dt.to_string(), "typing.Callable")

        # Pattern: `AnyType`
        # Ref: https://github.com/nutti/fake-bpy-module/issues/141
        intermidiate_data_type = IntermidiateDataType("`AnyType`")
        refined_data_type = refiner.get_refined_data_type(
            intermidiate_data_type, "module_1", 'FUNC_ARG')
        self.assertEqual(refined_data_type.type(), 'MODIFIER')
        self.assertEqual(refined_data_type.modifier_data_type(), "typing.Any")
        self.assertEqual(refined_data_type.to_string(), "typing.Any")
