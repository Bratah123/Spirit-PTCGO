from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="f072d389-30e6-57d8-8357-ca20ff46950f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=145,
    abilities=[
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Raging Thunder",
            game_text="This attack does 40 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=snipe_attack(40, side='mine', also_base=True),
        ),
    ],
)