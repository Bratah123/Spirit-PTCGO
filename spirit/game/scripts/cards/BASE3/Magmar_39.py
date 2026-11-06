from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack, condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="d2c6b73e-13c7-5dc0-a2ef-2971aeefc77d",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
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
            title="Smog",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
