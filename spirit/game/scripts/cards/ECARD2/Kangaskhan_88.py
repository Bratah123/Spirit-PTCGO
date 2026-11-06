from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import baby_outing


card = PokemonCardDef(
    guid="9721f30f-8f4c-5461-922e-a4f0cd82fbc3",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name",
    display_name="Kangaskhan",
    searchable_by=["Kangaskhan", "Basic", "Kangaskhan"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Baby Outing",
            game_text="Look at the top 3 cards of your deck, and then choose 1 of those cards and put it into your hand. Shuffle the rest into your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=baby_outing,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
