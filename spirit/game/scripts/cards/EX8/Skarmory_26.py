"""STUB: effect not implemented — do not guess mechanics.
Skarmory (EX8 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.ex import heavy_metal_flip
from spirit.game.card_effects.pokemon import energy_provides_type



card = PokemonCardDef(
    guid="23ed4b26-19d7-5d2e-ae13-5afc8e88b513",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Ability(
            title="Metallic Lift",
            game_text="If Skarmory has any Metal Energy attached to it, the Retreat Cost for Skarmory is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=retreat_free_when(lambda p, _c: any(energy_provides_type(c, PokemonTypes.METAL.value) for c in p.children)),
        ),
        Attack(
            title="Spearhead",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(1),
        ),
        Attack(
            title="Heavy Metal",
            game_text="Flip a coin for each Metal Energy attached to Skarmory. This attack does 10 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=heavy_metal_flip(),
        ),
    ],
)