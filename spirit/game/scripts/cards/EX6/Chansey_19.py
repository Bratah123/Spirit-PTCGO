from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import egg_surprise


card = PokemonCardDef(
    guid="456106a1-0757-5e7f-9591-5850fb9e5394",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Sing",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Egg Surprise",
            game_text="Flip a coin. If heads, Chansey does 50 damage to the Defending Pok\u00e9mon. If tails, remove 5 damage counters from Chansey. (All if there are less than 5.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=egg_surprise(),
        ),
    ],
)