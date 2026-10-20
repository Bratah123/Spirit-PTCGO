from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="c66e95ad-06c3-5595-a108-cb77951511a8",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)