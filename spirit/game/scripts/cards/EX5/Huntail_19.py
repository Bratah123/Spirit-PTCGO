"""STUB: effect not implemented — do not guess mechanics.
Huntail (EX5 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dark_splash

card = PokemonCardDef(
    guid="2703ece0-554c-5324-b9b7-038a192e3c41",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Huntail"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Dark Splash",
            game_text="Does 40 damage plus 10 more damage for each Darkness Pok\u00e9mon in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=dark_splash(),
        ),
    ],
)