/**
 * @license
 * Copyright 2012 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview Text blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

// goog.provide('Blockly.Blocks.texts');  // Deprecated
// goog.provide('Blockly.Constants.Text');

// goog.require('Blockly');
// goog.require('Blockly.Blocks');
// goog.require('Blockly.FieldDropdown');
// goog.require('Blockly.FieldImage');
// goog.require('Blockly.FieldMultilineInput');
// goog.require('Blockly.FieldTextInput');
// goog.require('Blockly.FieldVariable');
// goog.require('Blockly.Mutator');


/**
 * Unused constant for the common HSV hue for all blocks in this category.
 * @deprecated Use Blockly.Msg['TEXTS_HUE']. (2018 April 5)
 */
Blockly.Constants.Text={}
Blockly.Constants.Text.HUE = 160;

Blockly.Blocks['text_print'] = {
    /**
     * Block for print statement.
     * @this {Blockly.Block}
     */
    init: function () {
        this.jsonInit({
            "message0": Blockly.Msg['TEXT_PRINT_TITLE'],
            "args0": [
                {
                    "type": "input_value",
                    "name": "TEXT"
                }
            ],
            "previousStatement": null,
            "nextStatement": null,
            "style": "text_blocks",
            "tooltip": Blockly.Msg['TEXT_PRINT_TOOLTIP'],
            "helpUrl": Blockly.Msg['TEXT_PRINT_HELPURL']
        });
    }
};