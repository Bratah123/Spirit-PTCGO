from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import gesture_gust

card = PokemonCardDef(
    guid="acc3ff04-0a75-5487-8669-fee9e10202d9",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=35,
    abilities=[
        Attack(
            title="Gesture",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gesture_gust(),
        ),
        Attack(
            title="Moon Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)