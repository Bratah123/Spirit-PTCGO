from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import texture_magic


card = PokemonCardDef(
    guid="b9c9bf37-8816-599f-9808-9cfe1953137a",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CoolPorygon.Name",
    display_name="Cool Porygon",
    searchable_by=["Cool Porygon", "Basic", "CoolPorygon"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=137,
    abilities=[
        Attack(
            title="Texture Magic",
            game_text="You may change Cool Porygon's Resistance to a type of your choice other than Colorless. If the Defending Pok\u00e9mon has a Weakness, you may change it to a type of your choice other than Colorless. (Benching either Pok\u00e9mon ends the effect on that Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=texture_magic,
        ),
        Attack(
            title="3-D Attack",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
    ],
)
