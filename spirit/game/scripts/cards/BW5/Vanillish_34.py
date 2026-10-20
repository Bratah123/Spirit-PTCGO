from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="6eff23d5-1af4-5bc9-a228-9ebd94f09d49",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    display_name="Vanillish",
    searchable_by=["Vanillish", "Stage 1", "Vanillish"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(3, per_heads=20),
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)