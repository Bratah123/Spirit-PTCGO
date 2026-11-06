from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import thunderstorm


card = PokemonCardDef(
    guid="ec727fc5-e150-5f20-8df5-8026ef51e3fe",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
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
