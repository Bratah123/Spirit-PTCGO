"""Gameplay/session wire constants, including client vocabulary recovered by
deobfuscating the PTCGO client string blob.

Strings marked "decoded" were recovered from `pie-src.dll`'s
`<PrivateImplementationDetails>{AEF74014-...}` XOR string blob
(``blob[i] ^ i ^ 0xAA`` at file offset 0x001B3B1C; accessors give the
(offset, length) slice). They are exact wire/UI values the client compares
against -- do not reword them.
"""

from enum import Enum

from spirit.game.models.board import BENCH_SLOT_COUNT


# Game State Machine Phases (server-side; never sent on the wire)
class GamePhase:
    INIT = "INIT"
    COIN_FLIP_WAIT_CHOICE = "COIN_FLIP_WAIT_CHOICE"
    COIN_FLIP_WAIT_GO_FIRST = "COIN_FLIP_WAIT_GO_FIRST"
    DEAL_HANDS = "DEAL_HANDS"
    MULLIGAN_PHASE = "MULLIGAN_PHASE"
    SETUP_PHASE = "SETUP_PHASE"
    PLACEMENT_PHASE = "PLACEMENT_PHASE"
    PRIZE_DEAL = "PRIZE_DEAL"
    SETUP_COMPLETE = "SETUP_COMPLETE"
    TURN_LOOP = "TURN_LOOP"
    GAME_OVER = "GAME_OVER"


# Opening hand size and card-move animation duration (milliseconds).
STARTING_HAND_SIZE = 7
MOVE_ANIM_DURATION_MS = 300
# Seconds to let the deck-shuffle animation play before dealing hands.
SHUFFLE_ANIM_SECONDS = 0.5
# Board capacity rules. The bench capacity mirrors the slot count serialized
# on the bench PlayArea (board.BENCH_SLOT_COUNT).
BENCH_CAPACITY = BENCH_SLOT_COUNT
PRIZE_COUNT = 6
# Safety cap on re-offers of a single selection so a misbehaving client
# cannot spin the placement loop forever.
MAX_SELECTION_RETRIES = 50

# Turn-loop safety bounds and the main action offer's timer (milliseconds).
MAX_TURNS = 500
MAX_ACTIONS_PER_TURN = 100
TURN_OFFER_LENGTH_MS = 90000


# SequenceID for standalone (unbracketed) SequenceMessages. The client's
# SequenceParser only accepts a SequenceMessage outside a Start/StopSequence
# bracket when its sequenceID is the empty GUID.
EMPTY_SEQUENCE_ID = "00000000-0000-0000-0000-000000000000"


class SelectionKind(str, Enum):
    """Every selection-node Kind the client's UI command factory recognizes.

    Decoded from the kind -> SelectionCommand table in
    ``PieSelectionNodeCommandFactory.Start()`` (pie-src). A selection offer's
    Kind (SelectionMessage ``targetType``, or a TargetInformation's ``name``
    once the chain descends into a target node) picks the UI command that
    drives highlights, drag/drop gating, and drop-zone glow. Kinds NOT in
    this table fall back to generic defaults (``r.e`` for entity lists,
    ``R.y`` for custom choices) that have no zone hints.
    """

    # Ability / play-action selection
    ABILITY = "Ability"                                     # j.V
    OUT_OF_PLAY = "OutOfPlay"                               # b.h
    ABILITY_SELECTION = "AbilitySelection"                  # K.O
    # Active-spot targeting (glow + drag onto activeTransform)
    RETREAT_NEW_ACTIVE = "RetreatNewActiveTargetInformation"        # j.U
    ACTIVE_POKEMON = "ActivePokemonTargetInformation"               # l.x
    KNOCKOUT_POKEMON = "KnockoutPokemonTargetInformation"           # b.X - knockout replace + initial active placement
    # Bench targeting (glow + drag onto benchTransform)
    INITIAL_BENCHED = "InitialBenchedTargetInformation"             # l.T - setup bench placement
    # Zone/pile selections
    PRIZE_CARD = "PrizeCardTargetInformation"                       # r.B
    RETREAT_COST_ENTITY_LIST = "RetreatCostEntityListTargetInformation"  # d.j (pip tray) / no-op
    ENERGY_COST_ENTITY_LIST = "EnergyCostEntityListTargetInformation"    # d.j
    # Pregame coin dialog
    COIN_FLIP_CHOICE = "CoinFlipChoice"                             # l.V
    GO_FIRST_CHOICE = "GoFirstChoice"                               # l.p
    # Custom-choice variants
    ORIENTATION_CUSTOM_CHOICE = "OrientationCustomChoiceTargetInformation"      # l.N
    CAKE_ATTACK_CUSTOM_CHOICE = "CakeAttackCustomChoiceTargetInformation"       # l.L
    CUSTOM_CHOICE_AS_ABILITY_SELECT = "CustomChoiceAsAbilitySelectTargetInformation"  # R.U
    CUSTOM_CHOICE_AS_ABILITY_SELECT_TAG_BONUS = "CustomChoiceAsAbilitySelectTargetInformationWithTAGBonus"  # b.q
    PARAMETERIZED_LOC_CUSTOM_CHOICE_REQUIRED = "ParameterizedLocCustomChoiceRequired"  # q.Z
    CAKE_CUSTOM_CHOICE_SHOW_REQUIRED = "CakeCustomChoiceShowRequiredTargetInformation"  # q.U
    # Reveal / composite selections
    COMPOSITE_REVEAL = "CompositeRevealEntityListTargetInformation"             # R.o
    OR_COMPOSITE_REVEAL = "OrCompositeRevealEntityListTargetInformation"        # R.k
    ANY_COMPOSITE_REVEAL = "AnyCompositeRevealEntityListTargetInformation"      # R.i
    AND_COMPOSITE_REVEAL = "AndCompositeRevealEntityListTargetInformation"      # R.f
    EXCLUSIVE_MULTI_COMPOSITE_REVEAL = "ExclusiveMultiCompositeRevealEntityListTargetInformation"  # q.X
    REVEAL_ASSOCIATED = "RevealAssociatedEntityListTargetInformation"           # R.b
    COMPOSITE_REVEAL_ASSOCIATED = "CompositeRevealAssociatedEntityListTargetInformation"  # q.r
    # List selections
    ALIGNED_ENTITY_LIST = "AlignedEntityListTargetInformation"      # R.E
    MULTI_SELECT_ENTITY_LIST = "MultiSelectEntityListTargetInformation"  # Q.N
    SLOT_ASSOCIATED_ENTITY_LIST = "SlotAssociatedEntityListTargetInformation"   # q.m
    # Generic base kind: NOT in the factory table (falls back to r.e); the
    # drag pile's active/bench drop gates accept it only when a selectable
    # entity's NameData matches ZONE_NAME_ACTIVE / ZONE_NAME_BENCH.
    ENTITY_LIST = "EntityListTargetInformation"

    def __str__(self):
        return self.value


# PlayArea NameData strings the drag pile compares against for the generic
# ENTITY_LIST kind's drop gates (decoded: aqm / aqM).
ZONE_NAME_ACTIVE = "active"
ZONE_NAME_BENCH = "bench"

LOC_KEY_DONE = "common.dialog.done"
LOC_KEY_END_TURN = "playmat.controls.endTurnButton"
LOC_KEY_CANCEL = "playmat.actionpanel.buttons.cancel.text"


TARGET_TYPE_ACTIVE = SelectionKind.KNOCKOUT_POKEMON.value
TARGET_TYPE_BENCH = SelectionKind.INITIAL_BENCHED.value
# Root Kind for the main-turn SelectionWithTargetsAndActionsRequired offer.
TARGET_TYPE_MAIN_TURN = SelectionKind.ABILITY.value

GAME_OPTION_TOKENS_KEY = "Tokens"
TOKEN_GX = "GXToken"
TOKEN_VSTAR = "VSTARToken"

# MatchFound gameOption flag that makes the client rebuild the match model from
# gameOptions and jump straight to the playmat scene (F.w.handleReconnecting).
GAME_OPTION_RECONNECTING_KEY = "Reconnecting"
GAME_OPTION_RECONNECTING_VALUE = "true"
# Grace window a detached player has to reconnect before the game is awarded to
# the connected opponent (via the concede/end_game flow).
RECONNECT_GRACE_SECONDS = 90


# Prompt sort types (informational on the wire; the client routes selection
# messages by class name, not sortType)
PROMPT_SORT_COIN = SelectionKind.COIN_FLIP_CHOICE.value
PROMPT_SORT_GO_FIRST = SelectionKind.GO_FIRST_CHOICE.value
PROMPT_SORT_MULLIGAN = "MulliganExtraDraw"

# Text Prompt Content & Buttons. All prompt strings ride LocalizableText
# {"id": ...} fields; unknown ids display as their raw text on the client.
PROMPT_CHOOSE_HEADS_TAILS = "Choose Heads or Tails"
PROMPT_HEADS = "Heads"
PROMPT_TAILS = "Tails"

PROMPT_GO_FIRST = "Would you like to go first?"
PROMPT_YES = "Yes"
PROMPT_NO = "No"

TEXT_COIN_TOSS_RESULT = "Coin Toss Result"
TEXT_HEADS_RESULT = "Heads!"
TEXT_TAILS_RESULT = "Tails!"

# Retreat target-node prompts (targetPrompt: the new-active one shows as the
# on-screen banner, the cost one becomes the energy pip tray's label).
PROMPT_RETREAT_NEW_ACTIVE = "Choose a Pokémon to be your new Active Pokémon"
PROMPT_RETREAT_COST = "Choose Energy to discard for the Retreat Cost"

# Setup phase prompts.
PROMPT_CHOOSE_ACTIVE = "Choose a Basic Pokémon to be your Active Pokémon"
PROMPT_CHOOSE_BENCH = "You may put Basic Pokémon on your Bench"
PROMPT_WAIT_OPPONENT_ACTIVE = "Please wait while your opponent chooses an Active Pokémon."
PROMPT_WAIT_OPPONENT_SETUP = "Please wait while your opponent finishes setting up."
PROMPT_WAIT_OPPONENT_DECISION = "Please wait while your opponent makes a decision."
PROMPT_MULLIGAN_EXTRA_DRAW = "Your opponent had no Basic Pokémon. Would you like to draw an extra card?"

# MulliganRevealArea does string.Format(prompt, pileCount) for its subheader.
TEXT_MULLIGAN_REVEAL_PROMPT = "Hands revealed: {0}"

# Knockout aftermath prompts.
PROMPT_TAKE_PRIZE = "Choose a Prize card to take"
PROMPT_CHOOSE_NEW_ACTIVE = "Choose a Pokémon to be your new Active Pokémon"
PROMPT_REVEAL_BASIC_FROM_PRIZE = "You may reveal a Basic Pokémon from your Prize cards."

# Pokemon Checkup (sleep flip) texts.
TEXT_SLEEP_CHECK = "Asleep Check"
TEXT_WOKE_UP = "Woke up!"
TEXT_STILL_ASLEEP = "Still Asleep!"

# Pokemon Checkup (burn flip) texts.
TEXT_BURN_CHECK = "Burn Check"
TEXT_BURN_CURED = "Cured!"
TEXT_STILL_BURNED = "Still Burned!"

# Confusion attack flip texts.
TEXT_CONFUSION_CHECK = "Confusion Check"
TEXT_CONFUSION_PROCEEDS = "Attack proceeds!"
TEXT_CONFUSION_HURT = "Hurt itself in confusion!"
