"""STUB: effect not implemented — do not guess mechanics.
Glalie (EX5 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import heavy_blizzard, ice_wall_passive

card = PokemonCardDef(
    guid="32221087-39e5-5e0a-a1a9-0d1972f953a0",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Ice Wall",
            game_text="Any damage done to Glalie by attacks from your opponent's Pok\u00e9mon with any Special Energy cards attached to it is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=ice_wall_passive(),
        ),
        Attack(
            title="Heavy Blizzard",
            game_text="Flip a coin. If heads, put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=heavy_blizzard(),
        ),
    ],
)