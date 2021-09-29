#!/usr/bin/env bash
# require: bash version >= 4
# usage example: bash collect_failure_state.sh failure_state
set -eEu

# check arguments
if [ $# -ne 1 ]; then
    echo "Usage: sh download_upbge.sh <output-dir>"
    exit 1
fi

SCRIPT_DIR=$(cd $(dirname $0); pwd)

OUTPUT_DIR=${1}

mkdir -p ${OUTPUT_DIR}

GENERATED_MODS_DIR="${SCRIPT_DIR}/../../src/mods/generated_mods"
if [ -d ${GENERATED_MODS_DIR} ]; then
    cp -r ${GENERATED_MODS_DIR} ${OUTPUT_DIR}
fi

GEN_MODULE_TMP_DIRS="${SCRIPT_DIR}/../../tools/pip_package/tmp-*"
for d in ${GEN_MODULE_TMP_DIRS}; do
    if [ -d ${d} ]; then
        cp -r ${d} ${OUTPUT_DIR}
    fi
done

FAKE_BPY_MODULE_TEST_LOG_DIR="${SCRIPT_DIR}/../../fake_bpy_module_test.log"
if [ -d ${FAKE_BPY_MODULE_TEST_LOG_DIR} ]; then
    cp -r ${FAKE_BPY_MODULE_TEST_LOG_DIR} ${OUTPUT_DIR}
fi

GENERATED_TESTS_DIR="${SCRIPT_DIR}/../../generated_tests"
if [ -d ${GENERATED_TESTS_DIR} ]; then
    cp -r ${GENERATED_TESTS_DIR} ${OUTPUT_DIR}
fi
