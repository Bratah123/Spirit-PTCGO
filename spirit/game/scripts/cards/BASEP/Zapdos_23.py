from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import lightning_burn


card = PokemonCardDef(
    guid="4ef04ac1-5d9e-56e3-a3dd-caa99ea2931b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Lightning Burn",
            game_text="Flip a coin. If heads, and if your opponent has any Benched Pok\u00e9mon, choose 1 of them. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, Zapdos does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=lightning_burn,
        ),
    ],
)
