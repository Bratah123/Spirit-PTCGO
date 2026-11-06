from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import overhead_toss, terrorize


card = PokemonCardDef(
    guid="4e86aa17-5532-5efe-b236-884817333c24",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=234,
    abilities=[
        Attack(
            title="Terrorize",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, choose 1 of its attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=terrorize,
        ),
        Attack(
            title="Overhead Toss",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If tails, this attack does 10 damage to 1 of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=overhead_toss,
        ),
    ],
)
