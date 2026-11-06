from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import scary_face


card = PokemonCardDef(
    guid="37b4989e-3260-5ea8-b189-e4d69d813c97",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    display_name="Snubbull",
    searchable_by=["Snubbull", "Basic", "Snubbull"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=209,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, until the end of your opponent's next turn the Defending Pok\u00e9mon can't attack or retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scary_face,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
