from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    fairy_song,
    kaleidostorm,
    magical_miracle_gx,
)

card = PokemonCardDef(
    guid="ab303b67-067b-5b0f-84f7-129bd0de55ff",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirSylveonGX.Name",
    display_name="Gardevoir & Sylveon-GX",
    searchable_by=["Gardevoir & Sylveon-GX", "Basic", "TAG TEAM", "GX", "GardevoirSylveonGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=130,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=260,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title="Fairy Song",
            game_text="Search your deck for up to 2 Fairy Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fairy_song
        ),
        Attack(
            title="Kaleidostorm",
            game_text="Move any number of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=kaleidostorm
        ),
        Attack(
            title="Magical Miracle-GX",
            game_text="If this Pok\u00e9mon has at least 3 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles their hand into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 3},
            damage=200,
            effect=magical_miracle_gx
        ),
    ],
)