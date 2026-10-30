"""STUB: effect not implemented — do not guess mechanics.
Camerupt ex (EX9 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import eruption_damage, magma_armor_passive


card = PokemonCardDef(
    guid="35ffbf69-e161-5d53-9a90-2d5f2ee8fe4a",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cameruptex.Name",
    display_name="Camerupt ex",
    searchable_by=["Camerupt ex", "Stage 1", "ex", "Cameruptex"],
    subtypes=["Stage 1", "ex"],
    collector_number=92,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Magma Armor",
            game_text="Camerupt ex can't be Asleep or Paralyzed.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=magma_armor_passive(),
        ),
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 60 damage plus 20 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
                        effect=eruption_damage(60, 20),
        ),
    ],
)