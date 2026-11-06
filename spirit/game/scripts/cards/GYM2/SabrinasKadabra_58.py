from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import life_drain


card = PokemonCardDef(
    guid="5041c89d-d67e-5617-88e5-f1984a0b85e6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasKadabra.Name",
    display_name="Sabrina's Kadabra",
    searchable_by=["Sabrina's Kadabra", "Stage 1", "SabrinasKadabra"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAbra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Life Drain",
            game_text="Flip a coin. If heads, put a number of damage counters on the Defending Pok\u00e9mon so that its remaining HP are 10.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=life_drain,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
