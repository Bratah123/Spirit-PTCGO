"""STUB: effect not implemented — do not guess mechanics.
Kyogre ★ (EX11 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import critical_collection, sheer_cold


card = PokemonCardDef(
    guid="061fe370-8185-5365-8d8b-e4bb2e3d6fa8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre ★",
    searchable_by=["Kyogre \u2605", "Basic", "Star", "Kyogre"],
    subtypes=["Basic", "Star"],
    collector_number=112,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Water Energy cards and attach them to Kyogre Star.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=critical_collection(PokemonTypes.WATER),
        ),
        Attack(
            title="Sheer Cold",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=sheer_cold(),
        ),
    ],
)