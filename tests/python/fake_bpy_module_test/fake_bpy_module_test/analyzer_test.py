from pathlib import Path

import docutils
from fake_bpy_module import config  # pylint: disable=E0401
from fake_bpy_module.analyzer.analyzer import (
    BaseAnalyzer,  # pylint: disable=E0401
)

from . import common


class BaseAnalyzerTest(common.FakeBpyModuleTestBase):

    name = "BaseAnalyzerTest"
    module_name = __module__
    data_dir = Path(
        f"{Path(__file__).parent}/analyzer_test_data/base_analyzer_test").resolve()

    def setUp(self) -> None:
        super().setUp()

        self.__setup_config()

    def __setup_config(self) -> None:
        config.set_target("blender")
        config.set_target_version("2.80")

    def compare_with_file_contents(self, actual: str, expect_file: str) -> None:
        with Path(expect_file).open("r", encoding="utf-8") as f:
            expect = f.read()
        self.assertEqual(actual, expect)

    def test_no_contents(self) -> None:
        rst_files = ["no_contents.rst"]
        expect_files = ["no_contents.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_only_base_class(self) -> None:
        rst_files = ["only_base_class.rst"]
        expect_files = ["only_base_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_only_module_name(self) -> None:
        rst_files = ["only_module_class.rst"]
        expect_files = ["only_module_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_single_constant(self) -> None:
        rst_files = ["single_constant.rst"]
        expect_files = ["single_constant.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_multiple_constants(self) -> None:
        rst_files = ["multiple_constants.rst"]
        expect_files = ["multiple_constants.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_single_function(self) -> None:
        rst_files = ["single_function.rst"]
        expect_files = ["single_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_multiple_functions(self) -> None:
        rst_files = ["multiple_functions.rst"]
        expect_files = ["multiple_functions.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_single_class(self) -> None:
        rst_files = ["single_class.rst"]
        expect_files = ["single_class.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_multiple_classes(self) -> None:
        rst_files = ["multiple_classes.rst"]
        expect_files = ["multiple_classes.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_single_enum(self) -> None:
        rst_files = ["single_enum.rst"]
        expect_files = ["single_enum.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_multiple_enums(self) -> None:
        rst_files = ["multiple_enums.rst"]
        expect_files = ["multiple_enums.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_noisy_1(self) -> None:
        rst_files = ["noisy_1.rst"]
        expect_files = ["noisy_1.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_noisy_2(self) -> None:
        rst_files = ["noisy_2.rst"]
        expect_files = ["noisy_2.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_invalid_rst_format_1(self) -> None:
        rst_files = ["invalid_rst_format_1.rst"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]

        analyzer = BaseAnalyzer()
        with self.assertRaises(docutils.utils.SystemMessage):
            _ = analyzer.analyze(rst_files)

    def test_invalid_rst_format_2(self) -> None:
        rst_files = ["invalid_rst_format_2.rst"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]

        analyzer = BaseAnalyzer()
        with self.assertRaises(docutils.utils.SystemMessage):
            _ = analyzer.analyze(rst_files)

    def test_bpy_290_tweak(self) -> None:
        rst_files = ["bpy_290_tweak.rst"]
        expect_files = ["bpy_290_tweak.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        config.set_target_version("2.90")

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_bge_support(self) -> None:
        rst_files = ["bge_support.rst"]
        expect_files = ["bge_support.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        config.set_target("upbge")
        config.set_target_version("0.2.5")

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_invalid_function(self) -> None:
        rst_files = ["invalid_function.rst"]
        expect_files = ["invalid_function.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_invalid_function_arg_order(self) -> None:
        rst_files = ["invalid_function_arg_order.rst"]
        expect_files = ["invalid_function_arg_order.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_deprecated(self) -> None:
        rst_files = ["deprecated.rst"]
        expect_files = ["deprecated.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_class_name_with_arguments(self) -> None:
        rst_files = ["class_name_with_arguments.rst"]
        expect_files = ["class_name_with_arguments.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_function_with_reserved_argument_name(self) -> None:
        rst_files = ["function_with_reserved_argument_name.rst"]
        expect_files = ["function_with_reserved_argument_name.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_option(self) -> None:
        rst_files = ["option.rst"]
        expect_files = ["option.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)

    def test_generic_types(self) -> None:
        rst_files = ["generic_types.rst"]
        expect_files = ["generic_types.xml"]
        rst_files = [f"{self.data_dir}/input/{f}" for f in rst_files]
        expect_files = [f"{self.data_dir}/expect/{f}" for f in expect_files]

        analyzer = BaseAnalyzer()
        documents = analyzer.analyze(rst_files)

        self.assertEqual(len(documents), len(rst_files))
        for doc, expect in zip(documents, expect_files, strict=True):
            self.compare_with_file_contents(doc.pformat(), expect)
