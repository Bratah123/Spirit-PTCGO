from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, smokescreen_attack


card = PokemonCardDef(
    guid="b6a35759-74d2-507e-b8b0-bc8b6d72dc0c",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmarex.Name",
    display_name="Magmar ex",
    searchable_by=["Magmar ex", "Basic", "ex", "Magmarex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Super Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
