from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import photon_geyser, sky_scorching_condition, sky_scorching_light_gx

card = PokemonCardDef(
    guid="94ff5dfe-75d4-5b15-8473-54988ea1f0cc",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozmaGX.Name",
    display_name="Ultra Necrozma-GX",
    searchable_by=["Ultra Necrozma-GX", "Basic", "GX", "Ultra Beast", "UltraNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=95,
    set_code="SM6",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Attack(
            title="Photon Geyser",
            game_text="Discard all basic Psychic Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=photon_geyser,
        ),
        Attack(
            title="Sky-Scorching Light-GX",
            game_text="You can use this attack only if the total of both players' remaining Prize cards is 6 or less. Put 6 damage counters on each of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            condition=sky_scorching_condition,
            effect=sky_scorching_light_gx,
        ),
    ],
)
