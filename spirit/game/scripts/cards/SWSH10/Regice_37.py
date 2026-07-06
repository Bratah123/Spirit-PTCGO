from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import regi_gate, blizzard_bind

card = PokemonCardDef(
    guid="59dc24d1-a4f0-503f-b004-04bb8f58f8c7",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Attack(
            title="Regi Gate",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=regi_gate,
        ),
        Attack(
            title="Blizzard Bind",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon V, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=blizzard_bind,
        ),
    ],
)
