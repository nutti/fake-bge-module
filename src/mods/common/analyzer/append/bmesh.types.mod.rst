.. mod-type:: append

.. module:: bmesh.types

.. class:: BMElemSeq

   :generic-types: _GenericType1

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[_GenericType1, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [_GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMVertSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMVert`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[:class:`BMVert`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [:class:`BMVert`]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMEdgeSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMEdge`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[:class:`BMEdge`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [:class:`BMEdge`]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMFaceSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMFace`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[:class:`BMFace`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [:class:`BMFace`]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMLoopSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMLoop`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[:class:`BMLoop`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [:class:`BMLoop`]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMIter

   :generic-types: _GenericType1

   .. method:: __iter__()

      :rtype: :class:`BMIter`\ [_GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: _GenericType1
      :mod-option rtype: skip-refine

.. class:: BMLayerCollection

   :generic-types: _GenericType1

   .. method:: get()

      :rtype: :class:`BMLayerItem`\ [_GenericType1] | _GenericType2
      :mod-option rtype: skip-refine
      :generic-types: _GenericType2

.. class:: BMVert

   .. method:: __getitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine

.. class:: BMEdge

   .. method:: __getitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine

.. class:: BMFace

   .. method:: __getitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine

.. class:: BMLoop

   .. method:: __getitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :generic-types: _GenericType1
      :type key: :class:`BMLayerItem`\ [_GenericType1]
      :mod-option arg key: skip-refine
