"""Client visualization vocabulary and server-side indicator lifetimes."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict


class VisualizationArrow(str, Enum):
    NONE = "None"
    NEUTRAL = "Neutral"
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NOT_APPLIED = "NotApplied"
    LARGE_NEGATIVE = "LargeNegative"
    LARGE_POSITIVE = "LargePositive"
    UNSET = "UNSET"


class VisualizationType(str, Enum):
    NOTHING = "Nothing"
    POKE_TOOL_ATTACHED = "PokeToolAttached"
    ATTACK_COST_INCREASED = "AttackCostIncreased"
    CANNOT_ACTIVATE_POKE_ABILITIES = "CannotActivatePokeAbilities"
    CANNOT_ATTACK = "CannotAttack"
    CANNOT_PLAY_ITEM = "CannotPlayItem"
    CANNOT_PLAY_SUPPORTER = "CannotPlaySupporter"
    CANNOT_PLAY_TRAINER = "CannotPlayTrainer"
    CANNOT_RETREAT = "CannotRetreat"
    CANNOT_USE_ABILITY = "CannotUseAbility"
    CANNOT_USE_POKE_POWER = "CannotUsePokePower"
    DAMAGE_DEALT_REDUCED = "DamageDealtReduced"
    DAMAGE_TAKEN_INCREASED = "DamageTakenIncreased"
    DISABLED_ATTACK = "DisabledAttack"
    FLIP_MORE_COINS_TO_AWAKEN = "FlipMoreCoinsToAwaken"
    MUST_FLIP_TO_ATTACK = "MustFlipToAttack"
    RESISTANCE_REMOVED = "ResistanceRemoved"
    RETREAT_COST_INCREASED = "RetreatCostIncreased"
    SPECIAL_BURN_AMOUNT = "SpecialBurnAmount"
    SPECIAL_POISON_AMOUNT = "SpecialPoisonAmount"
    WEAKNESS_ADDED = "WeaknessAdded"
    ADDITIONAL_ATTACK_OPTION = "AdditionalAttackOption"
    ATTACK_COST_DECREASED = "AttackCostDecreased"
    ATTACK_FOR_FREE = "AttackForFree"
    DAMAGE_DEALT_IGNORES_RESISTANCE = "DamageDealtIgnoresResistance"
    DAMAGE_DEALT_INCREASED = "DamageDealtIncreased"
    DAMAGE_DEALT_INCREASED_IF = "DamageDealtIncreasedIf"
    DAMAGE_TAKEN_PREVENTED_IF = "DamageTakenPreventedIf"
    DAMAGE_TAKEN_REDUCED = "DamageTakenReduced"
    DAMAGE_TAKEN_REDUCED_IF = "DamageTakenReducedIf"
    DAMAGE_TAKEN_RETURNS_DAMAGE = "DamageTakenReturnsDamage"
    DISCARDS_BACK_TO_HAND = "DiscardsBackToHand"
    DRAW_ENERGY_WHEN_KILLED = "DrawEnergyWhenKilled"
    FLIP_MORE_COINS_NEXT_ATTACK = "FlipMoreCoinsNextAttack"
    HP_MAX_UP = "HPMaxUp"
    IMMUNE_TO_ATTACK_EFFECTS = "ImmuneToAttackEffects"
    IMMUNE_TO_SPECIAL_CONDITIONS = "ImmuneToSpecialConditions"
    JOINED_TEAM_PLASMA = "JoinedTeamPlasma"
    MOVE_ENERGY_WHEN_ALLY_KILLED = "MoveEnergyWhenAllyKilled"
    PRIZE_CARD_VALUE_REDUCED = "PrizeCardValueReduced"
    RETREAT_COST_REDUCED = "RetreatCostReduced"
    WEAKNESS_REMOVED = "WeaknessRemoved"
    ENERGY_TYPE_CHANGED = "EnergyTypeChanged"
    ENERGY_VALUE_INCREASED = "EnergyValueIncreased"
    FORCED_COIN_FLIP_TAILS = "ForcedCoinFlipTails"
    SPECIAL_PARALYZE_DURATION = "SpecialParalyzeDuration"
    DAMAGE_DEALT_IGNORES_WEAKNESS = "DamageDealtIgnoresWeakness"
    RESISTANCE_INCREASED = "ResistanceIncreased"
    HEALS_BETWEEN_TURNS = "HealsBetweenTurns"
    CANNOT_PLAY_SPECIAL_ENERGY = "CannotPlaySpecialEnergy"
    DRAW_ADDITIONAL_PRIZE_CARD_ON_KILL = "DrawAdditionalPrizeCardOnKill"
    MAY_NOT_BE_KNOCKED_OUT = "MayNotBeKnockedOut"
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    WEAKNESS_CHANGED = "WeaknessChanged"
    TURN_CONTINUES_ON_MEGA_EVOLUTION = "TurnContinuesOnMegaEvolution"
    MUST_FLIP_TO_PLAY_TRAINER = "MustFlipToPlayTrainer"
    CANNOT_EVOLVE_FROM_HAND = "CannotEvolveFromHand"
    CANNOT_PLAY_ENERGY_FROM_HAND = "CannotPlayEnergyFromHand"
    CANNOT_PLAY_POKEMON_TOOL_CARDS_SELF = "CannotPlayPokemonToolCardsSelf"
    CAN_ONLY_BE_DAMAGE = "CanOnlyBeDamage"
    REFLIP_FOR_ATTACKS = "ReflipForAttacks"
    KILLED_ON_DAMAGE = "KilledOnDamage"
    DIES_AT_END_OF_TURN = "DiesAtEndOfTurn"
    POKEMON_TOOL_HAS_NO_EFFECT = "PokemonToolHasNoEffect"
    BENCH_DAMAGE_DEALT_AFFECTED = "BenchDamageDealtAffected"
    ALL_SUPPORTERS_AFFECTED = "AllSupportersAffected"
    UNSET = "UNSET"


class VisualizationLifetime(Enum):
    CURRENT_TURN = "current_turn"
    UNTIL_YOUR_NEXT_TURN_START = "your_next_turn_start"
    UNTIL_YOUR_NEXT_TURN_END = "your_next_turn_end"
    UNTIL_OPPONENT_NEXT_TURN_START = "opponent_next_turn_start"
    UNTIL_OPPONENT_NEXT_TURN_END = "opponent_next_turn_end"
    WHILE_IN_PLAY = "while_in_play"


@dataclass
class Visualization:
    entity_id: str
    payload: Dict[str, Any]
    lifetime: VisualizationLifetime
    player_id: str
    opponent_id: str
    created_turn: int

    def expires(self, event: str, player_id: str, turn_number: int) -> bool:
        if self.lifetime is VisualizationLifetime.WHILE_IN_PLAY:
            return False
        if self.lifetime is VisualizationLifetime.CURRENT_TURN:
            return event == "end" and turn_number >= self.created_turn
        if turn_number <= self.created_turn:
            return False
        boundary, owner = {
            VisualizationLifetime.UNTIL_YOUR_NEXT_TURN_START: ("start", self.player_id),
            VisualizationLifetime.UNTIL_YOUR_NEXT_TURN_END: ("end", self.player_id),
            VisualizationLifetime.UNTIL_OPPONENT_NEXT_TURN_START: ("start", self.opponent_id),
            VisualizationLifetime.UNTIL_OPPONENT_NEXT_TURN_END: ("end", self.opponent_id),
        }[self.lifetime]
        return event == boundary and player_id == owner
