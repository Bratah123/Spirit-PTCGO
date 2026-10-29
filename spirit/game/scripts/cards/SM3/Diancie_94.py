from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import diamond_storm, sparkling_wish

card = PokemonCardDef(
    guid="70552d69-7950-5491-85ff-9d4f9c6fbc53",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Attack(
            title="Sparkling Wish",
            game_text="Search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=sparkling_wish,
        ),
        Attack(
            title="Diamond Storm",
            game_text="Heal 30 damage from each of your Fairy Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=diamond_storm,
        ),
    ],
)
