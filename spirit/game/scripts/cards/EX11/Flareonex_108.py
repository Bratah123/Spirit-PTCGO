"""STUB: effect not implemented — do not guess mechanics.
Flareon ex (EX11 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.card_effects.ex import evolutionary_flame_on_evolve, flame_screen_reduce, heat_tackle
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1b2e6b12-bb57-5d2f-aefd-767841c507d4",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareonex.Name",
    display_name="Flareon ex",
    searchable_by=["Flareon ex", "Stage 1", "ex", "Flareonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=108,
    set_code="EX11",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Evolutionary Flame",
            game_text="Once during your turn, when you play Flareon ex from your hand to evolve 1 of your Pok\u00e9mon, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Burned and Confused.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=evolutionary_flame_on_evolve(),
        ),
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, any damage done to Flareon ex by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flame_screen_reduce(20),
        ),
        Attack(
            title="Heat Tackle",
            game_text="Flareon ex does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=heat_tackle(10),
        ),
    ],
)