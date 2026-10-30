from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import thunderstorm


card = PokemonCardDef(
    guid="ce842b11-f744-5647-b475-d58bf112f344",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Thunderstorm",
            game_text="For each of your opponent's Benched Pok\u00e9mon, flip a coin. If heads, this attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Then, Zapdos does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=40,
            effect=thunderstorm,
        ),
    ],
)
