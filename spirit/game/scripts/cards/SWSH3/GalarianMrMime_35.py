from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="7a1a2254-2003-51d7-b6a1-1d4f7b40faeb",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    display_name="Galarian Mr. Mime",
    searchable_by=["Galarian Mr. Mime", "Basic", "GalarianMrMime"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=122,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)